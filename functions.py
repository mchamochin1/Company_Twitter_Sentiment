import tweepy
import datetime
import xlsxwriter
import sys

import pandas as pd

from openpyxl import Workbook
from openpyxl import load_workbook

# For twitter
from variables import USERNAME, FILENAME, BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, START_TIME, END_TIME

# For AWS database
from variables import USERNAME, PASSWORD, HOST, PORT
import pymysql
from sqlalchemy import create_engine

# For sentiment analysis
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def getClient():
    client = tweepy.Client( bearer_token = BEARER_TOKEN,
                            consumer_key = CONSUMER_KEY,
                            consumer_secret = CONSUMER_SECRET,
                            access_token = ACCESS_TOKEN,
                            access_token_secret = ACCESS_TOKEN_SECRET)
    return client

def createTweetsFile():

    # CSV header file
    # tweet_id: Id del mensaje
    # tweet_text: Cuerpo del texto del mensaje
    # created_at: Fecha del tweet
    # author_id: Id del autor
    # author_name: Nombre del autor
    # author_username: Nombre de usuario del autor
    # Métricas públicas del tweet:
    #   A.- retweet_count = retweet
    #   B.- reply_count = reply
    #   C.- like_count = like
    tweet_id = []
    tweet_text = []
    created_at = []
    author_id = []
    author_name = []
    author_username = []
    retweet_count = []
    reply_count = []
    like_count = []
    quote_count = []

    client=getClient()

    user = client.get_user(username=USERNAME)
    id = str(user.data.id)

    #YYYY-MM-DDTHH:mm:ss
    start_time = '2022-01-01T00:00:00Z'
    end_time =   '2022-05-22T23:59:59Z'

    #
    # Process data of the tweets and append them to a csv file
    #
    # How do I access includes data while using Paginator?
    # Paginator.flatten() flattens the data and iterates over each object.
    # To access includes, you’ll need to iterate through each response instead.
    for tweet in tweepy.Paginator(client.get_users_mentions, 
            id=id, 
            start_time = START_TIME, end_time = END_TIME,
            #exclude=['retweets', 'replies'],
            expansions='author_id',
            tweet_fields=['context_annotations','created_at','author_id', 'public_metrics'], 
            max_results=100).flatten(limit=1000):

        #
        # Create the DataFrame
        #
        tweet_id.append(tweet.id)  # Id del mensaje
        tweet_text.append(tweet.text) # Cuerpo del texto del mensaje
        created_at.append(tweet.created_at) # Fecha del tweet
        author_id.append(tweet.author_id) # Id del autor
        # Get the name of the author, user.name     
        user = client.get_user(id = str(tweet.author_id)) 
        author_name.append(str(user.data.name)) # Nombre del autor. The friendly name of this user, as shown on their profile.
        author_username.append(str(user.data.username)) # Nombre de usuario del autor. The Twitter handle (screen name) of this user.
        # Métricas públicas del tweet (retweet, reply, like, count)
        retweet_count.append(tweet.public_metrics.get('retweet_count'))
        reply_count.append(tweet.public_metrics.get('reply_count'))
        like_count.append(tweet.public_metrics.get('like_count'))
        quote_count.append(tweet.public_metrics.get('quote_count'))


    #header = ['tweet_id', 'tweet_text', 'created_at', 'author_id', 'author_name', 'author_username', 'retweet_count', 'reply_count', 'like_count', 'quote_count']
    df = pd.DataFrame({
        'tweet_id':tweet_id,
        'tweet_text':tweet_text,
        'created_at': created_at,
        'author_id':author_id,
        'author_name': author_name,
        'author_username': author_username, 
        'retweet_count':retweet_count,
        'reply_count':reply_count,
        'like_count':like_count,
        'quote_count':quote_count
        })
    # Create csv file
    df.to_csv(FILENAME, sep=';')

def createTweetsDB():

    # Connect to the MySQL database. pymysql.cursors.DictCursor is used to return dictionary
    db = pymysql.connect(host = HOST,
                        user = USERNAME,
                        password = PASSWORD,
                        cursorclass = pymysql.cursors.DictCursor
    )

    # cursor object will execute the queries and it will return the results
    cursor = db.cursor()

    # Create the database
    create_db = '''CREATE DATABASE tweet_search'''

    # Use the database
    use_db = '''USE tweet_search'''

    # Create two tables
    create_table1 = '''
    CREATE TABLE tweet_data (
    tweet_id INT,
    tweet_text TEXT,
    created_at DATE,
    retweet_count INT,
    reply_count INT,
    like_count INT,
    quote_count INT,
    author_id INT
    )
    '''
 
    create_table2 = '''
    CREATE TABLE user_data (
    author_id INT,
    author_name TEXT,
    author_username TEXT
    )
    '''

    # Drop tables
    drop_table1 = '''DROP TABLE tweet_data'''
    drop_table2 = '''DROP TABLE user_data'''

    # Drops DB
    drop_db = '''DROP DATABASE tweet_search'''

    try:
        cursor.execute(create_db)
        cursor.execute(use_db)
        cursor.execute(create_table1)
        cursor.execute(create_table2)
    except pymysql.Error as e:
        print(e)
        cursor.execute(use_db)
        cursor.execute(drop_table1)
        cursor.execute(drop_table2)
        cursor.execute(create_table1)
        cursor.execute(create_table2)
    #
    # Insert data from csv file
    #
    df = pd.read_csv(FILENAME, sep=';')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    # Produces an Engine object based on a URL
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(user = USERNAME, pw = PASSWORD, host = HOST, db = 'tweet_search'))

    # Insert the dataframe in the Data Base
    df[['tweet_id', 'tweet_text', 'created_at', 'retweet_count', 'reply_count', 'like_count', 'quote_count', 'author_id']].to_sql(
        name='tweet_data',
        con=engine,
        if_exists= 'append',
        index=False)

    df[['author_id', 'author_name', 'author_username']].to_sql(
        name='user_data',
        con=engine,
        if_exists= 'append',
        index=False)

    db.commit()
    return cursor, db


def dumpTweetsDB1(cursor):
    # Reading data from the user_data
    sql = '''SELECT * FROM user_data'''
    cursor.execute(sql)
    table1 = cursor.fetchall()
    print(table1)

def dumpTweetsDB2(cursor):
    sql = '''SELECT * FROM tweet_data'''
    cursor.execute(sql)
    table2 = cursor.fetchall()
    print(table2)

def closeTweetsDBs(db):
    db.close() # To close db when finished

def signs_tweets(tweet):
    signos = re.compile("(\.)|(\;)|(\:)|(\!)|(\?)|(\¿)|(\@)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\d+)")
    return signos.sub('', tweet.lower())

def remove_links(df):
    return " ".join(['{link}' if ('http') in word else word for word in df.split()])

def remove_stopwords(df):
    spanish_stopwords = stopwords.words('spanish')
    return " ".join([word for word in df.split() if word not in spanish_stopwords])

def spanish_stemmer(x):
    stemmer = SnowballStemmer('spanish')
    return " ".join([stemmer.stem(word) for word in x.split()])

def predictSentiment(text):

    with open("finished_model.model", "rb") as archivo_entrada:
        pipeline = pickle.load(archivo_entrada)
    
    auxText = pd.Series(text)
    test_clean = pd.DataFrame(auxText, columns=['content'])

    test_clean['content_clean'] = test_clean['content'].apply(signs_tweets) # Signos de puntuacion
    test_clean['content_clean'] = test_clean['content_clean'].apply(remove_links) # Eliminamos links
    test_clean['content_clean'] = test_clean['content_clean'].apply(remove_stopwords) # Nos cargamos stopwords
    test_clean['content_clean'] = test_clean['content_clean'].apply(spanish_stemmer) # Aplicamos el Stemmer

    predictions = pipeline.predict(test_clean['content_clean'])
    test_clean['Polarity'] = pd.Series(predictions)

    predictions = pipeline.predict_proba(test_clean['content_clean'])
    test_clean['Polarity_Pos'] = pd.Series(predictions[0][0])
    test_clean['Polarity_Neg'] = pd.Series(predictions[0][1])

    return test_clean

def tweetsCleanWords(df):

    test_clean = df.copy()

    test_clean['content_clean'] = test_clean['tweet_text'].apply(signs_tweets) # Signos de puntuacion
    test_clean['content_clean'] = test_clean['content_clean'].apply(remove_links) # Eliminamos links
    test_clean['content_clean'] = test_clean['content_clean'].apply(remove_stopwords) # Nos cargamos stopwords
    test_clean['content_clean'] = test_clean['content_clean'].apply(spanish_stemmer) # Aplicamos el Stemmer

    return test_clean

def tweetsInfluentialWords(df):
    cv = CountVectorizer(binary=True)
    reviews_train_clean = tweetsCleanWords(df)
    cv.fit(reviews_train_clean)
    X = cv.transform(reviews_train_clean)

    log_reg = LogisticRegression(C=0.5)

    target = pd.Series()

    for i in range(0, df.shape[0]):
        aux_df = predictSentiment(df.iloc[i,].tweet_text)
        target = target.append(aux_df['Polarity'])

    log_reg.fit(X, target)

    #
    # Importancia de los coeficientes. 
    # 

    # Total de palabras vectorizadas
    #print(len(log_reg.coef_[0]))

    # Cada coeficiente va asociado a una palabra
    cv.get_feature_names()

    # Montamos un diccionario con palabra -> coeficiente
    feature_to_coef = {
        word: coef for word, coef in zip(
            cv.get_feature_names(), log_reg.coef_[0]
        )
    }

    print('#### BEST POSITIVE ####')
    for best_positive in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1], 
        reverse=True)[:5]:
        print(best_positive)
    
    print('################################')

    print('#### BEST NEGATIVE ####')
    for best_negative in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1])[:5]:
        print(best_negative)
    
    return None


# Company_Twitter_Sentiment

**This project analyses the sentiment that a Corporation has in Twitter**.

**This Company wants to develop its social media monitoring by measuring the impact of their brand and commercial actions**.

In order to make this analysis, the following **tasks** are performed:

#### 1.- COLLECTION OF THE TWEETS

Tweets nentioning the Corporation are **collected from the twitter**. 

To perform this, the twitter [**Twitter-built v2 tools and libraries**](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2) is used.

The following **information** is **collected**:

1. Message id
2. Body of the message text
3. Date of the Tweet 
4. Author's id 
5. Author's name
6. Author's username
7. Public tweet metrics (retweet, reply, like, count)

#### 2.- CREATION OF A SQL DATABASE

A **MySQL database** and its related tables are created to store the information collected.

#### 3.- EXPLORATORY DATA ANALYSIS

An exploratoty data analysis is performed to **answer the following business questions**:

1. What are the tweets with the greatest social impact?
2. Which are the users who mention the Corporation the most?
3. What are the months with the highest number of tweets concentrated?
4. What are the most frequent words?
5. What is the mathematical correlation observed for the public metrics?

This is an example of the most frequent words in the tweets.

<p align="center">
<img src="https://github.com/mchamochin1/Company_Twitter_Sentiment-/blob/main/images/frequent_words.png" alt="" width="400" height="300" /> 
</p>

#### 4.- PRE-TRAINED MODEL

**A pre-trained model previously developed** is deployed to determine the sentiment of the 3 tweets with the most repercussion. This allows to **answer the following questions**:

1. What are the sentiment predictions for such tweets? 
2. What are the variables most influencing the model's predictions?
3. How could the model be improved?
4. What other opportunities are foreseen with other ML models to measure the impact of Company's brand and commercial actions?

Sentiment polarity determines if the text expresses the positive, negative or neutral sentiment of the user about the entity in consideration. This is a visualization of the tweets' sentiment polarity. Most of the polarity is positive. 

<p align="center">
<img src="https://github.com/mchamochin1/Company_Twitter_Sentiment-/blob/main/images/Sentiment.png" alt="" width="400" height="300" /> 
</p>

#### DEPLOYEMENT OF THE MODEL WITH ENDPOINTS AND AWS

The model has been deployed on the [**pythonanywhere**](https://www.pythonanywhere.com/) service provider with endpoints, for example, to return the sentiment prediction when a body of text is provided.

**MySQL** database was deployed in the **Cloud** with [**Amazon Web Services**](https://aws.amazon.com/).
<p align="center">
<img src="https://github.com/mchamochin1/Company_Twitter_Sentiment-/blob/main/images/pythonanywhere.png" alt="" width="200" height="100" /> <img src="https://github.com/mchamochin1/Company_Twitter_Sentiment-/blob/main/images/AWS.png" alt="" width="100" height="100" /> <img src="https://github.com/mchamochin1/Company_Twitter_Sentiment-/blob/main/images/mysql.png" alt="" width="100" height="100" /> <img src="https://github.com/mchamochin1/Company_Twitter_Sentiment-/blob/main/images/twitter.png" alt="" width="100" height="100" /> <img src="https://github.com/mchamochin1/Company_Twitter_Sentiment-/blob/main/images/machine-learning.jpg" alt="" width="100" height="100" />
</p>

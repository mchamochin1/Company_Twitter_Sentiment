# Company_Twitter_Sentiment
Analyse the sentiment that a Company has in Twitter

This is the case of a Corporation who wants to develop social media monitoring to measure the impact of their brand and commercial actions.

In order to make this analysis, the following tasks have been performed:

## 1.- COLLECTION OF THE TWEETS

The tweets were collected from the twitter account where the Corporation was mentioned. The twitter [**Twitter-built v2 tools and libraries**](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2)
It is recommended to use the Twitter API. You must collect:
a. message id
b. Body of the message text
c. tweet date
d. author id
and. Author's name
F. Author username
g. Public tweet metrics (retweet, reply, like, count)

## 2.- CREATION OF A SQL DATABASE
2. Store them in a SQL database in 2 different tables of your choice.

## 3.- Exploratory data analysis
3. Carry out a small analysis where the following business questions are answered:
a. What is the tweet with the greatest social impact?
b. Which user mentions the school the most?
c. In which month is the highest number of tweets concentrated?
d. What words are more frequent?
and. What kind of mathematical correlation do you find between the public metrics?

4.- PRE-TRAINED MODEL

4. Use a pre-trained model
(ds_thebridge_1_22\3-Machine_Learning\5-NLP\NLTK&CountVectorizer\data\output\ finished_model.model) to determine the sentiment of the 3 tweets with the most repercussion. Questions:
a. What are the predictions? Interpret the results.
b. What variables could have most influenced the model's predictions?
c. How could you improve the model?
d. What other opportunities can you think of where other ML models could be applied?

5.- DEPLOY MODEL (endpoint + AWS)

5. Deploy the model (not locally, you can choose the provider), with an endpoint where you can send it a body of text and return the sentiment prediction.

All the use cases that will be carried out will be developed in the Cloud (AWS).

5.- GIT REPOSITORY
6. Git repository: The tools or resources you need to develop the technical test are up to you. You will need to upload both your code and the presentation to a Git repository. The delivery will be in G Classroom, of a txt with the url of your repository.

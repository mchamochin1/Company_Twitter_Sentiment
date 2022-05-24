# Company_Twitter_Sentiment

This project analyses the sentiment that a Corporation has in Twitter for a Corporation who wants to develop social media monitoring to measure the impact of their brand and commercial actions.

In order to make this analysis, the following tasks are performed:

#### 1.- COLLECTION OF THE TWEETS

The tweets nentioning the Corporation are collected from the twitter account. For performing this, the twitter [**Twitter-built v2 tools and libraries**](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2) is used.

The following information is collected:

1. Message id
2. Body of the message text
3. Tweet date
4. Author id 
5. Author's name
6. Author's username
7. Public tweet metrics (retweet, reply, like, count)

#### 2.- CREATION OF A SQL DATABASE
A SQL database and its related tables are created to store the information collected.

#### 3.- EXPLORATORY DATA ANALYSIS
An analysis is performed with the following business questions answered:

1. What are the tweets with the greatest social impact?
2. Which users mentions the Corporation the most?
3. What are the months with the highest number of tweets concentrated?
4. What are the words more frequent?
5. What is the mathematical correlation observed from the public metrics?

#### 4.- PRE-TRAINED MODEL
A pre-trained model previously developed is deploy to determine the sentiment of the 3 tweets with the most repercussion. 

Questions:
a. What are the predictions? Interpret the results.
b. What variables could have most influenced the model's predictions?
c. How could you improve the model?
d. What other opportunities can you think of where other ML models could be applied?

#### DEPLOYEMENT OF THE MODEL WITH ENDPOINTS AND AWS
The model has been deployed on a service provider with an endpoint where it can be sent it a body of text to return the sentiment prediction.

All the use cases carried out they were deploed in the Cloud (AWS).


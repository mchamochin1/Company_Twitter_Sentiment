# Company_Twitter_Sentiment

This project analyses the sentiment that a Corporation has in Twitter for a Corporation who wants to develop its social media monitoring to measure the impact of their brand and commercial actions.

In order to make this analysis, the following tasks are performed:

#### 1.- COLLECTION OF THE TWEETS

Tweets nentioning the Corporation are collected from the twitter. 

To perform this, the twitter [**Twitter-built v2 tools and libraries**](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2) is used.

The following information is collected:

1. Message id
2. Body of the message text
3. Date of the Tweet 
4. Author's id 
5. Author's name
6. Author's username
7. Public tweet metrics (retweet, reply, like, count)

#### 2.- CREATION OF A SQL DATABASE

A MySQL database and its related tables are created to store the information collected.

#### 3.- EXPLORATORY DATA ANALYSIS

An analysis is performed to answer the following business questions:

1. What are the tweets with the greatest social impact?
2. Which are the users who mention the Corporation the most?
3. What are the months with the highest number of tweets concentrated?
4. What are the most frequent words?
5. What is the mathematical correlation observed for the public metrics?

#### 4.- PRE-TRAINED MODEL

A pre-trained model previously developed is deployed to determine the sentiment of the 3 tweets with the most repercussion. This allos to answer the following questions:

a. What are the sentiment predictions for such tweets? 
b. What are the variables most influencing the model's predictions?
c. How could the model be improved?
d. What other opportunities are foreseen with other ML models to measure the impact of Company's brand and commercial actions?

#### DEPLOYEMENT OF THE MODEL WITH ENDPOINTS AND AWS

The model has been deployed on the [pythonanywhere](https://www.pythonanywhere.com/) service provider with endpoints, for example, to return the sentiment prediction when a body of text is provided.

MySQL database was deployed in the Cloud with [Amazon Web Services](https://aws.amazon.com/).


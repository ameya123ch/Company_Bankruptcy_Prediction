

# Finance-Related Projects

## Here is the list of my Finance Projects and a detailed overview of this projects:






## 1. Online Payments Fraud Detection

![dataset-cover](https://user-images.githubusercontent.com/88341388/203754171-9b931d52-652c-4b60-a868-d97920a21181.jpg)

### Problem Statement

To identify online payment fraud with machine learning, we need to train a machine learning model for classifying fraudulent and non-fraudulent payments. 

For this, we need a dataset containing information about online payment fraud, so that we can understand what types of transactions lead to fraud. 

For this task, I collected a dataset from Kaggle, which contains historical information about fraudulent transactions which can be used to detect fraud in online payments. Below are all the columns from the dataset I’m using here:

###### Challenges Faced

Imbalanced Dataset

Outliers

App

![Screenshot (7)](https://user-images.githubusercontent.com/88341388/210163372-5447d565-60f0-4f9f-aeb6-dd21354571fb.png)




## 2. Credit Score Classification

![istockphoto-1200726951-612x612](https://user-images.githubusercontent.com/88341388/203758077-9342a869-9631-49ae-91b6-136b0c4d9554.jpg)

###### Problem Statement

You are working as a data scientist in a global finance company. Over the years, the company has collected basic bank details and gathered a lot of credit-related information. The management wants to build an intelligent system to segregate the people into credit score brackets to reduce the manual efforts.



###### Task

Given a person’s credit-related information, build a machine learning model that can classify the credit score.



###### Dataset link : https://www.kaggle.com/datasets/clkmuhammed/creditscoreclassification







## 3. Stock Price Forecasting App

![91867Screenshot (125)](https://user-images.githubusercontent.com/88341388/203889985-dc079235-1694-4cf3-8176-f749c2e27604.png)

###### Content

Stocks and financial instrument trading is a lucrative proposition. Stock markets across the world facilitate such trades and thus wealth exchanges hands. Stock prices move up and down all the time and having ability to predict its movement has immense potential to make one rich.

Stock price prediction is the task of forecasting the future value of a given stock. Given the historical daily close price, prepare and compare forecasting solutions.

###### Dataset

The historical stock price information is also publicly available. For our current use case, we will utilize the pandasdatareader library to get the required 4 stocks which are Goldman Sachs, Morgan Stanley, JP Morgan Chase and Citigroup using Yahoo Finance databases.


###### Tools used for this Project
Stock price forecasting:

Facebook Prophet

Deployment :

Streamlit

Huggingface






## 4. Finanical News Sentiment Analysis

![project-2](https://user-images.githubusercontent.com/88341388/211352023-4366ae1b-f4b5-41f2-9836-2fb30ed0aeed.jpeg)

###### About the Dataset

India financial news sentiment analysis dataset compiled together.

Date range: Jan 1, 2017 to April 15, 2021

News sources:
Indian sources: Economic Times, Money Control, Livemint, Business Today, Financial Express
Foreign sources: NY Times, WSJ, Washington Post

Keywords:
Indian sources: "economy" or "markets" or "inflation"
Foreign sources: "Indian economy" OR "India economy" OR "Indian businesses" OR "Indian business"

Sentiment analysis: Performed using flair NLP model. All confidence scores for NEGATIVE sentiment datapoints have been multiplied by -1 from the original flair output. Basic cleanup of data done to remove repetition of headlines and all headlines less than 30 characters are ignored.

Acknowledgements: GDELT Headline Scrape script from Prof. Ken Blake (https://drkblake.com/gdeltheadlinescrape/) has been used to generate the news headlines dataset.

Motivation: The intent of generating this data was to compile recent years financial news headlines for India and perform sentiment analysis on it.

Tools used to create & deploy app:

streamlit and hugging face

Check out my app: https://huggingface.co/spaces/ameya123ch/FinanicalNewsSentimentAnalysis







## 5. Company Bankruptcy Prediction

![business-man-watching-company-go-bankrupt-pop](https://user-images.githubusercontent.com/88341388/203910486-bbc908c2-1d3b-4d79-b760-dcac7341b9fc.jpg)

Bankruptcy data from the Taiwan Economic Journal for the years 1999–2009

###### Context

The data were collected from the Taiwan Economic Journal for the years 1999 to 2009. Company bankruptcy was defined based on the business regulations of the Taiwan Stock Exchange.

###### Source

Deron Liang and Chih-Fong Tsai, deronliang '@' gmail.com; cftsai '@' mgt.ncu.edu.tw, National Central University, Taiwan The data was obtained from UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Taiwanese+Bankruptcy+Prediction


###### Dataset link : https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction


###### Task
Create a model which can classify whether the company will go bankcrupt or not

###### Challenges Faced

Outliers

Imbalanced Dataset











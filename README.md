

# Finance-Related Data Science Projects

## Here is the list of my Finance Projects and a detailed overview of this projects:


## 1. Stock Price Forecasting App

![91867Screenshot (125)](https://img.etimg.com/thumb/height-450,width-600,imgsize-180242,msid-87946375/.jpg)

### Content

Stocks and financial instrument trading is a lucrative proposition. Stock markets across the world facilitate such trades and thus wealth exchanges hands. Stock prices move up and down all the time and having ability to predict its movement has immense potential to make one rich.

Stock price prediction is the task of forecasting the future value of a given stock. Given the historical daily close price, prepare and compare forecasting solutions.

### Dataset

The historical stock price information is also publicly available. For our current use case, we will utilize the pandasdatareader library to get the required 4 stocks which are Goldman Sachs, Morgan Stanley, JP Morgan Chase and Citigroup using Yahoo Finance databases.


### Tools used for this Project
Stock price forecasting:

Facebook Prophet

Deployment :

Streamlit

Huggingface






## 2. Finanical News Sentiment Analysis


![sentiment_gif_v02b](https://user-images.githubusercontent.com/88341388/226693375-65664154-529a-4dd8-bd34-14251b7797b1.gif)


### Problem Statement

People with non-financial knowledge need to improve in making investment decisions.The solution to this problem could be visiting a trustworthy financial advisor. What if you do homework before visiting a financial advisor to ensure they are right about the current market condition?

### Goal

To provided a user-friendly and efficient way for individuals to stay informed and make informed investment decisions, leading to improved financial outcomes.


### Tools used to create & deploy app

Tensorflow,streamlit and hugging face spaces


### About the Dataset

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


### App 

https://huggingface.co/spaces/ameya123ch/Financial_Sentiment_Analysis







## 3. Company Bankruptcy Prediction

![business-man-watching-company-go-bankrupt-pop](https://img.etimg.com/thumb/msid-90690911,width-1070,height-580,imgsize-345899/photo.jpg)

Bankruptcy data from the Taiwan Economic Journal for the years 1999–2009

### Context

The data were collected from the Taiwan Economic Journal for the years 1999 to 2009. Company bankruptcy was defined based on the business regulations of the Taiwan Stock Exchange.

### Source

Deron Liang and Chih-Fong Tsai, deronliang '@' gmail.com; cftsai '@' mgt.ncu.edu.tw, National Central University, Taiwan The data was obtained from UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Taiwanese+Bankruptcy+Prediction


### Dataset link : https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction


### Task
Create a model which can classify whether the company will go bankcrupt or not

### Challenges Faced

Outliers

Imbalanced Dataset











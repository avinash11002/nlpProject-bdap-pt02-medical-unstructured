# nlpProject-bdap-pt02-medical-unstructured
This is Project for BDAP PT 02 student for NLP Assignment

We have developed this program in R Language

The following libraries were used for this project and the visualization was done using sundial package.

# CRAN
library(twitteR)
library(ROAuth)
library(SnowballC)
library(ggplot2)
library(RColorBrewer)
library(httr)
library(RCurl)
library(XML)
library(devtools)
library(sqldf)
#downloaded the next
library(BiocGenerics)
library(graph)
library(Rgraphviz)
library(Rstem)
library(slam)
library(tm) #CRAN
library(modeltools) #CRAN
library(sentiment)
library(wordcloud)
#Downloaded gsl dependency first
#sudo yum install gsl-devel
library(topicmodels)
library(shiny)
library(sunburstR)

-----------------------------------

In addition to this we have used LDA algorithm to identify the topic and sentiment packages to classify the sentiments.

------------------------------------

Then using oAuth we picked the tweets from tweeter, approximately 3000 in numbers

we removed the stop words and did the stemming before using LDA to identify the topics then using SunBurst we did the visualization.

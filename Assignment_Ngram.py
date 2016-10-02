# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:37:52 2016
BDAP part Time batch 2
Group 5
Project 2

Avinash Tiwari
Vishawajeet Deshmukh
Avinash Tiwari
Mithilesh
Ganesh Shinde
Sachidanand Tripathi
@author: Ganesh
"""

import nltk
# from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

with open(r"InputDataForNgram") as inputData:
    data = inputData.read()

dataWithoutPun = RegexpTokenizer(r'\w+')
token = dataWithoutPun.tokenize(data)


def ngramfunction(token, number):
    totCount = len(token)

    ngramlist = ngrams(token, number)
    fdist = nltk.FreqDist(ngramlist)

    # FreqUnigramData = list(fdist.keys())
    # unigramResult = FreqUnigramData[0:100]

    # print(unigramResult)
    # fdist.plot(50,cumulative=False)

    # fdist.tabulate()

    fdist.values()
    fdist.keys()

    a = {}
    for k in fdist.keys():
        a.update({k: fdist.get(k)})

    sorted_names = sorted(a, key=a.__getitem__, reverse=True)

    j = 0

    print("Elements_in_ N-Gram","Frequency","Probability" ,sep = "\t")
    for i in sorted_names:
        if j > 100:
            break
        print(str(i),str(a[i]) ,str(round(float(int(a[i]) / totCount), 4)), sep="\t")
        j = j + 1


print("=============================================================================")
print("========================Top 100 Unigrams=====================================", end="\n")
unigrams = ngramfunction(token, 1)
print("========================Top 100 bigrams======================================", end="\n")
bigrams = ngramfunction(token, 2)
print("========================Top 100 Trigrams=====================================", end="\n")
trigrams = ngramfunction(token, 3)
print("=============================================================================")

# Removing stop words and generating
stop_words = set(stopwords.words('english'))
# print(stop_words)
for doc in data:
    data_without_stopwords = [i.lower() for i in token if i.lower() not in stop_words]

print("====================Top 100 Unigrams without Stop Words======================", end="\n")
unigrams = ngramfunction(data_without_stopwords, 1)
print("====================Top 100 bigrams without Stop Words=======================", end="\n")
bigrams = ngramfunction(data_without_stopwords, 2)
print("====================Top 100 Trigrams without Stop Words======================", end="\n")
trigrams = ngramfunction(data_without_stopwords, 3)
print("=============================================================================")
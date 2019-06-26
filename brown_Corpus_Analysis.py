#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:24:46 2019
"Brown Corpus Analysis"
@author: Singh Gagan Deep
The Brown Corpus was the first million-word electronic corpus of English, 
created in 1961 at Brown University. 
This corpus contains text from 500 sources, 
and the sources have been categorized by genre, such as news, editorial, and so on. 
(for a complete list, see http://icame.uib.no/brown/bcm-los.html).

Reference http://www.nltk.org/book/ch02.html
"""

# Importing brown corpus
from nltk.corpus import brown
category=brown.categories()

# function to analysis the various keywords for a specific topic
def brown_words(new):
    new_list=[]
    for words in new:
        new_list.append(words)
    return new_list
total_words=brown_words(new=brown.words(categories='editorial'))

print(len(brown_words(new=brown.words(categories='editorial'))))


set(brown_words(new=brown.words(categories='news')))

print(len(brown_words(new=brown.words(categories='news'))))

print(len(set(total_words)))
    
''' 
There are 61604 words are in "editorial "category from which around 9890 words are unique
And  1000554 total words in " news category" from which around 14394 words are unique
'''
'''
The Brown Corpus is a convenient resource for studying systematic differences between genres, 
a kind of linguistic inquiry known as stylistics. 
Let's compare genres in their usage of modal verbs. 
The first step is to produce the counts for a particular genre.
'''
import nltk
news_text=brown.words(categories='news')
fdist=nltk.FreqDist(w.lower() for w in news_text)
model=['can', 'could','may','might','must','will']
for m in model:
    print(m + ':', fdist[m], end=' ')

'''
we need to obtain counts for each genre of interest.
We'll use NLTK's support for conditional frequency distribution
''' 
model1=['When','where','why','is','are']

cfd=nltk.ConditionalFreqDist((genre,word)
for genre in brown.categories() for word in brown.words(categories=genre))
genre=['news','religion','hobbies','science_fiction','romance','humor']
model=['can', 'could','may','might','must','will']
#model1=['When','where','why','is','are']
cfd.tabulate(conditions=genre,samples=model)







    






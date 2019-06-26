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
brown_words(new=brown.words(categories='editorial'))

print(len(brown_words(new=brown.words(categories='editorial'))))


brown_words(new=brown.words(categories='news'))

print(len(brown_words(new=brown.words(categories='news'))))

# We can see the no of words for different categories as here with our function we can analysis the keywords news and categories. 

    
    
    
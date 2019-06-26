#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:27:45 2019
Accessing Text Corpora and Lexical Resources
@author: Singh Gagan Deep
"""

# Working with the smallset of Gutenberg Corpus 

from nltk.corpus import gutenberg
gutenberg.fileids()

emma=gutenberg.words('austen-emma.txt')
len(emma)

for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid))
    num_words=len(gutenberg.words(fileid))
    num_sents=len(gutenberg.sents(fileid))
    num_vocab=len(set(w.lower() for w in gutenberg.words(fileid)))
    print("Average word length ",round(num_chars/num_words),"\n Average sentence Length ", round(num_words/num_sents),"\n number of times each vocabulary item appears in the text on average",round(num_words/num_vocab),"\n field Name",fileid)

shakes_macbeth=gutenberg.sents('shakespeare-macbeth.txt')
shakes_macbeth[1116]
longest_len=max(len(s) for s in shakes_macbeth)
[s for s in shakes_macbeth if len(s) == longest_len]

# Web and Chat Text
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65], '...')
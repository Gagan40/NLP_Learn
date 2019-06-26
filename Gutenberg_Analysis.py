#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:27:45 2019
Accessing Text Corpora and Lexical Resources
refrence taken from http://www.nltk.org/book/ch02.html
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
    

'''
Instant chat analysis
There is also a corpus of instant messaging chat sessions, 
originally collected by the Naval Postgraduate School 
for research on automatic detection of Internet predators. 
The corpus contains over 10,000 posts, 
anonymized by replacing usernames with generic names of the form "UserNNN", 
and manually edited to remove any other identifying information. 
The corpus is organized into 15 files, 
where each file contains several hundred posts collected on a given date, 
for an age-specific chatroom (teens, 20s, 30s, 40s, plus a generic adults chatroom). 
The filename contains the date, chatroom, and number of posts; 
e.g., 10-19-20s_706posts.xml contains 706 posts gathered from the 20s chat room on 10/19/2006.

'''
from nltk.corpus import nps_chat
chatroom=nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]

chatroom2=nps_chat.posts('11-09-40s_706posts.xml')
chatroom[123]


chatroom_adult=nps_chat.posts('11-09-adults_706posts.xml')
chatroom_adult[123]
















# -*- coding: utf-8 -*-
"""
Spyder Editor
@author: Singh Gagan Deep
Basic understanding of Natural Language Processing
using the nltk library
"""

import nltk
nltk.download()
from nltk.corpus import brown
brown.words()[0:10]
dir(brown)
len(brown.words())
from nltk.book import *
dir(text1)
len(text1)

from nltk import sent_tokenize, word_tokenize, pos_tag
text = "Machine learning is the science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI."
#len(text)
sents=sent_tokenize(text)
sents
len(sents)

tokens=word_tokenize(text)
tokens

tagged_tokens=pos_tag(tokens)
tagged_tokens

# Sentence tokenizing
from nltk import sent_tokenize, word_tokenize
text="this’s a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn."
sent_token_list=sent_tokenize(text)
sent_token_list
len(sent_token_list)
#tok=word_tokenize(text)


import nltk.data

#for french sentence tokenizing example
french_token=nltk.data.load('tokenizers/punkt/french.pickle')
french_token.tokenize('comment ça va. Bien merci et toi ?')

# tokenizing text into words

from nltk import word_tokenize
word_tokenize('Hello world')

word_tokenize('This is a text')
#Another equivalent call method like the following:
from nltk.tokenize import TreebankWordTokenizer
tokenizer=TreebankWordTokenizer()
tokenizer.tokenize('This is a text')


from nltk.book import *
text1
text1.concordance("monstrous")
text1.similar("monstrous")
text2.similar("monstrous")
text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])
text4
words='This is not a good idea i think so'
text3.generate(words)


len(text3)

# how many distinct words the book of Gensis have
sorted(set(text3))

len(set(text3))

# Measure the richness of Lexical richness of text
len(set(text3))/len(text3)
'''
The Lexical Analysis shows us that the number of distinct words is just 
6% of the total number of words, 
or equivalently that each word is used 16 times on average
'''


'''
Now, let's focus on particular word. 
We can count how often a word occurs in a text, 
and compute what percentage of the text is taken up by a specific word:
'''  
text3.count('God')
# So we could see that the word God occurs 231 times

# Now calculate the percentage
100*text3.count('God') / len(text3)

def diversity_lexical(text):
    return len(set(text))/len (text)

diversity_lexical(text5)
diversity_lexical(text6)
'''
Frequency Distribution 
Tt tells us the frequency of each vocabulary item in the text.
NLTK provides FreqDist method to do this task
'''
fre_dis=FreqDist(text1)

# Frequency distribution of most 50 frequent words
fre50=fre_dis.most_common(50)

'''
Do any words produced in the last example help us grasp the topic or genre of this text? 
Only one word, whale, is slightly informative! It occurs over 900 times. 
The rest of the words tell us nothing about the text; they're just English "plumbing." 
'''

'''What proportion of the text is taken up with such words? 
We can generate a cumulative frequency plot for these words
'''
fre_dis.plot(50,cumulative=True)


'''
If the frequent words don't help us, 
how about the words that occur once only, 
the so-called hapaxes? View them by typing fdist1.hapaxes().
'''
once_occur_words=fre_dis.hapaxes()

'''
This list contains lexicographer, cetological, contraband, expostulations, 
and about 9,000 others. 
It seems that there are too many rare words, 
and without seeing the context we probably can't guess what half of the hapaxes mean in any case! 
Since neither frequent nor infrequent words help, we need to try something else.
'''


'''
Fine-grained Selection of Words
let's look at the long words of a text; perhaps these will be more characteristic and informative. 
For this we adapt some notation from set theory. 
We would like to find the words from the vocabulary of the text that are more than 15 characters long. 
Let's call this property P, so that P(w) is true if and only if w is more than 15 characters long. 
Now we can express the words of interest using mathematical set notation  . 
This means "the set of all w such that w is an element of V (the vocabulary) and w has property P".

	
	{w | w ∈ V & P(w)}
	[w for w in V if p(w)]

'''
V=set(text1)
long_words=[w for w in V if len(w) > 15]
sorted(long_words)

''' 
So here we could see that there are some words which gives us the idea about text
Now applied the same methodology on different texts
''''

fdisk5=FreqDist(text5)
sorted([w for w in set(text5) if len(w)>7 and fdisk5[w]>7])

'''
Notice how we have used two conditions: len(w) > 7 ensures that the words are longer than seven letters,
 and fdist5[w] > 7 ensures that these words occur more than seven times. 
 At last we have managed to automatically identify the frequently-occurring content-bearing words 
 of the text. It is a modest but important milestone: a tiny piece of code, 
 processing tens of thousands of words, produces some informative output.
''' 


'''
Collocations and Bigrams
A collocation is a sequence of words that occur together unusually often. 
Thus red wine is a collocation, whereas the wine is not. 
A characteristic of collocations is that they are resistant to 
substitution with words that have similar senses; for example, maroon wine sounds definitely odd.

To get a handle on collocations, 
we start off by extracting from a text a list of word pairs, also known as bigrams. 
This is easily accomplished with the function bigrams()
'''
list(bigrams(['more','is','said','then','done']))

'''
Here we see that the pair of words than-done is a bigram, 
and we write it in Python as ('than', 'done'). 
Now, collocations are essentially just frequent bigrams, 
except that we want to pay more attention to the cases that involve rare words.
 In particular, we want to find bigrams that occur more often than 
 we would expect based on the frequency of the individual words. 
 The collocations() function does this for us.
'''
text4.collocations()


'''
Counting other things

Counting words is useful, but we can count other things too.
 For example, we can look at the distribution of word lengths in a text, 
 by creating a FreqDist out of a long list of numbers, 
 where each number is the length of the corresponding word in the text:
'''

[len(w) for w in text1]
fdist=FreqDist(len(w) for w in text1)

fdist.most_common()
fdist.freq(3)





























































































































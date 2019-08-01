# -*- coding: utf-8 -*-
"""
Spyder Editor

NLTK book Chapter1
# Singh Gagan
# Date:31July 2019
"""

# Introduction of NLTK Book

from nltk.book import *

""" 
Searching Text
There are many ways to examine the context of a text apart from simply reading it. 
A concordance view shows us every occurrence of a given word, together with some context.
 Here we look up the word monstrous in Moby Dick by entering text1
"""
text1.concordance("monstrous") # Display all 11 occurence of "Mondtrous Words"
text1.concordance("affection") # Display all 3 occurence of word affection
text2.concordance("affection") # Display all 25 occurence of word affection

# we  obtained different results for different text
text1.similar("monstrous")
text2.similar("monstrous")

"""
The term common_contexts allows us to examine just the contexts
that are shared by two or more words, such as monstrous and very
"""

text2.common_contexts(["monstrous","very"])

text3.concordance("god")

text3.common_contexts(["god","after"])

"""
It is one thing to automatically detect that a particular word occurs in a text, 
and to display some words that appear in the same context. 
However, we can also determine the location of a word in the text how many words from the beginning it appears. 
This positional information can be displayed using a dispersion plot. 
Each stripe represents an instance of a word, and each row represents the entire text.

"""

text2.dispersion_plot(["affection","god","said","other"])

#Lexical Dispersion Plot for Words in U.S. Presidential Inaugural Addresses: This can be used to investigate changes in language use over time.
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# Counting vocablary

len(text3) # 44764

"""
So Genesis has 44,764 words and punctuation symbols, or "tokens.
A token is the technical name for a sequence of characters — such as hairy, his, or :) — that we want to treat as a group. 
When we count the number of tokens in a text, say, the phrase to be or not to be, 
we are counting occurrences of these sequences. 
Thus, in our example phrase there are two occurrences of to, two of be, and one each of or and not. 
But there are only four distinct vocabulary items in this phrase. 
How many distinct words does the book of Genesis contain? 
To work this out in Python, we have to pose the question slightly differently. 
The vocabulary of a text is just the set of tokens that it uses, since in a set, all duplicates are collapsed together. 

"""
sorted(set(text3))

len(sorted(set(text3))) # 2789
# set containts the non duplicate values

#calculate a measure of the lexical richness of the text.
len(sorted(set(text3)))/len(sorted(text3)) # he number of distinct words is just 6% of the total number of words

# Next, let's focus on particular words. We can count how often a word occurs in a text, 
#and compute what percentage of the text is taken up by a specific word:
text3.count("smote") # 5 times
100 * text4.count('a') / len(text4) # 1.457973123627309


text5.count('lol') # the word lol occured 704 limes in text

# creating a function to calculate the Lexical_Diversity
def lexical_diversity(text):
    return len(set(text)) / len(text)
lexical_diversity(text1)

"""
Lexical Diversity for text1 = 0.07406285585022564
Lexical Diversity for text2 = 0.04826383002768831
Lexical Diversity for text3 = 0.06230453042623537
Lexical Diversity for text4 = 0.06617622515804722
Lexical Diversity for text5 = 0.13477005109975562
Lexical Diversity for text6 = 0.1276595744680851
Lexical Diversity for text7 = 0.12324685128531129
Lexical Diversity for text8 = 0.22765564002465585
Lexical Diversity for text9 = 0.0983485761345412
"""

# Creating a function for calculating the the percentage of a word out of total nimbers
def percentageCount(count,total):
    return 100* count/total 

percentageCount(text4.count('a'),len(text4))

percentageCount(text5.count('lol'),len(text5))

"""
What is a text? At one level, it is a sequence of symbols on a page such as this one.
At another level, it is a sequence of chapters, made up of a sequence of sections, 
where each section is a sequence of paragraphs, and so on. 
However, for our purposes, we will think of a text as nothing more than a sequence of words and punctuation
In python we works with text using lists
"""
sent1 # ['Call', 'me', 'Ishmael', '.']
len(sent1) # length 4
lexical_diversity(sent1) #1.0

sent2 # ['The','family', 'of', 'Dashwood', 'had', 'long', 'been', 'settled', 'in', 'Sussex', '.']
len(sent2) # length of sent 2 is 11
lexical_diversity(sent2) # 1.0

# User defined test 

user_defined_sent=['Hi','I','am','new','to','NLP','.','Ensuit','I','will','become','Expert']

type(user_defined_sent) # It is list
len(user_defined_sent) # length is 12
lexical_diversity(user_defined_sent)  # 1.0
user_defined_sent.count('I') # 2
sorted(user_defined_sent)
len(set(user_defined_sent))

sent1+user_defined_sent # adding two list

user_defined_sent.append('with love') # appending text or item  in list
user_defined_sent # ['.', 'Ensuit', 'Expert', 'Hi', 'I', 'I', 'NLP', 'am', 'become', 'new', 'to', 'will', 'with love']

# indexing list
# we could see the word or item on the desired index as follow
text4[173] # so at index 173 the word 'awaken' in available
# we could also check the index value for a paricular item 
text4.index('awaken') # 173

"""
Indexes are a common way to access the words of a text, 
or, more generally, the elements of any list. 
Python permits us to access sublists as well, 
extracting manageable pieces of language from large texts, a technique known as slicing.
"""
text5[16715:16735] 
user_defined_sent[3:5] #  ['Hi', 'I']

saying=['After','all','is','said','and','done','more','is','said','than','done']
token=set(saying)
token=sorted(token)
token[-2:]

"""
Frequency Distributions
How can we automatically identify the words of a text that are most informative about the topic
and genre of the text? 
Imagine how you might go about finding the 50 most frequent words of a book. 
One method would be to keep a tally for each vocabulary item, 
The tally would need thousands of rows, and it would be an exceedingly laborious process
so laborious that we would rather assign the task to a machine.

NLTK provides built-in support for them. 
Let's use a FreqDist to find the 50 most frequent words of Moby Dick:

"""
freqDistri=FreqDist(text1)
print(freqDistri) # <FreqDist with 19317 samples and 260819 outcomes>
freqDistri.most_common(50)

freqDistri['whale']

freqDistri.plot(50,cumulative=50)
"""
When we first invoke FreqDist, we pass the name of the text as an argument .
 We can inspect the total number of words ("outcomes") 
 that have been counted up — 260,819 in the case of Moby Dick. 
 The expression  most_common(50) gives us a list of the 50 most frequently occurring types
 in the text
"""

freqDistri2=FreqDist(text2)
freqDistri2.most_common(50)
# Visulaizinng cumulative frequency plot for most cpmmon 50 words
freqDistri2.plot(50,cumulative=50)
"""    
Do any words produced in the text1' most common 50 words help us grasp the topic or genre of this text?
Only one word, whale, is slightly informative! 
It occurs over 900 times. 
The rest of the words tell us nothing about the text; they're just English "plumbing.
" What proportion of the text is taken up with such words? 
We can generate a cumulative frequency plot for these words, to produce the graph 
These 50 words account for nearly half the book!


If the frequent words don't help us, how about the words that occur once only, 
the so-called hapaxes? View them by  hapaxes() method. 
This list contains lexicographer, cetological, contraband, expostulations, and about 9,000 others. 
It seems that there are too many rare words,
and without seeing the context we probably can't guess 
what half of the hapaxes mean in any case! Since neither frequent nor infrequent words help, 
we need to try something else.
"""
freqDistri.hapaxes()

# Fine Grain Selection of words

"""
Next, let's look at the long words of a text; 
perhaps these will be more characteristic and informative. 
For this we adapt some notation from set theory. 
We would like to find the words from the vocabulary of the text that are more than
15 characters long. Let's call this property P, so that P(w) is true 
if and only if w is more than 15 characters long. 
Now we can express the words of interest using mathematical set notation as shown in (a).
This means 
"the set of all w such that w is an element of V (the vocabulary) and w has property P".


a.		{w | w ∈ V & P(w)}

b.		[w for w in V if p(w)]

"""

V=set(text1)
long_words=[w for w in V if len(w) > 15]
sorted(long_words)
# For each word w in the vocabulary V, we check whether len(w) is greater than 15; all other words will be ignored

V2=set(text2)
long_words1=[word for word in V2 if len(word) > 15]
sorted(long_words1)

# In text1 we found the words with length more than 15 character which are called hapaxes.
# These seems promising 

# Here are all words from the chat corpus that are longer than seven characters, that occur more than seven times
frequencyDistribution=FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and frequencyDistribution[w] > 7  )

"""
Notice how we have used two conditions: len(w) > 7 ensures that the words are longer than seven letters, 
and fdist5[w] > 7 ensures that these words occur more than seven times. 
At last we have managed to automatically identify the frequently-occurring content-bearing words of the text. 
It is a modest but important milestone: a tiny piece of code, processing tens of thousands of words, produces some informative output.

"""
# Collocations of Bigrams

"""
A collocation is a sequence of words that occur together unusually often. 
Thus red wine is a collocation, whereas the wine is not. 
A characteristic of collocations is that they are resistant to substitution with words 
that have similar senses; for example, maroon wine sounds definitely odd.

To get a handle on collocations, we start off by extracting from a text a list of word pairs, 
also known as bigrams. This is easily accomplished with the function bigrams ()

"""

list(bigrams(['more','is','said','than','done']))

#[('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]

"""
Here we see that the pair of words than-done is a bigram, 
and we write it in Python as ('than', 'done'). 
Now, collocations are essentially just frequent bigrams, 
except that we want to pay more attention to the cases that involve rare words. 
In particular, we want to find bigrams that occur more often than we would expect 
based on the frequency of the individual words. 
The collocations() function does this for us. 
"""
text1.collocation_list(num=10)

# Counting other things

"""
Counting words is useful, but we can count other things too. 
For example, we can look at the distribution of word lengths in a text, 
by creating a FreqDist out of a long list of numbers, 
where each number is the length of the corresponding word in the text

"""
[len(w) for w in text1]

fdist=FreqDist(len(w) for w in text1)

print(fdist)

fdist.most_common()

# [(3, 50223),(1, 47933),(4, 42345),(2, 38513),(5, 26597),(6, 17111),(7, 14399),
#(8, 9966),(9, 6428),(10, 3528),(11, 1873),(12, 1053),(13, 567),(14, 177),(15, 70),
#(16, 22),(17, 12),(18, 1),(20, 1)]

fdist[3]
fdist.freq(3)
# So in the text1 more than 50000 words are to 3 character

#Functions Defined for NLTK's Frequency Distributions

"""
Example	                            Description

fdist = FreqDist(samples) :__	create a frequency distribution containing the given samples

fdist[sample] += 1	:__ increment the count for this sample

fdist['monstrous']	:__ count of the number of times a given sample occurred

fdist.freq('monstrous')	:__ frequency of a given sample

fdist.N()	:__ total number of samples

fdist.most_common(n) :__	the n most common samples and their frequencies

for sample in fdist: :__	iterate over the samples

fdist.max()	 :__ sample with the greatest count

fdist.tabulate() :__ 	tabulate the frequency distribution

fdist.plot() :__	 graphical plot of the frequency distribution

fdist.plot(cumulative=True)	:__  cumulative plot of the frequency distribution

fdist1 |= fdist2	:__ update fdist1 with counts from fdist2

fdist1 < fdist2	:__ test if samples in fdist1 occur less frequently than in fdist2


"""

# Some word Comparison Function

"""
Function	                    Meaning


s.startswith(t)	test if s starts with t
s.endswith(t)	test if s ends with t
t in s	        test if t is a substring of s
s.islower()	test if s contains cased characters and all are lowercase
s.isupper()	test if s contains cased characters and all are uppercase
s.isalpha()	test if s is non-empty and all characters in s are alphabetic
s.isalnum()	test if s is non-empty and all characters in s are alphanumeric
s.isdigit()	test if s is non-empty and all characters in s are digits
s.istitle()	test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)

"""
sorted(w for  w in set(text1)if w.endswith('ableness'))

sorted(w for w in set(text4) if 'gnt' in w)

sorted(w for w in set(text6) if w.istitle())

sorted(d  for d in set(text7) if d.isdigit())
                                                                                                                                

"""
We can also create more complex conditions. 
If c is a condition, then not c is also a condition.
If we have two conditions c1 and c2, then we can combine them to form a new condition 
using conjunction and disjunction: c1 and c2, c1 or c2.

"""
# This is used to the check the words with - and index keywords 
sorted(w for w in set(text7) if '-' in w and 'index' in w )
#['Stock-index','index-arbitrage','index-fund','index-options','index-related','stock-index']


# Word with title and length is more than 10

sorted(i for i in set(text3) if i.istitle()and len(i) > 10)

#['Abelmizraim','Allonbachuth','Beerlahairoi','Canaanitish','Chedorlaomer','Girgashites','Hazarmaveth','Hazezontamar','Ishmeelites','Jegarsahadutha','Jehovahjireh','Kirjatharba','Melchizedek','Mesopotamia','Peradventure','Philistines','Zaphnathpaaneah']

sorted( i for i in set(sent7) if  not  i.islower())
# [',', '.', '29', '61', 'Nov.', 'Pierre', 'Vinken']

# displaying the words with contains either the string 'cie' or 'cei'
sorted(w for w in set(text2) if 'cie' in w or 'cei' in w)

# Operating on every element
[len(w)for w in text1]
[w.upper() for w in text1]

"""
These expressions have the form [f(w) for ...] or [w.f() for ...], 
where f is a function that operates on a word to compute its length, or to convert it to uppercase. 
For now, you don't need to understand the difference between the notations f(w) and w.f(). 
Instead, simply learn this Python idiom which performs the same operation on every element 
of a list. In the preceding examples, it goes through each word in text1, 
assigning each one in turn to the variable w and performing 
the specified operation on the variable.

"""



# Let's return to the question of vocabulary size, and apply the same idiom here:

len(text1) #260819
len(set(text1)) #19317
len(set(word.lower()for word in text1)) #17231 (2000 words removed )

"""
Now that we are not double-counting words like This and this, 
which differ only in capitalization, 
we've wiped 2,000 off the vocabulary count! 
We can go a step further and eliminate numbers and punctuation from the vocabulary 
count by filtering out any non-alphabetic items:

"""
len( set(word.lower() for word in text1 if word.isalpha()))  #16948



   




"""
Summary
Texts are represented in Python using lists: ['Monty', 'Python']. We can use indexing, slicing, and the len() function on lists.
A word "token" is a particular appearance of a given word in a text; a word "type" is the unique form of the word as a particular sequence of letters. We count word tokens using len(text) and word types using len(set(text)).
We obtain the vocabulary of a text t using sorted(set(t)).
We operate on each item of a text using [f(x) for x in text].
To derive the vocabulary, collapsing case distinctions and ignoring punctuation, we can write set(w.lower() for w in text if w.isalpha()).
We process each word in a text using a for statement, such as for w in t: or for word in text:. This must be followed by the colon character and an indented block of code, to be executed each time through the loop.
We test a condition using an if statement: if len(word) < 5:. This must be followed by the colon character and an indented block of code, to be executed only if the condition is true.
A frequency distribution is a collection of items along with their frequency counts (e.g., the words of a text and their frequency of appearance).
A function is a block of code that has been assigned a name and can be reused. Functions are defined using the def keyword, as in def mult(x, y); x and y are parameters of the function, and act as placeholders for actual data values.
A function is called by specifying its name followed by zero or more arguments inside parentheses, like this: texts(), mult(3, 4), len(text1).

"""









































































































































































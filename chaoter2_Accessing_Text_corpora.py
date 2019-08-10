#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:36:38 2019

@author: singhgagan
# Accessing Text Corpora and Lexical Resources
# Source: NLTK book chapter2

Practical work in Natural Language Processing typically uses large bodies of linguistic data, or corpora. The goal of this chapter is to answer the following questions:

What are some useful text corpora and lexical resources, and how can we access them with Python?
Which Python constructs are most helpful for this work?
How do we avoid repeating ourselves when writing Python code?
"""

# A text corpora is large body of text
# Accessing the text corpora
"""
Gutenberg Corpus
NLTK includes a small selection of texts from the Project Gutenberg electronic text archive, 
which contains some 25,000 free electronic books, hosted at http://www.gutenberg.org/. 
We begin by getting the Python interpreter to load the NLTK package, 
then ask to see nltk.corpus.gutenberg.fileids(), the file identifiers in this corpus
"""
from nltk.book import *
import nltk
nltk.corpus.gutenberg.fileids()

"""
The gutenberg corpus contains the following 18 fileids
['austen-emma.txt','austen-persuasion.txt','austen-sense.txt','bible-kjv.txt','blake-poems.txt',
 'bryant-stories.txt','burgess-busterbrown.txt','carroll-alice.txt','chesterton-ball.txt',
 'chesterton-brown.txt','chesterton-thursday.txt','edgeworth-parents.txt',
 'melville-moby_dick.txt','milton-paradise.txt','shakespeare-caesar.txt',
 'shakespeare-hamlet.txt','shakespeare-macbeth.txt','whitman-leaves.txt']

"""
#Let's pick out the first of these texts — Emma by Jane Austen — 
# and give it a short name, emma, then find out how many words it contains:

emma=nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma) # 192427
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance('surprize')

"""
When we defined emma, we invoked the words() function of the gutenberg object in NLTK's corpus package. But since it is cumbersome to type such long names all the time,
Python provides another version of the import statement, as follows:
"""
from nltk.corpus import gutenberg
gutenberg.fileids()

for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid))
    num_words=len(gutenberg.words(fileid))
    num_sents=len(gutenberg.sents(fileid))
    num_vocab=len(set(w.lower() for w in gutenberg.words(fileid )))
    print(round(num_chars/num_words), round(num_words/num_sents),round(num_words/num_vocab),fileid)

"""
This program displays three statistics for each text: 
1.average word length, 
2.average sentence length, 
3.The number of times each vocabulary item appears in the text on average(our lexical diversity score).
Observe that average word length appears to be a general property of English, 
since it has a recurrent value of 4. 
(In fact, the average word length is really 3 not 4, since the num_chars variable counts spacecharacters.) 
By contrast average sentence length and lexical diversity appear to be characteristics of particular authors.


The previous example also showed how we can access the "raw" text of the book [1], not split up into tokens. 
The raw() function gives us the contents of the file without any linguistic processing. 
So, for example,  len(gutenberg.raw('blake-poems.txt')) tells us 
how many letters occur in the text, including the spaces between words. 
The sents() function divides the text up into its sentences, where each sentence is a list of words:

"""


macbeth_sentences=gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences
macbeth_sentences[1116]
longest_len=max(len(s) for s in macbeth_sentences)
[s for s in macbeth_sentences if len(s)==longest_len]

"""
Note

Most NLTK corpus readers include a variety of access methods 
apart from words(), raw(), and sents(). 
Richer linguistic content is available from some corpora, such as part-of-speech tags, 
dialogue tags, syntactic trees, and so forth; we will see these in later chapters.

"""


# Web and Chat Text
"""
Although Project Gutenberg contains thousands of books, it represents established literature. 
It is important to consider less formal language as well. 
NLTK's small collection of web text includes content from a 
Firefox discussion forum, 
conversations overheard in New York, 
the movie script of Pirates of the Carribean, 
personal advertisements, 
and wine reviews:
"""

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65],'...')


"""
There is also a corpus of instant messaging chat sessions, 
originally collected by the Naval Postgraduate School for research 
on automatic detection of Internet predators. 
The corpus contains over 10,000 posts, anonymized by replacing usernames with generic names of
the form "UserNNN", and manually edited to remove any other identifying information. 
The corpus is organized into 15 files, where each file contains several hundred posts 
collected on a given date, 
for an age-specific chatroom (teens, 20s, 30s, 40s, plus a generic adults chatroom). 
The filename contains the date, chatroom, 
and number of posts; e.g., 10-19-20s_706posts.xml contains 706 posts gathered
 from the 20s chat room on 10/19/2006.
"""

from nltk.corpus import nps_chat
chatroom=nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]


# ********************* Starting Brown Corpus **************************#


"""
The Brown Corpus was the first million-word electronic corpus of English, 
created in 1961 at Brown University. 
This corpus contains text from 500 sources, and the sources have been categorized by genre, 
such as news, editorial, and so on. 
1.1 gives an example of each genre 
(for a complete list, see http://icame.uib.no/brown/bcm-los.html).

"""
# Example Document for Each Section of the Brown Corpus
"""
ID	File	Genre	      Description
A16	ca16	news	      Chicago Tribune: Society Reportage
B02	cb02	editorial	  Christian Science Monitor: Editorials
C17	cc17	reviews	      Time Magazine: Reviews
D12	cd12	religion	  Underwood: Probing the Ethics of Realtors
E36	ce36	hobbies	      Norling: Renting a Car in Europe
F25	cf25	lore	      Boroff: Jewish Teenage Culture
G22	cg22	belles_lettres	Reiner: Coping with Runaway Technology
H15	ch15	government	  US Office of Civil and Defence Mobilization: The Family Fallout Shelter
J17	cj19	learned	      Mosteller: Probability with Statistical Applications
K04	ck04	fiction	      W.E.B. Du Bois: Worlds of Color
L13	cl13	mystery	      Hitchens: Footsteps in the Night
M01	cm01	science_fiction	Heinlein: Stranger in a Strange Land
N14	cn15	adventure	  Field: Rattlesnake Ridge
P12	cp12	romance	      Callaghan: A Passion in Rome
R06	cr06	humor	      Thurber: The Future, If Any, of Comedy

We can access the corpus as a list of words, or a list of sentences
 (where each sentence is itself just a list of words). 
 We can optionally specify particular categories or files to read:

"""
from nltk.corpus import brown

brown.categories()
# ['adventure','belles_lettres','editorial','fiction','government','hobbies','humor','learned','lore','mystery','news','religion','reviews','romance','science_fiction']

brown.words(categories='news') #  ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]

brown.words(fileids=['cg22']) # ['Does', 'our', 'society', 'have', 'a', 'runaway', ',', ...]

brown.words(fileids=['cp12']) # ['``', 'I', 'had', 'a', 'rather', 'small', 'place', ...]

brown.sents(categories=['news','editorial','reviews'])

"""
The Brown Corpus is a convenient resource for studying systematic differences between genres, 
a kind of linguistic inquiry known as stylistics. 
Let's compare genres in their usage of modal verbs. 
The first step is to produce the counts for a particular genre.
"""
import nltk
news_text=brown.words(categories='news')
frequency_Distribution=nltk.FreqDist(w.lower() for w in news_text)
modals=['can','could','may','might','will','must']
for m in modals:
    print(m + ':', frequency_Distribution[m], end='') # We need to include end=' ' in order for the print function to put its output on a single line.

# can: 94could: 87may: 93might: 38will: 389must: 53

reviews_text=brown.words(categories='reviews')
freDis=nltk.FreqDist(w.lower() for w in reviews_text)
model_review=['what','when','where','who','why']
for m in model_review:
    print(m+':',freDis[m], end='')

# what: 56when: 60where: 29who: 130why: 9

"""
we need to obtain counts for each genre of interest. 
We'll use NLTK's support for conditional frequency distributions
"""
cfd=nltk.ConditionalFreqDist((genre,words)
                            for genre in brown.categories()
                            for words in brown.words(categories=genre))
genres=['news','hobbies','religion','science_fiction','romance','humor']
models=['can','could','may','might','must','will']
cfd.tabulate(conditions=genres,samples=models)

"""
Observe that the most frequent modal in the news genre is will,
while the most frequent modal in the romance genre is could. 
Would you have predicted this? The idea that word counts might distinguish genres
will be taken up again in chap-data-intensive.
"""
# ****************END of Brown Corpus **************************#


# **************** Strating of Reuters Corpus **************************#

"""
The Reuters Corpus contains 10,788 news documents totaling 1.3 million words. 
The documents have been classified into 90 topics, and grouped into two sets, 
called "training" and "test"; thus, 
the text with fileid 'test/14826' is a document drawn from the test set. 
This split is for training and testing algorithms that automatically detect 
the topic of a document, as we will see in chap-data-intensive.

"""
from nltk.corpus import reuters
reuters.categories() # ['acq', 'alum', 'barley', 'bop', 'carcass', 'castor-oil', 'cocoa','coconut', 'coconut-oil',...]

reuters.fileids() # ['test/14826', 'test/14828', 'test/14829', 'test/14832', ...]

"""
Unlike the Brown Corpus, categories in the Reuters corpus overlap with each other, 
simply because a news story often covers multiple topics.
We can ask for the topics covered by one or more documents, 
or for the documents included in one or more categories. 
For convenience, the corpus methods accept a single fileid or a list of fileids.
"""
reuters.categories('training/9865') # ['barley', 'corn', 'grain', 'wheat']

reuters.categories('training/9880') # ['money-fx']

reuters.categories((['training/9865','training/9880'])) # ['barley', 'corn', 'grain', 'money-fx', 'wheat']

reuters.fileids('barley') #['test/15618','test/15649','test/15676','test/15728','test/15871','test/15875','test/15952','test/17767','test/17769', ...]

reuters.fileids((['barley','corn'])) 
"""
Similarly, we can specify the words or sentences we want in terms of files or categories. 
The first handful of words in each of these texts are the titles, 
which by convention are stored as upper case.

"""
reuters.words('training/2172')[:14] #['FRENCH','CEREAL','EXPORTS','THROUGH','ROUEN','FALL','French','cereal','exports','through','the','port','of','Rouen']

reuters.words(['training/8004','training/8759']) # ['U', '.', 'S', '.', 'SUGAR', 'PROGRAM', 'CUT', 'SENT', ...]


reuters.words(categories='barley') # ['FRENCH', 'FREE', 'MARKET', 'CEREAL', 'EXPORT', ...]

reuters.words(categories=['barley','corn']) # ['THAI', 'TRADE', 'DEFICIT', 'WIDENS', 'IN', 'FIRST', ...]

# ****************END of Reuters Corpus **************************#


# **************** Starting of Inaugural Address  Corpus **************************#

"""
we looked at the Inaugural Address Corpus, but treated it as a single text. 
The graph in fig-inaugural used "word offset" as one of the axes;
this is the numerical index of the word in the corpus, 
counting from the first word of the first address. However, 
the corpus is actually a collection of 55 texts, one for each presidential address. 
An interesting property of this collection is its time dimension:

"""

from nltk.corpus import inaugural
inaugural.fileids() # ['1789-Washington.txt','1793-Washington.txt','1797-Adams.txt','1801-Jefferson.txt','1805-Jefferson.txt','1809-Madison.txt','1813-Madison.txt','1817-Monroe.txt','1821-Monroe.txt',...]

[fileid[:4] for fileid in inaugural.fileids()] # ['1789','1793','1797','1801','1805','1809','1813','1817','1821','1825','1829',...]

"""
Notice that the year of each text appears in its filename. 
To get the year out of the filename, we extracted the first four characters, using fileid[:4].

Let's look at how the words America and citizen are used over time. 
The following code converts the words in the Inaugural corpus to lowercase using w.lower()
then checks if they start with either of the "targets" america or citizen using startswith() 
Thus it will count words like American's and Citizens
"""
import nltk
cfd=nltk.ConditionalFreqDist(
        (target,fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in['america','citizen']
        if w.lower().startswith(target))

cfd.plot() # Plot of a Conditional Frequency Distribution: all words in the Inaugural Address Corpus that begin with america or citizen are counted; separate counts are kept for each address; these are plotted so that trends in usage over time can be observed; counts are not normalized for document length.


# **************** End of Inaugural Address  Corpus **************************#


# **************** Starting of Annotated Text Corpus **************************#

"""
Many text corpora contain linguistic annotations, representing POS tags, named entities, 
syntactic structures, semantic roles, and so forth.
NLTK provides convenient ways to access several of these corpora, 
and has data packages containing corpora and corpus samples, freely downloadable 
for use in teaching and research. 1.2 lists some of the corpora. 
For information about downloading them, see http://nltk.org/data. 
For more examples of how to access NLTK corpora, 
please consult the Corpus HOWTO at http://nltk.org/howto.
"""



# **************** End of Annotated Text Corpus **************************#


# **************** Starting Corpora in Another languages **************************#
"""
NLTK comes with corpora for many languages, though in some cases you will need to learn 
how to manipulate character encodings in Python before using these corpora
"""
nltk.corpus.cess_esp.words() # ['El', 'grupo', 'estatal', 'Electricité_de_France', ...]

nltk.corpus.floresta.words() # ['Um', 'revivalismo', 'refrescante', 'O', '7_e_Meio', ...]

nltk.corpus.indian.words('hindi.pos') #  ['पूर्ण', 'प्रतिबंध', 'हटाओ', ':', 'इराक', 'संयुक्त', ...]

nltk.corpus.udhr.fileids() # ['Abkhaz-Cyrillic+Abkh','Abkhaz-UTF8','Achehnese-Latin1','Achuar-Shiwiar-Latin1','Adja-UTF8','Afaan_Oromo_Oromiffa-Latin1','Afrikaans-Latin1','Aguaruna-Latin1','Akuapem_Twi-UTF8',...]

nltk.corpus.udhr.words('Javanese-Latin1')[11:] # ['Saben', 'umat', 'manungsa', 'lair', 'kanthi', 'hak', ...]

"""
The last of these corpora, udhr, contains the 
Universal Declaration of Human Rights in over 300 languages. 
The fileids for this corpus include information about 
the character encoding used in the file,such as UTF8 or Latin1. 
 Let's use a conditional frequency distribution to examine 
 the differences in word lengths for a selection of languages included in the udhr corpus
"""

from nltk.corpus import udhr
languages=['Chickasaw','English','German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

cfd2=nltk.ConditionalFreqDist(
        (lang,len(word))
        for lang in languages
        for word in udhr.words(lang+'-Latin1'))
cfd2.plot(cumulative=True)

"""
Cumulative Word Length Distributions: Six translations of the Universal Declaration 
of Human Rights are processed; this graph shows that words having 5 or fewer letters account 
for about 80% of Ibibio text, 60% of German text, and 25% of Inuktitut text.
"""

"""
Unfortunately, for many languages, substantial corpora are not yet available. 
Often there is insufficient government or industrial support for developing language resources,
and individual efforts are piecemeal and hard to discover or re-use. 
Some languages have no established writing system, or are endangered.
"""

# **************** End Corpora in Another languages **************************#

# **************** Text Corpus Structure *************************************#
"""
We have seen a variety of corpus structures so far.
The simplest kind lacks any structure: it is just a collection of texts.
Often, texts are grouped into categories that might correspond to genre, source, author, language, etc. 
Sometimes these categories overlap, notably in the case of topical categories
as a text can be relevant to more than one topic. 
Occasionally, text collections have temporal structure, 
news collections being the most common example.

Common Structures for Text Corpora: 
The simplest kind of corpus is a collection of isolated texts with no particular organization;
some corpora are structured into categories like genre (Brown Corpus); 
some categorizations overlap, such as topic categories (Reuters Corpus); 
other corpora represent language use over time (Inaugural Address Corpus).

Basic Corpus Functionality defined in NLTK: 
    more documentation can be found using help(nltk.corpus.reader) and by reading the online Corpus HOWTO at http://nltk.org/howto.
**********************************************************************************************
                             Table 1.3 
                             
Example	                                Description

fileids()	                 the files of the corpus

fileids([categories])	     the files of the corpus corresponding to these categories

categories()	             the categories of the corpus

categories([fileids])	     the categories of the corpus corresponding to these files

raw()	                     the raw content of the corpus

raw(fileids=[f1,f2,f3])	     the raw content of the specified files

raw(categories=[c1,c2])	     the raw content of the specified categories

words()	                     the words of the whole corpus

words(fileids=[f1,f2,f3])	 the words of the specified fileids

words(categories=[c1,c2])	 the words of the specified categories
sents()	the sentences of     the whole corpus

sents(fileids=[f1,f2,f3])	 the sentences of the specified fileids

sents(categories=[c1,c2])	 the sentences of the specified categories

abspath(fileid)	             the location of the given file on disk

encoding(fileid)	         the encoding of the file (if known)

open(fileid)	             open a stream for reading the given corpus file

root	                     if the path to the root of locally installed corpus

readme()	                 the contents of the README file of the corpus

*******************************************************************************************
NLTK's corpus readers support efficient access to a variety of corpora, 
and can be used to work with new corpora. 
1.3 lists functionality provided by the corpus readers. 
We illustrate the difference between some of the corpus access methods below
"""
import nltk
from nltk.corpus import gutenberg
raw=gutenberg.raw("burgess-busterbrown.txt")
raw[1:20] # 'The Adventures of B'
words=gutenberg.words("burgess-busterbrown.txt")
words[1:20] # ['The','Adventures','of','Buster','Bear','by','Thornton','W','.','Burgess','1920',']','I','BUSTER','BEAR','GOES','FISHING','Buster','Bear']

sents=gutenberg.sents("burgess-busterbrown.txt")
sents[1:20]

"""
[['I'], ['BUSTER', 'BEAR', 'GOES', 'FISHING'], ['Buster', 'Bear', 'yawned', 'as',
'he', 'lay', 'on', 'his', 'comfortable', 'bed', 'of', 'leaves', 'and', 'watched',
'the', 'first', 'early', 'morning', 'sunbeams', 'creeping', 'through', ...], ...]
"""

# **************** End Text Corpus Structure *************************************#



# *************** Loading your own Corpus ****************************************#
"""
If you have your own collection of text files that you would like to access 
using the above methods, you can easily load them with the help of NLTK's PlaintextCorpusReader. 

 
"""
from nltk.corpus import PlaintextCorpusReader
corpus_root='/home/singhgagan/Gagan/Images'
word_list=PlaintextCorpusReader(corpus_root,'.*')
word_list.fileids()
word_list.words()

"""
As another example, suppose you have your own local copy of Penn Treebank (release 3), in C:\corpora. We can use the BracketParseCorpusReader to access this corpus. We specify the corpus_root to be the location of the parsed Wall Street Journal component of the corpus [1], and give a file_pattern that matches the files contained within its subfolders [2] (using forward slashes).
"""
# *********************************SECTION 1 Completed*************************************#

# *********************************SECTION 2 STARTED**************************************#
# Conditional Frequency Distributions
"""
We saw that given some list mylist of words or other items, FreqDist(mylist) would compute the
number of occurrences of each item in the list. Here we will generalize this idea.

When the texts of a corpus are divided into several categories, by genre, topic, author, etc,
we can maintain separate frequency distributions for each category. 
This will allow us to study systematic differences between the categories. 
In the previous section we achieved this using NLTK's ConditionalFreqDist data type. 
A conditional frequency distribution is a collection of frequency distributions,
each one for a different "condition". The condition will often be the category of the text.
2.1 depicts a fragment of a conditional frequency distribution having just two conditions, 
one for news text and one for romance text.
"""

#************ 2.1 Condition and Events Starts ********************************************

"""
A frequency distribution counts observable events, such as the appearance of words in a text. 
A conditional frequency distribution needs to pair each event with a condition. 
So instead of processing a sequence of words [1], we have to process a sequence of pairs [2]:

"""
text=['The','Fulton','County','Grand','Jury','said'] #1
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...] 

"""
Each pair has the form (condition, event). 
If we were processing the entire Brown Corpus by genre there would be 15 conditions
 (one per genre), and 1,161,192 events (one per word).
"""
#****************** 2.1 Condition and Events Ends ********************************************

#****************** 2.2 Counting words by Genre **********************************************

from nltk.corpus import brown
cfd=nltk.ConditionalFreqDist(
        (genre,word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
"""
# Let's break this down, and look at just two genres, news and romance. 
For each genre [2], we loop over every word in the genre [3], 
producing pairs consisting of the genre and the word [1]:

"""

genre_word=[(genre,word)
for genre in ['news','romance']
for word in brown.words(categories=genre)]
len(genre_word) #170576

 
# So, as we can see below, pairs at the beginning of the list genre_word will be of the form ('news', word)
genre_word[:4]  # [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ('news', 'Grand')]

# while those at the end will be of the form ('romance', word)
genre_word[-4:] # [('romance', 'afraid'),('romance', 'not'),('romance', "''"),('romance', '.')]



 # We can now use this list of pairs to create a ConditionalFreqDist, 
# and save it in a variable cfd. As usual, we can type the name of the variable to inspect it 

cfd=nltk.ConditionalFreqDist(genre_word)
cfd  # <ConditionalFreqDist with 2 conditions>
cfd.conditions() # ['news', 'romance']
cfd.items() # dict_items([('news', FreqDist({'the': 5580, ',': 5188, '.': 4030, 'of': 2849, 'and': 2146, 'to': 2116, 'a': 1993, 'in': 1893, 'for': 943, 'The': 806, ...})), ('romance', FreqDist({',': 3899, '.': 3736, 'the': 2758, 'and': 1776, 'to': 1502, 'a': 1335, 'of': 1186, '``': 1045, "''": 1044, 'was': 993, ...}))])

# Let's access the two conditions, and satisfy ourselves that each is just a frequency distribution:
print(cfd['news']) # <FreqDist with 14394 samples and 100554 outcomes>
print(cfd['romance']) # <FreqDist with 8452 samples and 70022 outcomes>
cfd['romance'].most_common(20) 
"""
[(',', 3899),('.', 3736),('the', 2758),('and', 1776),('to', 1502),('a', 1335),('of', 1186),
 ('``', 1045),("''", 1044),('was', 993),('I', 951),('in', 875),('he', 702),('had', 692),
 ('?', 690),('her', 651),('that', 583),('it', 573),('his', 559),('she', 496)]
"""
cfd['romance']['could'] #  193

#**********End of Section 2.2 Counting words by Genre *************************************#



#******************Starting Section 2.3 Plotting and Tabulating Distribution**************#

"""
Apart from combining two or more frequency distributions, and being easy to initialize, 
a ConditionalFreqDist provides some useful methods for tabulation and plotting.

The plot in 1.1 was based on a conditional frequency distribution reproduced in the code below.
The condition is either of the words america or citizen [2],
 and the counts being plotted are the number of times the word occured in a particular speech. It exploits the fact that the filename for each speech, e.g., 1865-Lincoln.txt contains the year as the first four characters [1]. This code generates the pair ('america', '1865') for every instance of a word whose lowercased form starts with america — such as Americans — in the file 1865-Lincoln.txt.

"""
from nltk.corpus import inaugural
cfd_inagural=nltk.ConditionalFreqDist(
        (target,fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america','citizen'] 
        if w.lower().startswith(target))

cfd_inagural.plot(cumulative=True) # Plot 1.1

"""
The plot in 1.2 was also based on a conditional frequency distribution, reproduced below. 
This time, the condition is the name of the language and the counts being plotted are derived
 from word lengths [1]. It exploits the fact that the filename for each language 
 is the language name followed by '-Latin1' (the character encoding).
"""


from nltk.corpus import udhr
languages=['Chickasaw', 'English', 'German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

cfd_lang=nltk.ConditionalFreqDist(
        (lang,len(word))
        for lang in languages
        for word in udhr.words(lang+'-Latin1')
        )

cfd_lang.plot(cumulative=True) # plot 1.2



"""
In the plot() and tabulate() methods, we can optionally specify which conditions to display 
with a conditions= parameter. When we omit it, we get all the conditions. 
Similarly, we can limit the samples to display with a  samples= parameter. 
This makes it possible to load a large quantity of data into a conditional frequency distribution, 
and then to explore it by plotting or tabulating selected conditions and samples. 
It also gives us full control over the order of conditions and samples in any displays. 
For example, we can tabulate the cumulative frequency data just for two languages, and for words
less than 10 characters long, as shown below. We interpret the last cell on the top row to mean
that 1,638 words of the English text have 9 or fewer letters.

"""
#************** I am getting difficulties in obtaining acurate results
from nltk.corpus import brown
#cfd_brown=nltk.ConditionalFreqDist()
#brown.categories()[13]
brown.words(categories='news')

week=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

temp_brown=nltk.ConditionalFreqDist(
        (w,cat)
        for w in week
        for cat in brown.categories())
        #for genre in brown.categories() )


temp_brown.tabulate(cumulative=True,Sample=week)

temp_brown.tabulate(cumulative=True)


temp_brown.plot(cumulative=True,sample=week)

#************** I am getting difficulties in obtaining acurate results

#*************** 2.3 End of plotting and tabulating Distribution **********************************************



#**********************2.4 Starting Generating Random text with bigram*****************************************

"""
We can use a conditional frequency distribution to create a table of bigrams (word pairs).
(We introducted bigrams in 3.) The bigrams() function takes a list of words 
and builds a list of consecutive word pairs. 
Remember that, in order to see the result and not a cryptic "generator object", we need to use 
the list() function:
"""
sent=['in', 'the' ,'beginning', 'god' ,'created ','the' ,'heaven' ,'and' ,'then' ,'earth']

list(nltk.bigrams(sent))

"""
In 2.2, we treat each word as a condition, and for each one we effectively create a frequency distribution over
the following words. The function generate_model() contains a simple loop to generate text.
When we call the function, we choose a word (such as 'living') as our initial context, then once inside the loop,
we print the current value of the variable word, and reset word to be the most likely token in that context 
(using max()); next time through the loop, we use that word as our new context. 
As you can see by inspecting the output, this simple approach to text generation tends to get stuck in loops; 
another method would be to randomly choose the next word from among the available words.
"""

def generate_model(cfdist,word,num=15):
    for i in range(num):
        print(word, end='')
        word=cfdist[word].max()

text=nltk.corpus.genesis.words('english-kjv.txt')
bigrams=nltk.bigrams(text)
cfd=nltk.ConditionalFreqDist(bigrams)

cfd['living']

"""
Generating Random Text: this program obtains all bigrams from the text of the book of Genesis, then constructs a conditional frequency distribution to record which words are most likely to follow a given word; e.g., after the word living, the most likely word is creature; the generate_model() function uses this data, and a seed word, to generate random text.

Conditional frequency distributions are a useful data structure for many NLP tasks. Their commonly-used methods are summarized in 2.1.

"""
#**************Table 2.1*************************************************
"""
NLTK's Conditional Frequency Distributions: commonly-used methods and idioms for defining, accessing, and visualizing a conditional frequency distribution of counters.

Example	Description
cfdist = ConditionalFreqDist(pairs)	create a conditional frequency distribution from a list of pairs
cfdist.conditions()	the conditions
cfdist[condition]	the frequency distribution for this condition
cfdist[condition][sample]	frequency for the given sample for this condition
cfdist.tabulate()	tabulate the conditional frequency distribution
cfdist.tabulate(samples, conditions)	tabulation limited to the specified samples and conditions
cfdist.plot()	graphical plot of the conditional frequency distribution
cfdist.plot(samples, conditions)	graphical plot limited to the specified samples and conditions
cfdist1 < cfdist2	test if samples in cfdist1 occur less frequently than in  cfdist2

"""
#**************Table 2.1*************************************************
 

#******** End Section 2.4 Generating Random Text with bigram**************


 
#**************Section 3 is Python Function and I am skipping this***********

#**************Section 4 Lexical Resources Started*********************************************#

"""
A lexicon, or lexical resource, is a collection of words and/or phrases along with associated 
information such as part of speech and sense definitions. 
Lexical resources are secondary to texts, and are usually created and enriched with the help of
texts. For example, if we have defined a text my_text, 
then vocab = sorted(set(my_text)) builds the vocabulary of my_text, 
while word_freq = FreqDist(my_text) counts the frequency of each word in the text. 
Both of vocab and word_freq are simple lexical resources. 
Similarly, a concordance like the one we saw in 1 gives us information about word usage 
that might help in the preparation of a dictionary. 
Standard terminology for lexicons is illustrated in 4.1.

A lexical entry consists of a headword (also known as a lemma) along with additional information
such as the part of speech and the sense definition. Two distinct words having the same spelling
are called homonyms.

The simplest kind of lexicon is nothing more than a sorted list of words. 
Sophisticated lexicons include complex structure within and across the individual entries. 
In this section we'll look at some lexical resources included with NLTK.

"""
#**************Section 4.1 Wordlist Corpora *********************************************#

"""
NLTK includes some corpora that are nothing more than wordlists.
The Words Corpus is the /usr/share/dict/words file from Unix, used by some spell checkers. 
We can use it to find unusual or mis-spelt words in a text corpus, as shown in 4.2.
"""
import nltk
def unusual_words(text):
    text_vocab= set(w.lower() for w in text if w.isalpha())
    english_vocab=set(w.lower() for w in nltk.corpus.words.words())
    unusual=text_vocab-english_vocab
    return(sorted(unusual))
    
unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))

unusual_words(nltk.corpus.nps_chat.words())
 


"""
There is also a corpus of stopwords, that is, high-frequency words
 like the, to and also that 
 we sometimes want to filter out of a document before further processing. 
Stopwords usually have little lexical content, and their presence in a text fails to distinguish
 it from other texts.

"""

from nltk.corpus import stopwords
stopwords.words('french') # ['au','aux','avec','ce','ces','dans','de','des','du','elle','en','et','eux','il','ils','je','la','le','les',...]


# Let's define a function to compute what fraction of words in a text are not in the stopwords list:

def content_fraction(text):
    stopwords=nltk.corpus.stopwords.words('english')
    content=[w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)

content_fraction(nltk.corpus.reuters.words()) # 0.735240435097661

#Thus, with the help of stopwords we filter out over a quarter of the words of the text.
# Notice that we've combined two different kinds of corpus here, *
#using a lexical resource to filter the content of a text corpus.


"""
***************************************************************************************
Word Puzzle: a grid of randomly chosen letters with rules for creating words out of the letters; 
this puzzle is known as "Target."

How many words of four letters and more can you make from the E G I V R V O N L
Each letter may be used once per word
Each word contain the center letter R 
There must be a 9 letter word
No Plurals like ending "s", no proper names no forign words
***************************************************************************************
A wordlist is useful for solving word puzzles, such as the one in 4.3. 
Our program iterates through every word and, for each one, checks whether 
it meets the conditions. It is easy to check obligatory letter [2] and 
length constraints [1] (and we'll only look for words with six or more letters here). 
It is trickier to check that candidate solutions only use combinations of the supplied letters,
especially since some of the supplied letters appear twice (here, the letter v). 
The FreqDist comparison method [3] permits us to check that the frequency of each letter 
in the candidate word is less than or equal to the frequency of the corresponding letter
in the puzzle.


"""
puzzle_letters=nltk.FreqDist('egivrvonl')
obligatory='r'
wordlist=nltk.corpus.words.words()
[w for w in wordlist if len(w)>=6 
 and obligatory in w 
 and nltk.FreqDist(w)<= puzzle_letters]
"""
['glover','gorlin','govern','grovel','ignore','involver','lienor','linger','longer',
'lovering','noiler','overling','region','renvoi','revolving','ringle','roving','violer','virole']
"""

"""
One more wordlist corpus is the Names corpus, containing 8,000 first names categorized by gender.
The male and female names are stored in separate files. 
Let's find names which appear in both files, i.e. names that are ambiguous for gender:

"""
names=nltk.corpus.names
names.fileids() # ['female.txt', 'male.txt']
male_names=names.words('male.txt')
female_names=names.words('female.txt')
[w for w in male_names if w in female_names] # There are 365 ambigous names for genders

"""
It is well known that names ending in the letter a are almost always female. 
We can see this and some other patterns in the graph in 4.4, produced by the following code. 
Remember that name[-1] is the last letter of name.

"""
cfd_names=nltk.ConditionalFreqDist(
        (fileid,name[-1])
        for fileid in names.fileids()
        for name in names.words(fileid))

cfd_names.plot()

"""
Conditional Frequency Distribution: this plot shows the number of female and male names ending 
with each letter of the alphabet; most names ending with a, e or i are female; 
names ending in h and l are equally likely to be male or female; 
names ending in k, o, r, s, and t are likely to be male.


"""

#********************End of Section 4.1 Wordlist Corpora****************************#

#******************* Starting section 4.2 Pronouncing Dictionary********************#

"""
A slightly richer kind of lexical resource is a table (or spreadsheet), 
containing a word plus some properties in each row. 
NLTK includes the CMU Pronouncing Dictionary for US English, which was designed for use by 
speech synthesizers.
""" 
entries=nltk.corpus.cmudict.entries()
len(entries) # 133737
for entry in entries[42371:42379]:
    print(entry)

"""
('fir', ['F', 'ER1'])
('fire', ['F', 'AY1', 'ER0'])
('fire', ['F', 'AY1', 'R'])
('firearm', ['F', 'AY1', 'ER0', 'AA2', 'R', 'M'])
('firearm', ['F', 'AY1', 'R', 'AA2', 'R', 'M'])
('firearms', ['F', 'AY1', 'ER0', 'AA2', 'R', 'M', 'Z'])
('firearms', ['F', 'AY1', 'R', 'AA2', 'R', 'M', 'Z'])
('fireball', ['F', 'AY1', 'ER0', 'B', 'AO2', 'L'])


For each word, this lexicon provides a list of phonetic codes — distinct labels for
each contrastive sound — known as phones. 
Observe that fire has two pronunciations (in US English): 
 the one-syllable F AY1 R, and the 
 two-syllable F AY1 ER0. 
 The symbols in the CMU Pronouncing Dictionary are from the Arpabet, 
 described in more detail at http://en.wikipedia.org/wiki/Arpabet
"""

"""
Each entry consists of two parts, and we can process these individually using a 
more complex version of the for statement. 
Instead of writing for entry in entries:, we replace entry with two variable names, 
word, pron [1]. Now, each time through the loop, word is assigned the first part of the entry, 
and pron is assigned the second part of the entry:

"""
for word,pron in entries:
    if len(pron)==3:
        ph1,ph2,ph3=pron
        if ph1 == 'P' and ph3=='T':
            print(word,ph2,end='')


"""
pait EY1pat AE1pate EY1patt AE1peart ER1peat IY1peet IY1peete IY1pert ER1pet EH1pete 
IY1pett EH1piet IY1piette IY1pit IH1pitt IH1pot AA1pote OW1pott AA1pout AW1puett UW1purt 
ER1put UH1putt AH1
"""
"""
The above program scans the lexicon looking for entries whose pronunciation consists of three
phones [2]. If the condition is true, it assigns the contents of pron to three new variables 
ph1, ph2 and ph3. Notice the unusual form of the statement which does that work [3].
"""

"""
Here's another example of the same for statement, this time used inside a list comprehension. 
This program finds all words whose pronunciation ends with a syllable sounding like nicks. 
You could use this method to find rhyming words
"""
syllable=['N','IH0','K','S']
[word for word, pron in entries if pron[-4:] == syllable]

"""
Notice that the one pronunciation is spelt in several ways: nics, niks, nix, even ntic's with 
a silent t, for the word atlantic's. Let's look for some other mismatches between pronunciation
and writing. Can you summarize the purpose of the following examples and explain how they work?
"""
[w for w, pron in entries if pron[-1]=='M'and w[-1]=='n']
# ['autumn', 'column', 'condemn', 'damn', 'goddamn', 'hymn', 'solemn']
sorted(set(w[:2]for w,pron in entries if pron[0]=='N'and w[0] !='n'))
#['gn', 'kn', 'mn', 'pn']
"""
The phones contain digits to represent primary stress (1), secondary stress (2) 
and no stress (0). As our final example, we define a function to extract the stress digits 
and then scan our lexicon to find words having a particular stress pattern.
"""
def stress(pron):
    return[char for phone in pron for char in phone if char.isdigit()]
[w for w, pron in entries if stress(pron)==['0','1','0','2','0']]
"""
'celebratory','coagulating','cogenerator','cogenerators','collaborated','collaborated',
 'collaborating','collaborative','collaborator','collaborators','collectivism','commemorated',
 'commemorating','commemorative','commercialism','commercializing','communicated','communicating',
 
"""

[w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']]



#['abbreviation', 'abbreviations','abomination','abortifacient','abortifacients',...]
 
# NOTE
"""

A subtlety of the above program is that our user-defined function stress() is invoked 
inside the condition of a list comprehension. There is also a doubly-nested for loop. 
There's a lot going on here and you might want to return to this once you've had 
more experience using list comprehensions.""

"""

"""
We can use a conditional frequency distribution to help us find minimally-contrasting sets of 
words. Here we find all the p-words consisting of three sounds [2], and group them according 
to their first and last sounds. 
"""

p3=[(pron[0]+ '-' +pron[2],word)
for(word,pron)in entries
if pron[0]=='P' and len(pron)==3]

cfd_pron=nltk.ConditionalFreqDist(p3)
for template in sorted(cfd_pron.conditions()):
    if len(cfd_pron[template]) > 10:
        words=sorted(cfd_pron[template])
        wordstring =' '.join(words)
        print(template,wordstring[:70] + "...")


"""
Rather than iterating over the whole dictionary, we can also access it by looking up particular
words. We will use Python's dictionary data structure, which we will study systematically in 3.
We look up a dictionary by giving its name followed by a key (such as the word 'fire')
inside square brackets [1].
"""
import nltk
pron_dict=nltk.corpus.cmudict.dict()
pron_dict['fire']
pron_dict['blog']=[['B','L','AAI','G']]
pron_dict['blog']

"""
If we try to look up a non-existent key [2], we get a KeyError. 
This is similar to what happens when we index a list with an integer that is too large, 
producing an IndexError. The word blog is missing from the pronouncing dictionary, 
so we tweak our version by assigning a value for this key [3] 
(this has no effect on the NLTK corpus; next time we access it, blog will still be absent).

"""


"""
We can use any lexical resource to process a text, e.g., to filter out words having some 
lexical property (like nouns), or mapping every word of the text. 
For example, the following text-to-speech function looks up each word of 
the text in the pronunciation dictionary.
"""

text=['natural','language','processing']
[ph for w in text for ph in pron_dict[w][0]]

#['N','AE1','CH','ER0','AH0', 'L','L','AE1','NG','G','W', 'AH0', 'JH','P','R','AA1','S','EH0','S','IH0','NG']

# ****************************END Section 4.2 A pronouncing Dictionary******************#


# **********Starting Section 4.3 Comparative Wordlist***********************************#
"""
Another example of a tabular lexicon is the comparative wordlist. 
NLTK includes so-called Swadesh wordlists, lists of about 200 common words in several languages.
The languages are identified using an ISO 639 two-letter code.
"""
from nltk.corpus import swadesh
swadesh.fileids() # ['be','bg','bs','ca','cs','cu','de','en','es','fr','hr','it','la','mk','nl','pl',pt','ro','ru','sk','sl','sr','sw','uk']

swadesh.words('en') # ['I', 'you (singular), thou','he', 'we', 'you (plural)','they', 'this', 'that', 'here',...]

"""
We can access cognate words from multiple languages using the entries() method,
specifying a list of languages. With one further step we can convert this into 
a simple dictionary (we'll learn about dict() in 3).
"""
fr2en=swadesh.entries(['fr','en']) # French-English
fr2en # [('je', 'I'),('tu, vous', 'you (singular), thou'),('il', 'he'),('nous', 'we'),('vous', 'you (plural)'),('ils, elles', 'they') ...]
translate=dict(fr2en)
translate['chien'] #  'dog'
translate['jeter'] # 'throw'

"""
We can make our simple translator more useful by adding other source languages. 
Let's get the German-English and Spanish-English pairs, convert each to a dictionary 
using dict(), then update our original translate dictionary with these additional mappings:

"""
de2en = swadesh.entries(['de','en']) # Geman -English
es2en = swadesh.entries(['es','en']) # Spanish- English
translate.update(dict(de2en))
translate.update(dict(es2en))

translate['Hund'] # 'dog'
translate['perro'] # 'dog'

# We can compare words in various Germanic and Romance languages:

languages=['en', 'de', 'nl', 'es', 'fr', 'pt', 'la']
for i in [139,140,141,142]:
    print(swadesh.entries(languages)[i])

"""
('say', 'sagen', 'zeggen', 'decir', 'dire', 'dizer', 'dicere')
('sing', 'singen', 'zingen', 'cantar', 'chanter', 'cantar', 'canere')
('play', 'spielen', 'spelen', 'jugar', 'jouer', 'jogar, brincar', 'ludere')
('float', 'schweben', 'zweven', 'flotar', 'flotter', 'flutuar, boiar', 'fluctuare')
"""

#*******************End of Section 4.3 Comparative Wordlist ******************************#

#*******************Starting of Section 4.4 Shoebox and toolbox lexicon*******************#

"""
Perhaps the single most popular tool used by linguists for managing data is Toolbox,
previously known as Shoebox since it replaces the field linguist's traditional shoebox 
full of file cards. Toolbox is freely downloadable from  http://www.sil.org/computing/toolbox/.

A Toolbox file consists of a collection of entries, where each entry is made up of one or more
fields. Most fields are optional or repeatable, which means that this kind of lexical resource
cannot be treated as a table or spreadsheet.

Here is a dictionary for the Rotokas language. We see just the first entry, for the word
kaa meaning "to gag":
"""
from nltk.corpus import toolbox
toolbox.entries('rotokas.dic') 
"""
[('kaa', [('ps', 'V'), ('pt', 'A'), ('ge', 'gag'), ('tkp', 'nek i pas'),
('dcsv', 'true'), ('vx', '1'), ('sc', '???'), ('dt', '29/Oct/2005'),
('ex', 'Apoka ira kaaroi aioa-ia reoreopaoro.'),
('xp', 'Kaikai i pas long nek bilong Apoka bikos em i kaikai na toktok.'),
('xe', 'Apoka is gagging from food while talking.')]), ...]
"""
"""
Entries consist of a series of attribute-value pairs, like ('ps', 'V') to indicate that 
the part-of-speech is 'V' (verb), and ('ge', 'gag') to indicate that the gloss-into-English 
is 'gag'. The last three pairs contain an example sentence in Rotokas and its translations 
into Tok Pisin and English.

The loose structure of Toolbox files makes it hard for us to do much more with them at this
stage. XML provides a powerful way to process this kind of corpus and we will return to this 
topic in 11..


"""

# Note
"""
The Rotokas language is spoken on the island of Bougainville, Papua New Guinea. 
This lexicon was contributed to NLTK by Stuart Robinson.
Rotokas is notable for having an inventory of just 12 phonemes (contrastive sounds), 
http://en.wikipedia.org/wiki/Rotokas_language
"""

#************End of Sction 4.4 Shoebox and toolboxLexicon*******************************#





































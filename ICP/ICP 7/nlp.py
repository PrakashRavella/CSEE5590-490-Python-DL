# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:00:42 2019

@author: chand
"""
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import nltk


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Google').read()
#print(text_from_html(html))
#print(text)
#
text = str(text_from_html(html).encode("utf-8")) 
text_file = open("input.txt", 'w') 
text_file.write(text) 
text_file.close()


# Question 3 

wtokens = nltk.word_tokenize(text)
for t in wtokens:
    print(t)

print(nltk.pos_tag(wtokens))

from nltk.stem import PorterStemmer

pStemmer = PorterStemmer()
print(pStemmer.stem('waiting'))   

from nltk.util import ngrams
trigram = ngrams(wtokens,3) 
for t in trigram:
    print(t)

from nltk import wordpunct_tokenize, pos_tag, ne_chunk
print(ne_chunk(pos_tag(wordpunct_tokenize(text))))



#Question 4





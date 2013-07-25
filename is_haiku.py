#!venv/bin/python

import nltk
from nltk.corpus import cmudict

dict = cmudict.dict()

def sy_count(word):
  word = word.lower()
  #there must be a better way to check if a char is a number
  syl_list = [list (punct for punct in pron if str(punct[-1]).isdigit()) 
    for pron in dict[word]]
  #need to get a better way to assess the syllable count, as in "best fit" for a sentence
  return len(syl_list[0]) 



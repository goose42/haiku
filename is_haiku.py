#!venv/bin/python

import nltk
from nltk.corpus import cmudict

dict = cmudict.dict()

def sy_count(word):
  word = word.lower()
  #there must be a better way to check if a char is a number
  sy_list_list = []
  for pron in dict[word]:
    last_char = ''
    sy_list = []
    for punct in pron:
      if str(punct[-1]).isdigit() or (len(last_char)==1 and len(punct)==1 and len(sy_list)!=0):
        sy_list.append(punct)
      last_char = punct
    sy_list_list.append(sy_list)
  #syl_list = [list (punct for punct in pron if str(punct[-1]).isdigit()) 
  #  for pron in dict[word]]
  
  
  #need to get a better way to assess the syllable count, 
  #as in "best fit" for a sentence
  return max([len(x) for x in sy_list_list])  

def is_haiku(sentence):
  #best to add something here to check if the sentence is english
  words = nltk.word_tokenize(sentence)
  syllables = 0
  for word in words:
    print word, sy_count(word)
    syllables += sy_count(word)
  print "Total syllables = " , syllables
  if syllables == 17:
    return True
  else:
    return False

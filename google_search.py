#!/usr/bin/env python 
from googlesearch import gsearch 

def search(query):

  # to search 
  #query = "郭文貴"

  string=''
  for j in gsearch(query, tld="com", num=10, stop=3,  pause=2): 
    print(j) 
    string = string + j + '\n'

  return string

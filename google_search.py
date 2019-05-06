#!/usr/bin/env python 

def search(query):
  try: 
	  from googlesearch import gsearch 
  except ImportError: 
	  print("No module named 'google' found") 

  # to search 
  #query = "郭文貴"

  string=''
  for j in gsearch(query, tld="com", num=10, stop=3,  pause=2): 
    print(j) 
    string = string + j + '\n'

  return string

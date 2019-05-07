#!/usr/bin/env python 
from googlesearch import search as gs 
import urllib.request as ur
from bs4 import BeautifulSoup

def search(query):

  print('query:',query)

  def google_scrape(url):
    thepage = ur.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

  i = 1
  strings = ''
  query = str(query)
  for url in gs(query, stop=5, tpe='nws'):
#   a = google_scrape(url)
#   strings = strings + str(i) + ". " + a + '\n'
    strings = strings + url + '\n'
    strings = strings + '\n' 
    i += 1

  return strings

if __name__ == '__main__':
  # to search 
  query = "基督教"

  content = search(query) 
  print(content)

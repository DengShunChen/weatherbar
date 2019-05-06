#!/usr/bin/env python 
from googlesearch import search as gs 
import urllib.request as ur
from bs4 import BeautifulSoup

def search(query):


  def google_scrape(url):
    thepage = ur.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

  i = 1
  strings = ''
  for url in gs(query, stop=5):
    a = google_scrape(url)
    strings = strings + str(i) + ". " + a + '\n'
    strings = strings + url + '\n'
    strings = strings + '\n' 
    i += 1

  return strings

if __name__ == '__main__':
  # to search 
  query = "郭文貴"

  content = search(query) 
  print(content)

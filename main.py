#!/usr/bin/env python3
import nltk
import re
from interpreter import *
from urllib import request

url = "http://www.gutenberg.org/cache/epub/10007/pg10007.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

text = prepareText(raw)
interpretText(text)







def prepareText(txt):
  
  # text content; the actual content of the book, excluding the gutenberg header and footer(license details)
  content = ''
  
  try:
    content = re.search(r'\*\*\*\s[a-zA-Z\s]+\s\*\*\*\s*(.+?)\s*\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*', txt).group(1)
  except AttributeError:
    # header/footers with enclosed text not found
    content = ''

  return content
  # end prepareText()
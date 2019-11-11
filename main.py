#!/usr/bin/env python3
from nltk import *
import re
from interpreter import *
from urllib import request


def prepareText(text):

    # text content; the actual content of the book, excluding the gutenberg header and footer(license details)
    content = ''

    try:
        content = re.search(
            r'\*\*\*\s[a-zA-Z\s]+\s\*\*\*\s*(.+?)\s*\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*', text).group(1)
    except AttributeError:
        # header/footers with enclosed text not found
        content = ''

    return content


def findKeyWords(clippedText):
    frequencyDist = FreqDist(clippedText)

    return sorted(w for w in set(clippedText)
                  if len(w) > 10 and frequencyDist[w] < 5)


url = "http://www.gutenberg.org/cache/epub/10007/pg10007.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

tokens = word_tokenize(raw)

text = prepareText(raw)

# interpretText(text)
print(findKeyWords(tokens))

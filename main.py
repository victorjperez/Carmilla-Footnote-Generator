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
            r'\*\*\*\s[a-zA-Z\s]+\s\*\*\*\s*((?:.*(?:\s*))+?)\s*\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*', text).group(1)

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

text = prepareText(raw)
tokens = word_tokenize(text)
lines = text.split('\n')
chapters = []
chapterNames = []

chapterRomanNumerals = ['PROLOGUE\r', 'I\r', 'II\r', 'III\r', 'IV\r', 'V\r', 'VI\r',
                        'VII\r', 'VIII\r', 'IX\r', 'X\r', 'XI\r', 'XII\r', 'XIII\r', 'XIV\r', 'XV\r', 'XVI\r']
chapterBuilder = ''
for lineNumber, line in enumerate(lines):
    if (line in chapterNames):
        continue
    if (line not in chapterRomanNumerals):
        chapterBuilder += line+'\n'
    else:
        chapters.append(chapterBuilder)
        chapterNames.append(lines[lineNumber+2])
        chapterBuilder = ''

chapterNames.pop(0)
chapters.pop(0)

for number, chapter in enumerate(chapters):
    if (number < 5):
        print(str(number) + ": " + chapter)

print(chapterNames)
# interpretText(text)
#  # print(findKeyWords(tokens))

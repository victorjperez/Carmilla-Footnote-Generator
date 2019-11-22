#!/usr/bin/env python3
from urllib import request
import nltk
import re
import interpreter
__import__('interpreter')


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


def concatChapters(chapters):
    text = ''
    for chapter in chapters:
        text += str(chapter)
    return text


url = "http://www.gutenberg.org/cache/epub/10007/pg10007.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

text = prepareText(raw)
tokens = nltk.word_tokenize(text)
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
chapters.append(chapterBuilder)

firstSentenceofPrologue = chapterNames.pop(0)
chapters[1] = chapters[1].lstrip()
print(chapters[1])
titleBlurb = chapters.pop(0)

outputFile = open("output_file.txt", "w+")
outputFile.write(titleBlurb)

fullTextTrimmed = concatChapters(chapters)
footnotes = interpreter.summarizeText(fullTextTrimmed, chapters)

for number, chapter in enumerate(chapters):
    outputFile.write(chapterRomanNumerals[number])
    if (number == 0):
        outputFile.write(firstSentenceofPrologue)
    else:
        outputFile.write(chapterNames[number-1])
    outputFile.write(chapter)
    outputFile.write(
        '\n\n[------------------------------------[SUMMARY]------------------------------------]\n')
    outputFile.write('\n' + footnotes[number] + '\n')
    outputFile.write(
        '\n[---------------------------------------------------------------------------------]\n\n')

outputFile.close()

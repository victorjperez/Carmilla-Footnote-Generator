import nltk
import re

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

#format of gutenburg book beginning
#start_of_txt = "\*\*\*\s[a-zA-Z\s]+\s\*\*\*"

# format of gutenburg book ending
#end_of_txt = "\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*\s\s\s\s\s\s\s\*"

  # #book title
  # title = ''
  # #book author
  # author = ''
  # #book year
  # year = ''

def formatSummary(text):
  # set lines to be 80 characters long
  t1 = text.replace(r"\n", "")
  lines = 1
  new_summary

  for i in range(len(t1)):
    
    if i >= lines*80 and t1[i] == " "

  return

# frequency table of entire novel = text
def getFreqTable(text) -> dict:

    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    ps = PorterStemmer()

    freq_table = dict()
    for word in words:
        word = ps.stem(word)
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table

def scoreSentences(sentences, freq_table) -> dict:
    sentence_value = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for word_value in freq_table:
            if word_value in sentence.lower():
                if sentence[:10] in sentence_value:
                    sentence_value[sentence[:10]] += freq_table[word_value]
                else:
                    sentence_value[sentence[:10]] = freq_table[word_value]

        sentence_value[sentence[:10]] = sentence_value[sentence[:10]] // word_count_in_sentence

    return sentence_value

def avgSentenceScore(sentence_value) -> int:
    sum_of_values = 0
    for entry in sentence_value:
        sum_of_values += sentence_value[entry]

    # Average value of a sentence from original text
    avg = int(sum_of_values / len(sentence_value))

    return avg

def addSummary(sentences, sentence_value, threshold):
  sentence_count = 0
  summary = ''

  for sentence in sentences:
      if sentence[:10] in sentence_value and sentence_value[sentence[:10]] > (threshold):
          summary += " " + sentence
          sentence_count += 1

  return summary

  # chapter: chapter from the .txt file retrieved from gutenberg.org; in this case, Carmilla (1872)
def summarizeText(text, chapters):

  freq_table = getFreqTable(text)
  footnotes = []

  for chapter in chapters:
    sentences = sent_tokenize(chapter)
    sentence_scores = scoreSentences(sentences, freq_table)
    threshold = avgSentenceScore(sentence_scores)
    summary = addSummary(sentences, sentence_scores, 1.5 * threshold)
    # formatted_summary = summary.replace("\\n", "")
    footnotes.append(summary)

  return footnotes
# end func()
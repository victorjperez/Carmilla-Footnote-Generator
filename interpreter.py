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

def _create_frequency_table(text_string) -> dict:
  
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable

def _score_sentences(sentences, freqTable) -> dict:
    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] // word_count_in_sentence

    return sentenceValue

def _find_average_score(sentenceValue) -> int:
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))

    return average

def _generate_summary(sentences, sentenceValue, threshold):
  sentence_count = 0
  summary = ''

  for sentence in sentences:
      if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] > (threshold):
          summary += " " + sentence
          sentence_count += 1

  return summary

  # chapter: chapter from the .txt file retrieved from gutenberg.org; in this case, Carmilla (1872)
def summarizeText(chapter):

  # 1 Create the word frequency table
  freq_table = _create_frequency_table(chapter)

  # 2 Tokenize the sentences
  sentences = sent_tokenize(chapter)

  # 3 Important Algorithm: score the sentences
  sentence_scores = _score_sentences(sentences, freq_table)

  # 4 Find the threshold
  threshold = _find_average_score(sentence_scores)

  # 5 Important Algorithm: Generate the summary
  summary = _generate_summary(sentences, sentence_scores, 1.5 * threshold)

  print(summary)

  return
# end func()
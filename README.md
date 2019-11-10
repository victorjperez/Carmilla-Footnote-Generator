Carmilla-Footnote-Generator

DIRECTORY:

main.py - main python file, to be executed

    prepares file to be interpreted by NLTK
    
interpreter.py - uses nltk functions to interpret text

    includes functions that determine plumbing words,
    determine terms that need to have a footnote,
    then generate footnotes for those words
    
INTERPRETATION PROCESS:

    Code should avoid catching words that may require background information, such as real-world locations, character names,

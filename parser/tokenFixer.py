import os

__author__ = 'Swastik'
import enchant
from utils import text_extractor as TextExtractor
import constants

dict = False

def is_english(word):
    global dict
    if not dict:
        dict = enchant.Dict("en_US")
    if len(word) == 0:
            return True
    return dict.check(word)


# Input - List of noun phrases. Each noun phrase might have broken words like.
# Each phrase contains space separated words
# n atural language, natural l anguage, natural languag e
#TODO Remove single numbers, Remove 'example', 'introduction', 'abstract'
def fix_broken_words(list):
    result = []
    phraseChanged = False
    for phrase in list:
        if len(phrase) == 0:
            continue
        words = phrase.split(" ")
        wordCount = len(words)
        newPhrase = []
        change = False

        for idx, word in enumerate(words):
            word = filter_hyphen(word)
            if len(word) == 0:
                continue
            if len(word) <= 3:
                if idx+1 < wordCount:   #Next word exists
                    nextWord = words[idx+1]
                    if not is_english(nextWord) and is_english(word+nextWord):  #If next word is meaningless, but jointly makes meaning, then merge
                        change = True
                        newPhrase.append(word+nextWord)
                        for word2 in words[idx+2:wordCount]:
                            newPhrase.append(filter_hyphen(word2))
                        break
                if idx-1 >= 0:   #If previous word exists
                    prevWord = words[idx-1]
                    if not is_english(prevWord) and is_english(prevWord+word):  #If previous word is meaningless, but jointly makes meaning, then merge
                        change = True
                        newPhrase= newPhrase[:-1]
                        newPhrase.append(prevWord+word)
                        for word2 in words[idx+1:wordCount]:
                            newPhrase.append(filter_hyphen(word2))
                        break

            if not change:#Not changed yet
                newPhrase.append(word)

        newPhrase = " ".join(newPhrase)
        result.append(newPhrase)
        if change:
            phraseChanged = True


    if phraseChanged:   #If Changed, do second iteration
        result, phraseChanged = fix_broken_words(result)
    return result, phraseChanged

def filter_hyphen(word):
    if not word.find('-')==-1:
        if is_english("".join(word.split("-"))):
            word = word.replace("-","")
        else:
            word = word.replace("-"," ")
    return word

def test():
    # print(is_english("l"))
    # print(is_english("anguage"))
    # print(is_english("language"))
    # print(fix_broken_words(["natural l anguage", "n atural language", "natural languag e"]))
    list = TextExtractor.extract_corrected_text(os.path.join(constants.DATA_PATH, "authors_topic", "10.txt")).split(",")
    print(fix_broken_words(list))

if __name__ == '__main__':
    test()
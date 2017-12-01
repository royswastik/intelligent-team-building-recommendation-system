import os

__author__ = 'Swastik'
import enchant
from utils import text_extractor as TextExtractor, stopper
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
        if do_remove_phrase(phrase):
            # print("Removing: " + phrase)
            continue
        words = phrase.split(" ")
        wordCount = len(words)
        newPhrase = []
        change = False

        for idx, word in enumerate(words):
            word = filter_hyphen(word)
            if len(word) == 0:
                continue

            if do_remove_word(word):
                # print("Removing: " + word)
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

        if len(newPhrase) == 0: #If all words removed
            continue
        newPhrase = " ".join(newPhrase)
        result.append(newPhrase.strip())

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

#Check if the word has to be removed
def do_remove_word(w):
    if stopper.is_digit(w) or stopper.is_day(w) or stopper.is_date(w) or stopper.is_roman_numeral(w):
        return True
    elif stopper.is_time(w) or stopper.is_month(w) or stopper.is_year(w) or stopper.is_org_suffix(w) or stopper.is_person_prefix(w):
        return True
    elif stopper.is_location(w):    #country city or state
        return True
    elif stopper.is_nationality(w) or stopper.is_currency(w):
        return True
    elif stopper.is_language(w) or stopper.is_article_header(w):
        return True
    elif stopper.is_name(w):
        return True

    return False

def do_remove_phrase(phrase):
    if phrase in  stopper.CUSTOM_PHRASES_STOPS:
        return True

    if phrase.split(" ")[-1] in stopper.CUSTOM_PREFIX_STOP:
        return True

    if phrase.split(" ")[0] in stopper.CUSTOM_SUFFIX_STOP:
        return True

    return False

def test():
    # print(is_english("l"))
    # print(is_english("anguage"))
    # print(is_english("language"))
    # print(fix_broken_words(["natural l anguage", "n atural language", "natural languag e"]))
    list = TextExtractor.extract_corrected_text(os.path.join(constants.DATA_PATH, "authors_topic", "10.txt")).split(",")
    print("Number of phrases:"+str(len(list)))
    fixed_list, phraseChanged = fix_broken_words(list)
    print("Number of phrases:"+str(len(list)))
    print("Fixed Number of phrases:"+str(len(fixed_list)))
    TextExtractor.write_to_file((",".join(fixed_list)), os.path.join(constants.TEST_OUTPUT, '10.txt'))
    print("Success")

def test():
    # if not os.path.isdir(os.path.join(constants.DATA_PATH, "authors_topic")):
    #     os.mkdir(os.path.join(constants.DATA_PATH, "authors_topic"))
    for fileName in os.listdir(os.path.join(constants.DATA_PATH,'authors_topic')):
        outPath = os.path.join(constants.DATA_PATH,'author_topic_filtered', fileName)
        if os.path.isfile(outPath): #Already exist
            continue
        print(fileName)
        list = TextExtractor.extract_corrected_text(os.path.join(constants.DATA_PATH, "authors_topic", fileName)).split(",")
        print("Number of phrases:"+str(len(list)))
        fixed_list, phraseChanged = fix_broken_words(list)
        print("Fixed Number of phrases:"+str(len(fixed_list)))
        TextExtractor.write_to_file((",".join(fixed_list)), outPath)

    print("Success")

if __name__ == '__main__':
    test()
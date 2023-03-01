# imports
# import phantom_tollbooth
import string
import re
import collections


skip_words = ('the', 'a', 'an', 'of', 'on', 'over', 'above', 'and', 'but', 'or', 'he', 'her', 'it', 'to',
              'you', 'in', 'as', 'by', 'his', 'for', 'was', 'at', 'this', 'be', 'is', 'for', 'was', 'in', 'with', 'they', 'me', 'how', 'd', 's', 'm', 'll', 'i')
# create word count dict
word_count = {}


def count_words(text):
    # remove special characters using re(regular expresion) module
    # doc link (https://docs.python.org/3/library/re.html)
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    # split the text into words using split and make it all lowercase.
    for word in text.lower().split():
        # Check to make sure word is not in the skip words list.
        if word not in skip_words:
            # Checks to make sure value is not already recorded and if so adds word to the dict else add +1 to the value of word in dict.
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1


# test_list = ["test","test","test","as","as","am"]
def organize_words():
    # Sort the word_count dict into a counter that can be used with the most_common function.
    temp_count = collections.Counter(word_count)
    print("The most common words in Phantom Tollbooth are as follows: ")
    # for each word in the counter temp_count print the word and its repective value.
    for word, count in temp_count.most_common(50):
        print(f"{word} used {count} times.")


# count_words(book)
# print(word_count)
# organize_words()
# organize_words()

"""Utility functions for word collections.

Author: Dilpreet Singh Gill
Version: 11/04/2023
"""
from nltk.corpus import wordnet


def check_punctuation(word):
    """Check if text has surrounding punctuation.

    String slice around a given string to see if it contains
    the following: ().,?!;:#-_'"

    Args:
        word(str): The word to process

    Returns:
        final(str): The word without punctuation
    """
    final = word
    punctuation_list = ['(', ')', '.', ',', '?', '!', ';', ':', '#', '-', '_', "'", '"']
    # check if both sides have punctuation
    if word[0] in punctuation_list and word[-1] in punctuation_list:
        final = word[1:-1]
    # check if first item is punctuation
    elif word[0] in punctuation_list:
        final = word[1:]
    # check if last item is punctuation
    elif word[-1] in punctuation_list:
        final = word[:-1]
    return final


def check_letters(word):
    """Check each letter in a word to make sure it is in the English alphabet.

    It turns out s.isalpha() accepts characters with umlauts and accent marks,
    which cannot easily be typed on an English keyboard.  Return True if the
    word contains only the letters 'A' through 'Z' and False otherwise.

    Args:
        word(str): the word to check

    Returns:
        bool: True if the word contains only English letters
    """
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    sep_alpha = alphabet.split()
    for letter in word:
        if letter.isupper() is True:
            continue
        else:
            return False
    is_valid = True
    for letter in word.upper():
        if letter not in sep_alpha:
            is_valid = False
        else:
            continue
    return is_valid


def collect_unique_words(text):
    """Take the text string passed in and produce a set of unique words.

    Split the text into words
    Change every word to uppercase
    Remove all common surrounding punctuation: ().,?!;:#-_'"
    Place the words into a set to remove duplicates, and return

    Args:
        text(str): The text to process

    Returns:
        set: set of unique words from the text
    """
    if text == '':
        return set()
    final = set()
    split_text = text.split()
    for word in split_text:
        upper_word = word.upper()
        final.add(check_punctuation(upper_word))
    return final


def clean_word_set(word_set):
    """Take a set of unique words and produce a set of legal words.

    Return a list of the words that have no duplicate letters and contain only letters
    And are considered valid words by nltk

    Args:
        word_set(set): a set of words

    Returns:
        list: list of legal words from the set, all made uppercase
    """
    final = list()
    for word in word_set:
        if check_letters(word) is True:
            if len(word) == len(set(word)):
                if wordnet.synsets(word) != []:
                    final.append(word)
        else:
            continue
    return final


def categorize_words(word_list):
    """Take a list of legal unique words and categorized them by word length into a dictionary.

    Produce a dictionary of the form {int:list} where a key is a word length and its value
    is a list of words of that length, for example:
    {
     2: ['is', 'on', 'at'],
     5: ['value', 'legal', 'words', 'trail']
    }

    Args:
        word_list(list): a list of words

    Returns:
        dict: a dictionary categorized by word length
    """
    final = dict()

    for word in word_list:
        word_length = len(word)
        if word_length in final:
            final[word_length].append(word)
        else:
            final[word_length] = [word]
    return final

"""The main module of words.

Author: Dilpreet Singh Gill
"""
import sys
import os
import colorama
import nltk

import words_game
from words_utils import collect_unique_words, categorize_words, clean_word_set
from words_file_utils import process_word_file


def process_args(args):
    """Process the command-line arguments.

    Check for the correct number of args. Print the usage statement & then return None if incorrect.
    For each file:
        - If a file does not exist (according to the os module) just skip it with no messages.
        - Use  process_word_file function to make sure each file has the right format and read text.
        - If a file has the wrong format or no text, just skip it with no messages.
        - Use collect_unique_words function to process the file's text into set of unique words.
        - Use clean_word_set function to process the unique word set into list of valid words.
        - If any word are left, use categorize_words function to put them into a dictionary
        organized by lengths (key is length) and add that dictionary and the word collection title
        to a list of tuples.
    Return the list of tuples - 1 tuple per file that has no errors and contains valid words.

    Args:
        args (list): the list of command line arguments

    Returns:
        list: a list of tuples, where each tuple contains a str (title of collection),
                and a dict (of the words from the collection)
    """
    if len(args) < 2:
        print("Usage: python word_main.py file1 [file2 ...]")
        return None

    word_dicts = []

    for filename in args[1:]:
        if not os.path.isfile(filename):
            continue

        result = process_word_file(filename)

        if result is None:
            continue

        title, words_text = result

        # Process the file's text into a set of unique words
        unique_words_set = collect_unique_words(words_text)

        # Process unique word set into list of valid words
        valid_words_list = clean_word_set(unique_words_set)

        # If there are valid words, categorize them by lengths into a dictionary

        # TODO - don't need to call categorize_words if it's blank, don't even add it to the list
        if valid_words_list:
            word_length_dict = categorize_words(valid_words_list)
            word_dicts.append((title, word_length_dict))
    return word_dicts


if __name__ == "__main__":
    # Make sure that colorama resets to the default color for your screen when not playing the game
    colorama.init(autoreset=True)

    # load the nltk wordnet data
    nltk.download('wordnet')

    word_dicts = process_args(sys.argv)
    if word_dicts is None:
        sys.exit(1)

    if len(word_dicts) > 0:
        words_game.play_words_game(word_dicts)
    else:
        print("No legal words in these collections.")

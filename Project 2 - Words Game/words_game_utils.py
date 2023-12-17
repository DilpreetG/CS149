"""Words game utility functions.

Author: Dilpreet Singh Gill
Version: 11/05/2023
"""

import random
from colorama import Fore
from nltk.corpus import wordnet

BULL = 2
COW = 1
WRONG = 0


def get_hint(word):
    """Return a hint for this word.

    PART C: use nltk to get a definition for this word.

    Args:
        word (str): the word to find a definition for

    Returns:
        str: a definition or hint for this word
    """
    hint = wordnet.synsets(word)
    return hint[0].definition()


def is_valid_word(word):
    """Check that this word is not a proper noun and a real dictionary word.

    PART C: use nltk to assure this is a regular dictionary word.

    Args:
        word (str): the word to check

    Returns:
        bool: True if this is a valid game word
    """
    definition = wordnet.synsets(word)
    return definition != []


def get_random_word(word_dict, length):
    """Select a random word of the selected length.

    Args:
        word_dict (dict): a dict {int:list} where a key is a length,
            and the value is a list of words of that length
        length (int): the desired word length

    Returns:
        str: a random word from the word_dict's list for the given length
    """
    if length in word_dict:
        return random.choice(word_dict[length])
    else:
        return None


def check_guess(secret, guess):
    """Compare the user's guess to the secret word.

    If the guess is the wrong length return None
    Create an empty list, the for each letter in the guess:
        add a 0 (WRONG) if the letter is not in the secret word
        add a 1 (COW) if the letter is in the word but in the wrong position
        add a 2 (BULL) if the letter is in the correct position in the word

    Args:
        secret (str): the secret word being guessed
        guess (str): the current guess

    Returns:
        list: a list of markers, one for each letter
    """
    final = list()
    indx = 0
    if len(guess) != len(secret):
        return None
    for letter in guess:
        if letter in secret and secret.find(letter, indx) == guess.find(letter, indx):
            final.append(BULL)
            indx += 1
        elif letter in secret:
            final.append(COW)
            indx += 1
        else:
            final.append(WRONG)
            indx += 1
    return final


def color_string(result, guess):
    """Using a result list of letter markers and a guess, print the word in the "Wordle" colors.

    Color scheme:
        red if the letter is not in the secret word
        yellow if the letter is in the word but in the wrong position
        green if the letter is in the correct position in the word
    To assure the resulting string is readable to all users:
        surround green letters with square brackets []
        surround yellow letters with parentheses ()
        leave red letters as is
    For example:
        color_string([1, 0, 2, 1, 0], "PRINT") -> "(P)R[I](N)T"

    Args:
        result (str): the list of letter markers - 0, 1, 2
        guess (str): the current guess

    Returns:
        str: a string where each letter has the right color and is visually marked
    """
    indx = 0
    final = ''
    for item in result:
        if item == BULL:
            final += Fore.GREEN + ('[' + guess[indx] + ']') + Fore.RESET
            indx += 1
        elif item == COW:
            final += Fore.YELLOW + ('(' + guess[indx] + ')') + Fore.RESET
            indx += 1
        elif item == WRONG:
            final += Fore.RED + guess[indx] + Fore.RESET
            indx += 1
    return final


def collection_menu(word_dicts):
    """Create a single string of the word collection names for the user to select from.

        COLLECTIONS
        0    collection_name_0
        1    collection_name_1
        ...
        n    collection_name_n

    Args:
        word_dicts (list): a list of tuples of type (str, dict): a name and a word collection

    Returns:
        str: a string with the given format
    """
    indx = 0
    final = 'COLLECTIONS\n'
    for item in word_dicts:
        final += f'{indx}    {item[0]}\n'
        indx += 1
    return final

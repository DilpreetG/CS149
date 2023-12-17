"""File utility functions.

Author: Dilpreet Singh Gill
Version: 11/05/2023
"""


def process_word_file(filename):
    """Read the file, check its correctness and return the word collection name and its data.

    This file has the following format: The first line must contain the word WORDS
    followed by a space, and the rest of the first line is interpreted as the name
    for this collection of words. The following lines in the file can be in any format,
    for example:
            WORDS War and Peace
            ...
            the text of the book War and Peace
            ...

    If any of the following errors occur, the function should return None:
        The file does not have "WORDS" as the first word on the first line
        The file does not contain a name for the word collection on the 1st line
        The rest of the file is empty
    If there are no errors, the function should return a tuple of 2 items:
        the name of the word collection in a single string
        the word collection in a single string

    Args:
        filename (str): The name of the file to read from

    Returns:
        str: The name to use for this collection of words
        str: The rest of the file in a single string
        None: if any of the errors occur
    """
    try:
        with open(filename, 'r') as file:
            header = file.readline().strip()
            if not header.startswith("WORDS ") or header[6:] == "":
                return None
            name = header[6:]
            content = file.read()
            if not content.strip():
                return None
            return name, content
    except FileNotFoundError:
        return None

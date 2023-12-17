from words_file_utils import process_word_file


def test_process_word_file():
    # Test case 1: Correct file format with non-empty content
    with open("test_case_1.txt", "w") as test_file:
        test_file.write("WORDS SampleCollection\nThis is a test collection.")

    result = process_word_file("test_case_1.txt")
    assert result == ("SampleCollection", "This is a test collection.")

    # Test case 2: Incorrect file format (missing "WORDS")
    with open("test_case_2.txt", "w") as test_file:
        test_file.write("InvalidCollection\nThis is an invalid collection.")

    result = process_word_file("test_case_2.txt")
    assert result == (None)
    # Test case 3: Incorrect file format (empty collection name)
    with open("test_case_3.txt", "w") as test_file:
        test_file.write("WORDS \nThis is an invalid collection.")

    result = process_word_file("test_case_3.txt")
    assert result == (None)

    # Test case 4: File is empty
    with open("test_case_4.txt", "w") as test_file:
        pass

    result = process_word_file("test_case_4.txt")
    assert result == (None)


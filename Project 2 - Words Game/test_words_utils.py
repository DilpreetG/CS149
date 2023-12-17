from words_utils import check_letters, collect_unique_words

def test_check_letters():
    assert check_letters('a34d') == False
    assert check_letters('A34D') == False
    assert check_letters('a_-d') == False
    assert check_letters('a`4~d') == False
    assert check_letters('acd') == False
    assert check_letters('ACD') == True
    assert check_letters('HE-RE') == False
    assert check_letters('ACD') == True

def test_collect_unique_words():
    unordered_set = {'THE', 'LAZY', 'BROWN', 'FOX', 'JUMPED', 'OVER', 'HOG'}
    assert collect_unique_words('The lazy brown fox jumped over hog') == unordered_set

test_check_letters()
test_collect_unique_words()

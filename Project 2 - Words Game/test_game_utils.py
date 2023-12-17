import words_game_utils
from words_game_utils import check_guess, WRONG, COW, BULL, color_string, collection_menu
from colorama import Fore


def test_check_guess():
    secret_word = "APPLE"
    guess = "APPLE"
    result = words_game_utils.check_guess(secret_word, guess)
    assert result == [2, 2, 2, 2, 2]

    secret_word = "TIGER"
    guess = "LIONS"
    result = words_game_utils.check_guess(secret_word, guess)
    assert result == [0, 2, 0, 0, 0]

    assert check_guess("PONGO", "WRONG") == [WRONG, WRONG, COW, COW, COW]

    secret_word = "PYTHON"
    guess = "NYTHOP"
    result = words_game_utils.check_guess(secret_word, guess)
    assert result == [1, 2, 2, 2, 2, 1]


def test_color_string():
    expected_result = Fore.RED + "W" + Fore.RESET + Fore.RED + "R" + Fore.RESET
    expected_result += Fore.YELLOW + "(O)" + Fore.RESET + Fore.YELLOW + "(N)" + Fore.RESET
    expected_result += Fore.YELLOW + "(G)" + Fore.RESET
    assert color_string([WRONG, WRONG, COW, COW, COW], "WRONG") == expected_result

    expected_result = Fore.GREEN + '[A]' + Fore.RESET + Fore.GREEN + '[P]' + Fore.RESET
    expected_result += Fore.GREEN + '[P]' + Fore.RESET + Fore.GREEN + '[L]' + Fore.RESET
    expected_result += Fore.GREEN + '[E]' + Fore.RESET
    assert color_string([BULL, BULL, BULL, BULL, BULL], 'APPLE') == expected_result

    expected_result = Fore.RED + "N" + Fore.RESET + Fore.RED + "Y" + Fore.RESET
    expected_result += Fore.YELLOW + "(T)" + Fore.RESET
    expected_result += Fore.GREEN + "[H]" + Fore.RESET + Fore.RED + "O" + Fore.RESET
    expected_result += Fore.RED + "P" + Fore.RESET
    assert color_string([WRONG, WRONG, COW, BULL, WRONG, WRONG], "NYTHOP") == expected_result


def test_collection_menu():
    assert collection_menu([("Dogs", {}), ("Cats", {}), ("CS149", {})]) == \
           "COLLECTIONS\n" \
           "0    Dogs\n" \
           "1    Cats\n" \
           "2    CS149\n"


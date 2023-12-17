"""Poker Dice - a poker like dice game with 5 dice.

Each dice is six sided and has the following face values:
['9', '10', 'J', 'Q', 'K', 'A']
The game is played in 9 rounds where 5 dice are rolled and the player must assign to one of the
9 categories for scoring in each round.

Author: CS 149 Instructors
Version: 10-1-23
"""

from dice import roll_dice
import score_dice as score


if __name__ == "__main__":
    print("Poker Dice:")
    print("[1] pair, [2] pair, [3] of a kind), [4] of a kind, [5] of a kind")
    print("[6] Full House, [7]Small Straight, [8] Large Straight, [9]Chance")
    print("-"*80)
    total = 0
    left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1, 10):
        invalid = True
        category = 0
        dice = roll_dice(5, None)
        while(invalid and i <= 9):
            print("\tDice:", i, " ", end="")
            print(dice)
            category = input("\tSelect a valid category[1-9]: ")
            if category and category.isdigit():
                category = int(category)
                if category > 0 and category <= 9 and category in left:
                    invalid = False
        left.remove(category)
        total += score.calculate_score(dice, int(category))
        print("\tScore: ", total)
        print("Categories left:", left)
    print("End of Game.  You scored:", total, "points.")
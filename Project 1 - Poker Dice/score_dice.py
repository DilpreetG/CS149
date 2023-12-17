"""Plays a text based game of Poker Dice.

Author: Dilpreet Singh Gill
Version: 10/31/2023
"""

import dice
from dice import num_faces
from dice import add_values

# Constants that specify scoring types
PAIR = 1
TWO_PAIR = 2
THREE_OF_KIND = 3
FOUR_OF_KIND = 4
FIVE_OF_KIND = 5
FULL_HOUSE = 6
SMALL_STRAIGHT = 7
LARGE_STRAIGHT = 8
CHANCE = 9
FACES = dice.FACES
FACE_VALUES = dice.FACE_VALUES


def one_pair(dice_list):
    """Calculate score of dice faces according to one pair scoring.

    Args:
        dice_list (list): 5 dice roll faces.
        
    Returns:
        (list): The score amount.
    """
    final = 0
    for item in reversed(FACES):
        if num_faces(dice_list, item) >= 2:
            final = FACE_VALUES[item] * 2
            break
    return final
     
     
def two_pair(dice_list):
    """Calculate score of dice faces according to two pair scoring.

    Args:
        dice_list (list): 5 dice roll faces.

    Returns:
        (int): The score amount.
    """
    final = 0
    facemath1 = 0
    facemath2 = 0
    for item in reversed(FACES):
        if num_faces(dice_list, item) >= TWO_PAIR:
            if facemath1 == 0:
                facemath1 = FACE_VALUES[item]
                continue
            elif facemath1 != 0:
                facemath2 = FACE_VALUES[item]
                final += (facemath1 * 2) + (facemath2 * 2)
    return final


def three_of_a_kind(dice_list):
    """Calculate score of dice faces according to three of a kind scoring.

    Args:
        dice_list (list): 5 dice roll faces.

    Returns:
        (int): The score amount.
    """
    final = 0
    for item in reversed(FACES):
        if num_faces(dice_list, item) >= THREE_OF_KIND:
            facemath1 = FACE_VALUES[item]
            final = (facemath1 * 3) + 10
            continue
    return final


def four_of_a_kind(dice_list):
    """Calculate score of dice faces according to four of a kind scoring.

    Args:
        dice_list (list): 5 dice roll faces.

    Returns:
        (int): The score amount.
    """
    final = 0
    for i in FACES:
        if num_faces(dice_list, i) >= FOUR_OF_KIND:
            final = FACE_VALUES[i] * 4
            final += 20
    return final


def five_of_a_kind(dice_list):
    """Calculate score of dice faces according to five of a kind scoring.

    Args:
        dice_list (list): 5 dice roll faces.

    Returns:
        (int): The score amount.
    """
    final = 0
    for item in reversed(FACES):
        if num_faces(dice_list, item) == FIVE_OF_KIND:
            final = 100
    return final


def full_house(dice_list):
    """Calculate score of dice faces according to full house scoring.

    Args:
        dice_list (list): 5 dice roll faces.

    Returns:
        (int): The score amount.
    """
    final = 0
    for item in reversed(FACES):
        if num_faces(dice_list, item) == 3:
            final += FACE_VALUES[item] * 3
            final += 50
        elif num_faces(dice_list, item) == 2:
            final += FACE_VALUES[item] * 2
    return final


def small_straight(dice_list):
    """Calculate score of dice faces according to small straight scoring.

    Args:
        dice_list (list): 5 dice roll faces.

    Returns:
        (int): The score amount.
    """
    final = 0
    final_set = set()
    for i in FACES:
        if i in dice_list:
            final_set.add(i)
    if 'J' in final_set:
        if 'Q' in final_set:
            if '10' in final_set:
                if '9' in final_set or 'K' in final_set:
                    final = 70
            elif 'K' in final_set:
                if 'A' in final_set:
                    final = 70
    else:
        final = 0
    return final    


def large_straight(dice_list):
    """Calculate score of dice faces according to large straight scoring.

    Args:
        dice_list (list): 5 dice roll faces.

    Returns:
        (int): The score amount.
    """
    final = 0
    final_set = set()
    posb1 = {'9', '10', 'J', 'Q', 'K'}
    posb2 = {'10', 'J', 'Q', 'K', 'A'}
    for i in dice_list:
        final_set.add(i)
    if final_set == posb1 or final_set == posb2:
        final = 95
    return final


def chance(dice_list):
    """Calculate score of dice faces according to chance scoring.

    Args:
        dice_list (list): 5 dice roll faces.

    Returns:
        (int): The score amount.
    """
    final = add_values(dice_list)
    return final


def calculate_score(dice_list, score_type):
    """Calculate Poker Dice score based on dice_list and score_type.

    Args:
        dice_list (list): 5 values representing the outcome of the rolls.
        score_type (int): The type (category) to score.

    Returns:
        (final): The score amount.
    """
    if score_type == PAIR:
        final = one_pair(dice_list)
    elif score_type == TWO_PAIR:
        final = two_pair(dice_list)
    elif score_type == THREE_OF_KIND:
        final = three_of_a_kind(dice_list)
    elif score_type == FOUR_OF_KIND:
        final = four_of_a_kind(dice_list)
    elif score_type == FIVE_OF_KIND:
        final = five_of_a_kind(dice_list)
    elif score_type == FULL_HOUSE:
        final = full_house(dice_list)
    elif score_type == SMALL_STRAIGHT:
        final = small_straight(dice_list)
    elif score_type == LARGE_STRAIGHT:
        final = large_straight(dice_list)
    elif score_type == CHANCE:
        final = chance(dice_list)
    return final

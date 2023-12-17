"""Dice.py Module.

Author: Dilpreet Singh Gill
Version: 10/23/2023
"""

import random

FACES = ['9', '10', 'J', 'Q', 'K', 'A']

FACE_VALUES = {'9': 9,
               '10': 10,
               'J': 10,
               'Q': 10,
               'K': 10,
               'A': 11, }

di_bnd = (1, 11)


def roll_dice(num_dice=None, seed=None):
    """Roll dice with faces.

    Args:
        num_dice (int): Number of dice to be rolled.
        seed (int): Seed to be used.

    Returns:
        (list): The score amount.
    """
    if num_dice is None and seed is None:
        seed = 0
        num_dice = 5
    if num_dice not in range(di_bnd[0], di_bnd[1]):
        return_list = ['9']
        return return_list
    random.seed(seed)
    return_list = []
    for i in range(num_dice):
        index = random.randint(0, 5)
        return_list.append(FACES[index])
    return return_list


def are_valid(check_list=None):
    """Check if list length is 1-10, and if faces are valid.

    Args:
        check_list (list): List of faces.

    Returns:
        (bool): False if a face in list/length isn't valid, else, True.
    """
    if check_list is None:
        return False
    if len(check_list) > 10 or len(check_list) < 1:
        return False
    for item in check_list:
        if item not in FACES:
            return False
    return True


def add_values(dice=None):
    """Calculate and return sum of values of dice/faces in list.

    Args:
        dice (list): List of dice rolls.

    Returns:
        (int): Sum of values of die/faces.
    """
    sum_vals_dice = 0
    if are_valid(dice) is False:
        return -1
    for item in dice:
        sum_vals_dice += FACE_VALUES[item]
    return sum_vals_dice


def num_faces(dice_list=None, face_counted=None):
    """Count instances of certain item in a list.

    Args:
        dice_list (list): List of dice/face values.
        face_counted (str): Face to be checked.

    Returns:
        (int): The number of instances.
    """
    count = 0
    if are_valid(dice_list) is False:
        return -1
    for i in dice_list:
        if i is face_counted:
            count += 1
    return count

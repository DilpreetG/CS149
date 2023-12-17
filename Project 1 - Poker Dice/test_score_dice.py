import score_dice


def test_calculate_score_one_pair_no_match():
    my_dice = ['9', 'A', '10', 'J', 'K']
    assert score_dice.calculate_score(my_dice, score_dice.PAIR) == 0


def test_calculate_score_one_pair_one_match():
    my_dice = ['Q', '9', 'Q', '9', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.PAIR) == 20


def test_calculate_score_two_pair_no_match():
    my_dice = ['10', 'K', '9', 'A', '9']
    assert score_dice.calculate_score(my_dice, score_dice.TWO_PAIR) == 0
    
    
def test_calculate_score_two_pair_one_match():
    my_dice = ['9', '9', 'A', 'J', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.TWO_PAIR) == 40
    
    
def test_calculate_score_three_of_a_kind_match():
    my_dice = ['J', '9', 'J', '9', 'J']
    assert score_dice.calculate_score(my_dice, score_dice.THREE_OF_KIND) == 40
   
   
def test_calculate_score_three_of_a_kind_no_match():
    my_dice = ['K', '9', 'K', '9', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.THREE_OF_KIND) == 0


def test_calculate_score_four_of_a_kind_match():
    my_dice = ['K', 'K', 'K', '9', 'K']
    assert score_dice.calculate_score(my_dice, score_dice.FOUR_OF_KIND) == 60

  
def test_calculate_score_four_of_a_kind_no_match():
    my_dice = ['10', 'J', '10', 'J', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.FOUR_OF_KIND) == 0


def test_calculate_score_five_of_a_kind_match():
    my_dice = ['A', 'A', 'A', 'A', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.FIVE_OF_KIND) == 100


def test_calculate_score_five_of_a_kind_no_match():
    my_dice = ['9', '9', '9', '9', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.FIVE_OF_KIND) == 0


def test_calculate_score_full_house_match():
    my_dice = ['9', '9', '9', '9', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.FULL_HOUSE) == 0
    
    my_dice = ['9', '9', '9', 'A', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.FULL_HOUSE) == 99
    
    my_dice = ['A', '9', '9', '9', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.FULL_HOUSE) == 99
    
    
def test_calculate_score_small_straight_match():
    my_dice = ['10', 'J', '9', 'K', 'Q']
    assert score_dice.calculate_score(my_dice, score_dice.SMALL_STRAIGHT) == 70
    
    
def test_calculate_score_small_straight_no_match():
    my_dice = ['A', 'K', 'Q', '10', '9']
    assert score_dice.calculate_score(my_dice, score_dice.SMALL_STRAIGHT) == 0
    
    
def test_calculate_score_large_straight_match():
    my_dice = ['9', 'J', 'Q', 'K', '10']
    assert score_dice.calculate_score(my_dice, score_dice.LARGE_STRAIGHT) == 95
    my_dice = ['K', 'A', 'Q', 'J', '10']
    assert score_dice.calculate_score(my_dice, score_dice.LARGE_STRAIGHT) == 95
  
  
def test_calculate_score_large_straight_no_match():
    my_dice = ['9', 'J', 'Q', 'K', 'A']
    assert score_dice.calculate_score(my_dice, score_dice.LARGE_STRAIGHT) == 0
    
    
def test_calculate_score_chance_match():
    my_dice = ['9', 'K', '9', 'K', '10']
    assert score_dice.calculate_score(my_dice, score_dice.CHANCE) == 48
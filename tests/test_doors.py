import random
from montyhall.funcs import *
from montyhall import *

# ------- Auxiliary functions
def setup_doors_testing(standard=True):
    iterations = 100000
    doors_max = 10
    doors_standard = 3
    doors_min = doors_standard
    precision = 1 # if increased, make sure number of iterations is also increased
    if standard:
        doors_total = doors_standard
        doors_prize = doors_standard - 2
    else:
        doors_total = random.randint(doors_min, doors_max)
        doors_prize = doors_total - random.randint(1, doors_total - 2)
    win_counter, loss_counter = 0, 0
    for i in range(iterations):
        doors = setup_doors(doors_total, doors_prize)
        if random.choice(doors).prize == prize.win:
            win_counter += 1
        else:
            loss_counter += 1
    assert round(win_counter / iterations, precision) == round(doors_prize / doors_total, precision), 'Wrong statistics for winnning doors.'
    assert round(loss_counter / iterations, precision) == round((doors_total - doors_prize) / doors_total, precision), 'Wrong statistics for losing doors.'

def make_guesses_testing(total_doors=3, guesses=1):
    count = 0
    doors = make_guesses(setup_doors(total_doors=total_doors), guesses=guesses)
    for door in doors:
        if door.isGuessed():
            count += 1
    assert count == guesses, 'Wrong count of guessed.'

def open_losing_doors_testing(doors_to_open=1):
    for total_doors in range(doors_to_open+3 ,doors_to_open*10):
        open_door_count = 0
        doors = open_losing_doors(setup_doors(total_doors=total_doors), total_doors_to_open=doors_to_open)
        for door in doors:
            if door.isOpen():
                assert not door.hasPrize(), 'Failure: found a winning door that is open. '
                open_door_count += 1
        assert open_door_count == doors_to_open, 'Wrong count of open doors.'

# ------- Test functions
def test_get_prize_doors():
    for num_of_doors in range(3,10):
        num_of_prize_doors = num_of_doors - 2
        if num_of_doors == 3:
            drs = get_prize_doors()
        else:
            drs = get_prize_doors(total_doors = num_of_doors, prize_doors = num_of_prize_doors)
        assert len(drs) == num_of_doors, 'Wrong size of the returned dictionary.'
        assert list(drs.values()).count(prize.win) == num_of_prize_doors, 'Wrong count of prizes.'
        assert list(drs.values()).count(prize.bust) == num_of_doors - num_of_prize_doors, 'Wrong count of losing doors.'


def test_setup_doors_standard():
    setup_doors_testing(standard=True)

def test_setup_doors_non_standard():
    setup_doors_testing(standard=False)

def test_make_guesses():
    make_guesses_testing() # test for default
    for doors in range(4,20):
        for guesses in range(1,10):
            if guesses < doors:
                make_guesses_testing(total_doors=doors, guesses=guesses)

def test_open_losing_doors():
    open_losing_doors_testing()
    for doors_to_open in range(1,10):
        open_losing_doors_testing(doors_to_open=doors_to_open)

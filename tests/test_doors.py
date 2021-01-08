import random
import montyhall
from montyhall import *

def test_get_prize_doors():
    for num_of_doors in range(3,10):
        num_of_prize_doors = num_of_doors - 2
        if num_of_doors == 3:
            d = get_prize_doors()
        else:
            d = get_prize_doors(total_doors = num_of_doors, prize_doors = num_of_prize_doors)
        assert len(d) == num_of_doors, 'Wrong size of the returned dictionary.'
        assert list(d.values()).count(prize.win) == num_of_prize_doors, 'Wrong count of prizes.'
        assert list(d.values()).count(prize.bust) == num_of_doors - num_of_prize_doors, 'Wrong count of losing doors.'

def setup_doors_testing(standard=True):
    iterations = 100000
    max_doors = 10
    precision = 1 # if increased, make sure number of iterations is also increased
    if standard:
        total_doors = 3
        prize_doors = 1
    else:
        total_doors = random.randint(1, max_doors)
        prize_doors = total_doors - random.randint(1, total_doors - 2)
    win_counter, loss_counter = 0, 0
    for i in range(iterations):
        doors = setup_doors(total_doors, prize_doors)
        if random.choice(doors).prize == prize.win:
            win_counter += 1
        else:
            loss_counter += 1
    assert round(win_counter / iterations, precision) == round(prize_doors / total_doors, precision), 'Wrong statistics for winnning doors.'
    assert round(loss_counter / iterations, precision) == round((total_doors - prize_doors) / total_doors, precision), 'Wrong statistics for losing doors.'

def test_setup_doors_standard():
    setup_doors_testing(standard=True)

def test_setup_doors_non_standard():
    setup_doors_testing(standard=False)

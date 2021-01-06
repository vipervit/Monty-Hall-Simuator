import logging
import random
from enum import Enum


logger = logging.getLogger(__name__)
console = logging.StreamHandler()
logger.addHandler(console)
logger.setLevel(logging.INFO)


class door():
    id = None
    hasPrize = False
    isOpen = False
    markedGuessed = False

class prize(Enum):
    win = 'CAR!'
    bust = 'GOAT'

def get_prize_doors(num_of_doors=3, num_of_prize_doors=1):
    doors = {}
    for i in range(num_of_doors):
        doors.update({i: prize.bust})
    while list(doors.values()).count(prize.win) < num_of_prize_doors:
        doors[random.choice(range(len(doors)))] = random.choice([prize.win, prize.bust])
    return doors

# def setup_doors(num_of_doors=3):
#     doors = []
#     for i in range(num_of_doors):
#         door.id = i
#         for j in range(num_of_prize_doors):
#             door.hasPrize = random.choice()
#
# def make_guess(doors):
#     doors[random.choice(list(doors))] = statuses.guessed
#     return doors
#
# def open_losing_door(doors, guessed):
#     doors[random.choice([x for x in list(doors) if doors[x] is not statuses.win and x is not guessed])] = statuses.open
#     return doors

import logging
import random
from enum import Enum


logger = logging.getLogger(__name__)
console = logging.StreamHandler()
logger.addHandler(console)
logger.setLevel(logging.INFO)


class door:
    id = None
    prize = None
    isOpen = False
    markedGuessed = False

class prize(Enum):
    win = 'CAR!'
    bust = 'GOAT'

def get_prize_doors(total_doors=3, prize_doors=1):
    doors = {}
    for i in range(total_doors):
        doors.update({i: prize.bust})
    while list(doors.values()).count(prize.win) < prize_doors:
        doors[random.choice(range(len(doors)))] = random.choice([prize.win, prize.bust])
    return doors

def setup_doors(total_doors=3, prize_doors=1):
    doors = []
    prize_doors = get_prize_doors(total_doors=total_doors, prize_doors=prize_doors)
    for i in range(total_doors):
        d = door()
        d.id = i
        d.prize = prize_doors[i]
        doors.append(d)
    return doors

def make_guesses(doors, guesses=1):
    marked_guessed = 0
    while marked_guessed < guesses:
        door = random.choice(doors)
        if not door.markedGuessed:
            door.markedGuessed = True
            marked_guessed += 1
    return doors

# def open_losing_door(doors, guessed):
#     doors[random.choice([x for x in list(doors) if doors[x] is not statuses.win and x is not guessed])] = statuses.open
#     return doors

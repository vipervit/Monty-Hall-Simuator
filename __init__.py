import logging
import random
from enum import Enum


logger = logging.getLogger(__name__)
console = logging.StreamHandler()
logger.addHandler(console)
logger.setLevel(logging.INFO)


class statuses(Enum):
    win = 'CAR'
    loss = 'goat'
    open = 'open'
    guessed = 'guessed'

def setup_doors(num_of_doors=3):
    doors = {}
    for i in range(num_of_doors):
        doors.update({i: statuses.loss})
    doors[random.choice(list(doors))] = statuses.win
    return doors

def make_guess(doors):
    doors[random.choice(list(doors))] = statuses.guessed
    return doors

def open_losing_door(doors, guessed):
    doors[random.choice([x for x in list(doors) if doors[x] is not statuses.win and x is not guessed])] = statuses.open
    return doors

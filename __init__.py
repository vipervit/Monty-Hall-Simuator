import logging
from enum import Enum, IntEnum

logger = logging.getLogger(__name__)
console = logging.StreamHandler()
logger.addHandler(console)
logger.setLevel(logging.INFO)

class original(IntEnum):
    total = 3
    prized = 1
    toguess = 1
    toopen = 1

class prize(Enum):
    win = 'CAR!'
    bust = 'GOAT'

class params:
    total = original.total
    prized = original.prized
    guess = original.toguess
    open = original.toopen
    always_switch = False
    plays = 10000

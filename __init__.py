import logging
from enum import Enum

logger = logging.getLogger(__name__)
console = logging.StreamHandler()
logger.addHandler(console)
logger.setLevel(logging.INFO)

class prize(Enum):
    win = 'CAR!'
    bust = 'GOAT'

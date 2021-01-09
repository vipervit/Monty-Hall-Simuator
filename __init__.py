
from enum import Enum

class door:

    def __init__(self):
        self._id = None
        self._prize = None
        self._isOpen = False
        self._isGuessed = False

    def isSet(self):
        if self._id is not None or self._prize is not None:
            return True
        else:
            return False

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = val

    def hasPrize(self):
        if self._prize == prize.win:
            return True
        else:
            return False

    @property
    def prize(self):
        return self._prize

    @prize.setter
    def prize(self, val):
        self._prize = val

    def open(self):
        self._isOpen = True

    def isOpen(self):
        return self._isOpen

    def markGuessed(self):
        self._isGuessed = True

    def isGuessed(self):
        return self._isGuessed


class prize(Enum):
    win = 'CAR!'
    bust = 'GOAT'

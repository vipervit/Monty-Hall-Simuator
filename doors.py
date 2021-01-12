import random
import montyhall
from montyhall import door, prize, default_counts

class doors:

    def __init__(self):
        self._list = []
        self._total = default_counts.total
        self._prized = default_counts.prized
        self._guessed = default_counts.guessed
        self._revealed = default_counts.revealed

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, val):
        self._total = val

    @property
    def prized(self):
        return self._prized

    @prized.setter
    def prized(self, val):
        self._prized = val

    @property
    def guessed(self):
        return self._guessed

    @guessed.setter
    def guessed(self, val):
        self._guessed = val

    @property
    def revealed(self):
        return self._revealed

    @revealed.setter
    def revealed(self, val):
        self._revealed = val

    def setup(self):
        for i in range(self.total):
            dr = door()
            dr.id = i
            dr.hasPrize = False
            self._list.append(dr)
        self.__set_prized__()

    def __set_prized__(self):
        for i in range(self.prized):
            random.choice(self._list).hasPrize = prize.win

    def get_random_guessed(self):
        while True:
            door = random.choice(self._list)
            if door.isGuessed():
                return door

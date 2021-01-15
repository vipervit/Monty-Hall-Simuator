import random
from enum import IntEnum
import montyhall
from montyhall import prize
from montyhall.door import door

class original(IntEnum):
    total = 3
    prized = 1
    toguess = 1
    toopen = 1

class doors:

    def __init__(self):
        self._list = []
        self._total = original.total
        self._prized = original.prized

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

    def __open__(self, to_open):
        counter = 0
        while counter < to_open:
            door = random.choice(self._list)
            if not door.is_open and not door.hasPrize() and not door.is_guessed:
                door.is_open = True
                counter += 1

    def setup(self):
        for i in range(self._total):
            dr = door()
            dr.id = i
            self._list.append(dr)
        self.set_prized()

    def set_prized(self):
        counter = 0
        while counter < self._prized:
            door = random.choice(self._list)
            if not door.hasPrize():
                door.hides = prize.win
                counter += 1

    def get_random_guessed(self):
        while True:
            door = random.choice(self._list)
            if door.is_guessed:
                return door.id

    def get_ids_all(self):
        return [door.id for door in self._list]

    def get_ids_all_not_guessed(self):
        return [door.id for door in self._list if not door.is_guessed]

    def total_count(self):
        return len(self._list)

    def prized_count(self):
        return len([door for door in self._list if door.hasPrize()])

    def opened_count(self):
        return len([door for door in self._list if door.is_open])

    def guessed_count(self):
        return len([door for door in self._list if door.is_guessed])

    def get_ids_all_switchable(self):
        return [door.id for door in self._list if not door.is_open and not door.is_guessed]

    def switch_guesses(self, choices):
        counter = 0
        while counter < self.guessed_count():
            new = self.objlist()[random.choice(choices)].id
            old = self.get_random_guessed()
            switchable = [door.id for door in self.objlist() if not door.is_open and not door.is_guessed and not new == old]
            if new in switchable:
                self.objlist()[new].is_guessed = True
                self.objlist()[old].is_guessed = False
                counter += 1

    def set_guessed(self, idlist):
        for id in idlist:
            self._list[id].is_guessed = True

    def objlist(self):
        return self._list

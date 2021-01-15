import random
from enum import IntEnum
import montyhall
from montyhall import logger, prize
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

    def __setup__(self):
        for i in range(self._total):
            dr = door()
            dr.id = i
            self._list.append(dr)
        self.__set_prized__()

    def __set_prized__(self):
        counter = 0
        while counter < self._prized:
            door = random.choice(self._list)
            if not door.hasPrize():
                door.hides = prize.win
                counter += 1
        logger.debug(__name__ + '.__set_prized__: ' + str(self.__get_all_prized__()))

    def __get_all_prized__(self):
        return [door.id for door in self._list if door.hasPrize()]

    def __get_all_guessed_correctly__(self):
        return [door.id for door in self.__objlist__() if door.is_guessed and door.hasPrize()]

    def __get_all_not_guessed_correctly__(self):
        return [door.id for door in self.__objlist__() if door.is_guessed and not door.hasPrize()]

    def __set_guessed__(self, idlist):
        self.__reset_guessed__()
        for id in idlist:
            self._list[id].is_guessed = True
        logger.debug(__name__ + '__set_guessed__: ' + str(self.get_all_guessed()))
        logger.debug(__name__ + '__set_guessed__: winning guesses' + str(self.__get_all_guessed_correctly__()))
        logger.debug(__name__ + '__set_guessed__: losing guesses' + str(self.__get_all_not_guessed_correctly__()))

    def __reset_guessed__(self):
        for each in self._list:
            each.is_guessed = False

    def __objlist__(self):
        return self._list

    def get_random_guessed(self):
        while True:
            door = random.choice(self._list)
            if door.is_guessed:
                return door.id

    def get_all(self):
        return [door.id for door in self._list]

    def get_all_guessed(self):
        return [door.id for door in self._list if door.is_guessed]

    def get_all_not_guessed(self):
        return [door.id for door in self._list if not door.is_guessed]

    def get_all_switchable(self):
        switchable = [door.id for door in self._list if not door.is_open and not door.is_guessed]
        logger.debug(__name__ + '.get_all_switchable ' + str(switchable))
        return switchable

    def total_count(self):
        return len(self._list)

    def prized_count(self):
        return len([door for door in self._list if door.hasPrize()])

    def opened_count(self):
        return len([door for door in self._list if door.is_open])

    def guessed_count(self):
        return len([door for door in self._list if door.is_guessed])

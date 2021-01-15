import random
import montyhall
from montyhall import logger
from montyhall.doors import original



class player:

    def __init__(self):
        self._toguess = original.toguess
        self._guessrandomly = True
        self._guesslist = []
        self._doorlist = None

    @property
    def total_doors_to_guess(self):
        return self._toguess

    @total_doors_to_guess.setter
    def total_doors_to_guess(self, val):
        self._toguess = val

    @property
    def guess_randomly(self):
        return self._guessrandomly

    @guess_randomly.setter
    def guess_randomly(self, val):
        self._guessrandomly = val

    @property
    def guesses(self):
        self._guesslist.sort()
        return self._guesslist

    @guesses.setter
    def guesses(self, val):
        if not self._guessrandomly:
            self._guesslist = val
        else:
            raise 'Unable to assign guesses: random guesses mode is set to True. '

    @property
    def doorlist(self):
        return self._doorlist

    @doorlist.setter
    def doorlist(self, val):
        self._doorlist = val

    def __reset_guesses__(self):
        self._guesslist.clear()

    def make_guesses(self):
        counter = 0
        self.__reset_guesses__()
        if self.guess_randomly:
            while counter < self.total_doors_to_guess:
                choice = random.choice(self.doorlist)
                if not choice in self.guesses:
                    self.guesses.append(choice)
                    counter += 1
        logger.debug(__name__ + '.make_guesses: ' + str(self.guesses))

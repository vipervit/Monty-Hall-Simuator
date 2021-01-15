import random
import montyhall
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
    def guess_list(self):
        return self._guesslist

    @guess_list.setter
    def guess_list(self, val):
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

    def make_guesses(self):
        if self._guessrandomly:
            counter = 0
            while counter < self._toguess:
                choice = random.choice(self._doorlist)
                if not choice in self._guesslist:
                    self._guesslist.append(choice)
                    counter += 1

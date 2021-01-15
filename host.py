import montyhall
from montyhall import logger
from montyhall.doors import doors, original

class host:

    def __init__(self):
        self._toopen = None
        self.doors = doors()

    @property
    def total_doors_to_open(self):
        return self._toopen

    @total_doors_to_open.setter
    def total_doors_to_open(self, val):
        self._toopen = val

    def setup_doors(self):
        self.doors.__setup__()

    def open_doors(self):
        self.doors.__open__(self._toopen)

    def accept_guesses(self, guesses):
        self.doors.__set_guessed__(guesses)

    def won_guesses_count(self):
        count = len(self.doors.__get_all_guessed_correctly__())
        logger.debug(__name__ + '.won_guesses_count: ' + str(count))
        return count

    def lost_guesses_count(self):
        count = len(self.doors.__get_all_not_guessed_correctly__())
        logger.debug(__name__ + '.lost_guesses_count: ' + str(count))
        return count

    def win_rate(self):
        return self.won_guesses_count() / self.doors.prized_count()

    def loss_rate(self):
        return self.lost_guesses_count() / self.doors.prized_count()

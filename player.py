import montyhall
from doors import doors

class player:

    def __init__(self):
        self._doors

    @property
    def guess_count(self):
        return len([door for door in self._doors if door.isGuessed()])

    def get_doors(self, val):
        self._doors = val

    def make_guesses(self, guesses_to_make):
        while self.guess_count < guesses_to_make:
            door = random.choice(self._doors)
            if not door.isGuessed():
                door.markGuessed()

    def switch_guesses(self):
        switched_cnt = 0
        while switched_cnt < self.guess_count:
            new = random.choice(doors)
            old = self._doors.get_random_guessed()
            switchable = [door.id for door in doors if not door.isOpen() and not door.isGuessed() and not new is old]
            if new.id in switchable:
                new.markGuessed()
                old.unGuess()
                switched_cnt += 1
        return doors

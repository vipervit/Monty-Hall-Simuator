from montyhall.doors import prize

class door:

    def __init__(self):
        self._id = None
        self._hides = prize.bust
        self._isOpen = False
        self._isGuessed = False

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = val

    @property
    def hides(self):
        return self._hides

    @hides.setter
    def hides(self, val):
        self._hides = val

    @property
    def is_open(self):
        return self._isOpen

    @is_open.setter
    def is_open(self, val):
        self._isOpen = val

    @property
    def is_guessed(self):
        return self._isGuessed

    @is_guessed.setter
    def is_guessed(self, val):
        self._isGuessed = val

    def hasPrize(self):
        if self._hides == prize.win:
            return True
        else:
            return False

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

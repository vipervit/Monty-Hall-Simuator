import montyhall
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

    def open_doors(self):
        self.doors.__open__(self._toopen)

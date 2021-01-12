import montyhall
from montyhall import default_counts
from doors import doors

class host:

    def __init__(self):
        self.doors = doors()

    def setup_doors(self, total=default_counts.total, prized=default_counts.prized):
        self.doors.total = total
        self.doors.prized = prized
        self.doors.setup()

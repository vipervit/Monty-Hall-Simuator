from montyhall.doors import doors, original

class TestDoors:

    total = 10
    prized = 5
    toguess = 2

    x = doors()

    def test_setup(self):
        assert self.x.total == original.total
        assert self.x.prized == original.prized
        self.x.total = self.total
        self.x.prized = self.prized
        assert self.x.total == self.total
        assert self.x.prized == self.prized
        self.x.__setup__()
        assert self.x.total == self.total
        assert self.x.prized == self.prized
        assert self.x.total_count() == self.total
        assert self.x.prized_count() == self.prized

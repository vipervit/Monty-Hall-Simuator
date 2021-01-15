from montyhall.doors import doors, original

class TestDoors:

    total = 10
    prized = 5

    x = doors()

    def test_setup(self):
        assert self.x.total == original.total
        assert self.x.prized == original.prized
        self.x.total = self.total
        self.x.prized = self.prized
        assert self.x.total == self.total
        assert self.x.prized == self.prized
        self.x.setup()
        assert self.x.total == self.total
        assert self.x.prized == self.prized
        assert len(self.x.objlist()) == self.total
        assert len([door for door in self.x.objlist() if door.hasPrize]) == self.prized


    def test_set_guessed(self):
        pass

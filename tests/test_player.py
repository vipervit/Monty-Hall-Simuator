from montyhall.player import player
from montyhall.doors import doors

def test_make_guesses():
    drs = doors()
    drs.total = 10
    drs.setup()
    p = player()
    p.total_doors_to_guess = 4
    p.doorlist = drs.get_ids_all()
    p.make_guesses()
    assert len(p.guess_list) == p.total_doors_to_guess

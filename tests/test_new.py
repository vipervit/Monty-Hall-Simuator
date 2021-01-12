import random
from montyhall import default_counts
from montyhall.doors import doors

max_total = 10
max_prized = total_max - 1
max_guessed = total_max - 1
max_revealed = total_max - 1
max_iteration = 10000

class Test_Doors:

    def test_doors_setup_default(self):
        drs = doors()
        assert drs.total == default_counts.total, 'Wrong count of total.'
        assert drs.prized == default_counts.prized, 'Wrong count of prized.'
        assert drs.guessed == default_counts.guessed, 'Wrong count of guessed.'
        assert drs.revealed == default_counts.revealed, 'Wrong count of revealed.'

    def test_doors_setup_custom(self):
        total = random.randint(default_counts.total, max_total)
        prized = random.randint(1, max_prized)
        guessed = random.randint(1, max_guessed)
        revealed = random.randint(1, max_revealed)
        drs = doors(total, prized, guessed, revealed)
        cnt_win, cnt_loss, cnt_prize, cnt_guess, cnt_revealed = 0, 0, 0, 0, 0
        for i in range(max_iterations):
            if random.choice(doors).prize == prize.win:
                cnt_win += 1


            else:
                loss_counter += 1
                assert round(win_counter / iterations, precision) == round(doors_prize / doors_total, precision), 'Wrong statistics for winnning doors.'
                assert round(loss_counter / iterations, precision) == round((doors_total - doors_prize) / doors_total, precision), 'Wrong statistics for losing doors.'

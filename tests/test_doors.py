import montyhall
from montyhall import statuses, setup_doors, make_guess

def test_setup_doors():
    iterations = 100000
    win_counter, loss_counter = 0, 0
    for i in range(iterations):
        doors = setup_doors()
        if doors[0] == statuses.win:
            win_counter += 1
        if doors[0] == statuses.loss:
            loss_counter += 1
    win_rate = round(win_counter/iterations,2)
    loss_rate = round(loss_counter/iterations,2)
    assert win_rate >= 0.32 and win_rate <= 0.34, 'Wrong statistics for winnning doors.'
    assert  loss_rate >= 0.66 and loss_rate <= 0.68, 'Wrong statistics for losing doors.'

def test_make_guess():
    iterations = 100000
    ct_1, ct_2, ct_3 = 0,0,0
    for i in range(iterations):
        doors = make_guess(setup_doors())
        if doors[0] == statuses.guessed:
            ct_1 += 1
        if doors[1] == statuses.guessed:
            ct_2 += 1
        if doors[2] == statuses.guessed:
            ct_3 += 1
        rate1 = round(ct_1/iterations)
        rate2 = round(ct_2/iterations)
        rate3 = round(ct_3/iterations)
        assert rate1 >= 0.32 and rate1 <= 0.33, 'Wrong statistics for first door.'
        assert rate2 >= 0.32 and rate2 <= 0.33, 'Wrong statistics for second door.'
        assert rate3 >= 0.32 and rate3 <= 0.33, 'Wrong statistics for third door.'

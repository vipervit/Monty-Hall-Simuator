import montyhall
from montyhall import statuses, setup_doors, num_of_doors

def test_setup_doors():
    iterations = 100000
    win_counter, loss_counter = 0, 0
    for i in range(iterations):
        doors = setup_doors(num_of_doors)
        if doors[0] == statuses.win:
            win_counter += 1
        if doors[0] == statuses.loss:
            loss_counter += 1
    win_rate = round(win_counter/iterations,2)
    loss_rate = round(loss_counter/iterations,2)
    assert win_rate >= 0.32 and win_rate <= 0.34, 'Wrong statistics for winnning doors.'
    assert  loss_rate >= 0.66 and loss_rate <= 0.68, 'Wrong statistics for losing doors.'

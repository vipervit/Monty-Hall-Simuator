"""
Monty Hall problem simulator. Parameters:
-s <true/false>: always switch door / never swtich door
-i <number of iterations>: number of iterations
-n <number of doors> : number of doors (3 by default if omitted, as in the original problem description)
-p <number of prize doors>: number of doors behind which there is a prize
-g <number of guesses>: number of doors the player may guess (1 in the original description)
-h: prints help and quits
"""
import sys
import logging
import getopt
import random
import montyhall
from montyhall import logger
from montyhall.doors import original
from montyhall.host import host
from montyhall.player import player

def exec(always_switch, iterations, total, with_prize, to_guess, to_open):

    win_counter, loss_counter = 0, 0

    for i in range(iterations+1):

        _host = host()
        _player = player()

        _host.doors.total = total
        _host.doors.prized = with_prize
        _host.total_doors_to_open = to_open
        _host.doors.setup()

        _player.total_doors_to_guess = to_guess
        _player.doorlist = _host.doors.get_ids_all()
        _player.make_guesses()
        _host.doors.set_guessed(_player.guess_list)

        _host.open_doors()

        if always_switch == 'True':
            _player.doorlist = _host.doors.get_ids_all_switchable()
            _player.make_guesses()
            _host.doors.switch_guesses(_player.guess_list)

        win_counter += len([door for door in _host.doors.objlist() if door.is_guessed and door.hasPrize])
        loss_counter +=  len([door for door in _host.doors.objlist() if door.is_guessed and not door.hasPrize])

    logger.info('Total doors: ' + str(total))
    logger.info('Prize doors: ' + str(with_prize))
    logger.info('Doors guessed: ' + str(to_guess))
    logger.info('Doors opened: ' + str(to_open))
    logger.info('Iterations: ' + str(iterations))
    logger.info('Won: ' + str(win_counter) + ' ('+ str(round(win_counter*100/iterations,2)) + '%).')
    logger.info('Lost ' + str(loss_counter) + ' ('+ str(round(loss_counter*100/iterations,2)) + '%).')
    logger.info('Always switch the door: ' + always_switch + '.')


if __name__ == '__main__':

    iterations = 10000
    total = int(original.total)
    with_prize = int(original.prized)
    to_open = int(original.toopen)
    to_guess = int(original.toguess)

    try:
       opts, args = getopt.getopt(sys.argv[1:], 'hs:i:n:p:r:g:', [])
    except getopt.GetoptError as err:
        logger.error(err)
        logger.info(__doc__)
        sys.exit(2)
    for opt, args in opts:
        if opt == '-s':
            if args != 'True' and args != 'False':
                logger.critical('Can accept only True or False for -s.')
                sys.exit()
            always_switch = args
        if opt == '-i':
            iterations = int(args)
        if opt == '-n':
            total = int(args)
        if opt == '-g':
            to_guess = int(args)
        if opt == '-r':
            to_open = int(args)
        if opt == '-p':
            with_prize = int(args)
        if opt == '-h':
            logger.critical(__doc__)
            sys.exit()
    if total - with_prize < 2 or total - to_guess < 2 or total - to_open < 2:
        logger.critical('Total number of doors must be at least higher by 2 than number of prize doors, doors to guess, or doors to reveal.')
        sys.exit()
    exec(always_switch, iterations, total, with_prize, to_guess, to_open)

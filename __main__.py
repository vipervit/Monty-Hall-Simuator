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

        hst = host()
        plyr = player()

        hst.doors.total = total
        hst.doors.prized = with_prize
        hst.total_doors_to_open = to_open
        hst.doors.setup()

        plyr.total_doors_to_guess = to_guess
        plyr.doorlist = hst.doors.get_ids_all()
        plyr.make_guesses()
        hst.doors.set_guessed(plyr.guess_list)

        hst.open_doors()

        if always_switch == 'True':
            plyr.doorlist = hst.doors.get_ids_all_switchable()
            plyr.make_guesses()
            hst.doors.switch_guesses(plyr.guess_list)

        win_counter += len([door for door in hst.doors.objlist() if door.is_guessed and door.hasPrize])
        loss_counter +=  len([door for door in hst.doors.objlist() if door.is_guessed and not door.hasPrize])

    logger.info('Total doors: ' + str(hst.doors.total_count()))
    logger.info('Prize doors: ' + str(hst.doors.prized_count()))
    logger.info('Doors guessed: ' + str(hst.doors.guessed_count()))
    logger.info('Doors opened: ' + str(hst.doors.opened_count()))
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
       opts, args = getopt.getopt(sys.argv[1:], 'hs:i:n:p:o:g:', [])
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
        if opt == '-o':
            to_open = int(args)
        if opt == '-p':
            with_prize = int(args)
        if opt == '-h':
            logger.critical(__doc__)
            sys.exit()
    if total - with_prize < 2 or total - to_guess < 2 or total - to_open < 2 or to_guess + to_open + with_prize >= total:
        logger.critical('Total number of doors must be at least higher by 2 than number of prize doors, doors to guess, or doors to reveal.')
        logger.critical('The sum of doors to be opened, doors with prizes and doors to guess may not be higher than the total number of doors.')
        sys.exit()
    exec(always_switch, iterations, total, with_prize, to_guess, to_open)

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
import getopt
import random
import montyhall
from montyhall import *
from montyhall.funcs import *

def exec(always_switch, iterations, doors_total=DOORS_TOTAL_STANDARD, doors_prize=DOORS_PRIZE_STANDARD, doors_guess=DOORS_GUESS_STANDARD, doors_reveal=DOORS_REVEAL_STANDARD):
    win_counter, loss_counter = 0, 0
    doors = {}
    for i in range(iterations+1):
        doors = prepare_doors(doors_total, doors_prize, doors_guess, doors_reveal)
        if always_switch == 'True':
            doors = switch_guesses(doors)
        win_counter += len([door for door in doors if door.isGuessed() and door.hasPrize()])
        loss_counter +=  len([door for door in doors if door.isGuessed() and not door.hasPrize()])
    logger.info('Total doors: ' + str(doors_total))
    logger.info('Prize doors: ' + str(doors_prize))
    logger.info('Doors guessed: ' + str(doors_guess))
    logger.info('Doors revealed: ' + str(doors_reveal))
    logger.info('Iterations: ' + str(iterations))
    logger.info('Won: ' + str(win_counter) + ' ('+ str(round(win_counter*100/iterations,2)) + '%).')
    logger.info('Lost ' + str(loss_counter) + ' ('+ str(round(loss_counter*100/iterations,2)) + '%).')
    logger.info('Always switch the door: ' + always_switch + '.')


if __name__ == '__main__':
    doors_total =  defaults.DOORS_TOTAL_STANDARD
    doors_prize =  defaults.DOORS_PRIZE_STANDARD
    doors_guess =  defaults.DOORS_GUESS_STANDARD
    doors_reveal = default.DOORS_REVEAL_STANDARD
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
            doors_total = int(args)
        if opt == '-g':
            doors_guess = int(args)
        if opt == '-r':
            doors_reveal = int(args)
        if opt == '-p':
            doors_prize = int(args)
        if opt == '-h':
            logger.critical(__doc__)
            sys.exit()
    if doors_total - doors_prize < 2 or doors_total - doors_guess < 2 or doors_total - doors_reveal < 2:
        logger.critical('Total number of doors must be at least higher by 2 than number of prize doors, doors to guess, or doors to reveal.')
        sys.exit()
    exec(always_switch, iterations, doors_total, doors_prize, doors_guess, doors_reveal)

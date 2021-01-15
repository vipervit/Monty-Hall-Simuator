"""
Monty Hall problem simulator. Parameters:
-s <true/false>: always switch door / never swtich door
-i <number of plays>: number of plays
-n <number of doors> : number of doors (3 by default if omitted, as in the original problem description)
-p <number of prize doors>: number of doors behind which there is a prize
-g <number of guesses>: number of doors the player may guess (1 in the original description)
-d: debug mode
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

def exec(always_switch, plays, total, with_prize, to_guess, to_open):

    win_counter, loss_counter = 0, 0
    win_rates, loss_rates = [], []

    for i in range(plays):

        hst = host()
        plyr = player()

        hst.doors.total = total
        hst.doors.prized = with_prize
        hst.total_doors_to_open = to_open
        hst.setup_doors()

        plyr.doorlist = hst.doors.get_all()
        plyr.total_doors_to_guess = to_guess
        plyr.make_guesses()
        guesses = plyr.guesses

        hst.accept_guesses(guesses)
        hst.open_doors()

        if always_switch == 'True':

            plyr.doorlist = hst.doors.get_all_switchable()
            plyr.make_guesses()
            new_guesses = plyr.guesses

            hst.accept_guesses(new_guesses)

        win_counter += hst.won_guesses_count()
        win_rates.append(hst.win_rate())
        loss_counter +=  hst.lost_guesses_count()
        loss_rates.append(hst.loss_rate())

    win_rate = round(sum(win_rates) / len(win_rates),2) * 100
    loss_rate = round(sum(loss_rates) / len(loss_rates),2) * 100

    logger.info('Total doors per play: ' + str(hst.doors.total_count()))
    logger.info('Prize doors per play: ' + str(hst.doors.prized_count()))
    logger.info('Doors guessed per play: ' + str(hst.doors.guessed_count()))
    logger.info('Doors opened per play: ' + str(hst.doors.opened_count()))
    logger.info('Plays: ' + str(plays))
    logger.info('Total prizes available: ' + str(with_prize * plays))
    logger.info('Total prizes won : %s', str(win_counter))
    logger.info('Win rate: ' + str(win_rate))
    logger.debug('Total prizes lost: %s', str(loss_counter))
    logger.debug('Loss rate: ' + str(loss_rate))
    logger.info('Always switch the door: ' + always_switch + '.')


if __name__ == '__main__':

    plays = 10000
    total = int(original.total)
    with_prize = int(original.prized)
    to_open = int(original.toopen)
    to_guess = int(original.toguess)

    try:
       opts, args = getopt.getopt(sys.argv[1:], 'dhs:i:n:p:o:g:', [])
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
            plays = int(args)
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
        if opt == '-d':
            logger.setLevel(logging.DEBUG)
    if not total==original.total and not to_guess==original.toguess and not with_prize==original.prized and not to_open==original.toopen \
           and total < 2 * to_guess + to_open + with_prize:
        logger.critical('ERROR')
        sys.exit()
    exec(always_switch, plays, total, with_prize, to_guess, to_open)

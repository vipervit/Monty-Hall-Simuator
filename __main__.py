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
from enum import IntEnum
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import montyhall
from montyhall import logger, params
from montyhall.doors import original
from montyhall.host import host
from montyhall.player import player

def plot(data):
    pd.Series(data).plot(kind='barh')
    plt.show()

def exec(params):

    wins, losses = counts_init(params.plays), counts_init(params.plays)
    win_counter, loss_counter = 0, 0
    win_rates, loss_rates = [], []

    for i in range(params.plays):

        hst = host()
        plyr = player()

        hst.doors.total = params.total
        hst.doors.prized = params.prized
        hst.total_doors_to_open = params.open
        hst.setup_doors()

        plyr.doorlist = hst.doors.get_all()
        plyr.total_doors_to_guess = params.guess
        plyr.make_guesses()
        guesses = plyr.guesses

        hst.accept_guesses(guesses)
        hst.open_doors()

        if params.always_switch == 'True':

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
    logger.info('Plays: ' + str(params.plays))
    logger.info('Total prizes available: ' + str(params.prized * params.plays))
    logger.info('Total prizes won : %s', str(win_counter))
    logger.info('Win rate: ' + str(win_rate))
    logger.debug('Total prizes lost: %s', str(loss_counter))
    logger.debug('Loss rate: ' + str(loss_rate))
    logger.info('Always switch the door: ' + str(params.always_switch) + '.')

    plot({'Wins': win_counter, 'Losses': loss_counter})

if __name__ == '__main__':

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
            params.always_switch = args
        if opt == '-i':
            params.plays = int(args)
        if opt == '-n':
            params.total = int(args)
        if opt == '-g':
            params.guess = int(args)
        if opt == '-o':
            params.open = int(args)
        if opt == '-p':
            params.prized = int(args)
        if opt == '-h':
            logger.critical(__doc__)
            sys.exit()
        if opt == '-d':
            logger.setLevel(logging.DEBUG)

    exec(params)

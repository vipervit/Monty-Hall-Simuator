"""
Monty Hall problem simulator. Parameters:
-s <true/false>: always switch door / never swtich door
-i <number of iterations>: number of iterations
-n <number of doors> : number of doors (3 by default if omitted, as in the original problem description)
-h: prints this and quits
"""
import sys
import getopt
import logging
import random
import montyhall

def exec(always_switch, iterations, num_of_doors):
    win_counter, loss_counter = 0, 0
    doors = {}
    for i in range(iterations+1):
        # assign random winning door
        doors = setup_doors(num_of_doors)
        # make a guess
        doors = make_guess(doors)
        # open a losing door
        doors = open_losing_door(doors)
        if always_switch:
            guessed = [door for door in doors if door is not guessed and doors[door] is not open][0]
        if doors[guessed] == win:
            win_counter += 1
        else:
            loss_counter += 1
    logger.info('Won: ' + str(win_counter) + ' ('+ str(round(win_counter*100/iterations,2)) + '%).')
    logger.info('Lost ' + str(loss_counter) + ' ('+ str(round(loss_counter*100/iterations,2)) + '%).')
    logger.info('Always switched the door: ' + always_switch + '.')


if __name__ == '__main__':
    try:
       opts, args = getopt.getopt(sys.argv[1:], 'hs:i:n:', [])
    except getopt.GetoptError as err:
        logger.error(err)
        logger.info(__doc__)
        sys.exit(2)
    for opt, args in opts:
        if opt == '-s':
            always_switch = args
        if opt == '-i':
            iterations = int(args)
        if opt == '-n':
            num_of_doors = int(args)
        if opt == '-h':
            logger.critical(__doc__)
            sys.exit()
    exec(always_switch, iterations, num_of_doors)

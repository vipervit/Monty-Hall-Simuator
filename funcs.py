import random
from montyhall import door, prize

def get_prize_doors(total_doors=3, prize_doors=1):
    doors = {}
    for i in range(total_doors):
        doors.update({i: prize.bust})
    while list(doors.values()).count(prize.win) < prize_doors:
        doors[random.choice(range(len(doors)))] = random.choice([prize.win, prize.bust])
    return doors

def setup_doors(total_doors=3, prize_doors=1):
    doors = []
    prize_doors = get_prize_doors(total_doors=total_doors, prize_doors=prize_doors)
    for i in range(total_doors):
        d = door()
        d.id = i
        d.prize = prize_doors[i]
        doors.append(d)
    return doors

def make_guesses(doors, guesses=1):
    marked_guessed = 0
    while marked_guessed < guesses:
        door = random.choice(doors)
        if not door.isGuessed():
            door.markGuessed()
            marked_guessed += 1
    return doors

def open_losing_doors(doors, total_doors_to_open=1):
    open_doors_count = 0
    while open_doors_count < total_doors_to_open:
        door = random.choice(doors)
        if not door.isOpen() and not door.hasPrize():
            door.open()
            open_doors_count += 1
    return doors

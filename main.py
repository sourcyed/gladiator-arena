from battleground import Battleground
from gladiator import Gladiator
from ui import UI
from string import ascii_uppercase
from time import sleep
import os
import sys
import random

space_length = 6

gladiator_count = 5

arena_size = 10

game_count = 10

try:
    if (len(sys.argv) == 4):
        gladiator_count = int(sys.argv[1])
        arena_size = int(sys.argv[2])
        game_count = int(sys.argv[3])
except Exception as e:
    print(e)
    print("Invalied arguments. Default parameters will be set.")
    sleep(2)

ui = UI(space_length)

for i in range(game_count):
    battleground = Battleground(arena_size, arena_size)

    gladiators = []

    for i in range(gladiator_count):
        gladiators.append(Gladiator(battleground,ascii_uppercase[i],random.randint(1,3),random.randint(1,5),100))

    while True:
        os.system("cls")

        for gladiator in gladiators:
            if gladiator in battleground.gladiators:
                if len(battleground.gladiators) > 1:
                    gladiator.play()

        ui.show_matrix(battleground.get_matrix())

        sleep(0.5)

        if battleground.end:
            break

    for winner in battleground.gladiators:
        print("Winner: " + winner.name)
        if len(battleground.gladiators) > 1:
            print("     ", winner.find_nearest())
    
    sleep(1)
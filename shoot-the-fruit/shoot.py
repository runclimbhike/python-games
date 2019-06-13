# Date: 2019-06-13
# more comments to make a commit

# IMPORTS
from pgzrun import *
import pgzrun
from random import randint

# VARIABLES
apple = Actor("apple")


def draw():
    screen.clear()
    apple.draw()


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 800)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()


place_apple()


pgzrun.go()

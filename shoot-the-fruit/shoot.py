# Date: 2019-06-13
# more comments to make a commit

# IMPORTS
import pgzrun
from random import randint

# VARIABLES
apple = Actor("apple")


def draw():
    screen.clear()
    apple.draw()


def place_apple():
    apple.x = randint(20, 600)
    apple.y = randint(20, 600)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()


place_apple()


pgzrun.go()

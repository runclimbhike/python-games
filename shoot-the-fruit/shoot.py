# Date: 2019-06-13
# more comments to make a commit

from pgzrun import *
import pgzrun

apple = Actor("apple")


def draw():
    screen.clear()
    apple.draw()


def place_apple():
    apple.x = 300
    apple.y = 200


place_apple()


pgzrun.go()

# Date: 2019-06-13

from pgzrun import *
import pgzrun

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

pgzrun.go()


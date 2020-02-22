import random
import time
import turtle


def random_colour():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue


window = turtle.Screen()
bob = turtle.Turtle()
bob.color(random_colour())
bob.forward(100)
window.mainloop()

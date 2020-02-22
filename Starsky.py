import random
import turtle


def starfill(side_num, length):
    joe.right(random.randint(10, 350))
    joe.begin_fill()
    if side_num % 2 != 0:
        for side in range(side_num):
            joe.forward(length)
            angle = side_num // 2 * 360 / side_num
            joe.right(angle)
    joe.end_fill()


window = turtle.Screen()
window.bgcolor('blue')
window.setup(700, 500)

joe = turtle.Turtle()
joe.speed(0)
joe.color('yellow')
joe.hideturtle()


def move(x, y):
    joe.up()
    joe.setposition(x, y)
    joe.down()
    size = random.randint(10, 20)
    top_num = random.choice([5, 7, 9])
    starfill(top_num, size)


window.onclick(move)
window.listen()
window.mainloop()

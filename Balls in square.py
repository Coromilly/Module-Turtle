import random
import turtle

window = turtle.Screen()
border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('red')
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)

balls = []
count = 10

for nums in range(count):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.shape('circle')
    ball.up()
    randx = random.randint(-290, 290)
    randy = random.randint(-290, 290)
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red, green, blue)
    ball.goto(randx, randy)
    ball.showturtle()
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    balls.append([ball, dx, dy])

while True:
    for ball in range(count):
        # balls[ball][0] - мяч
        # balls[ball][0] - dx
        # balls[ball][0] - dy
        x, y = balls[ball][0].position()
        if x + balls[ball][1] >= 300 or x + balls[ball][1] <= -300:
            balls[ball][1] = -balls[ball][1]
        if y + balls[ball][2] >= 300 or y + balls[ball][2] <= -300:
            balls[ball][2] = -balls[ball][2]
        balls[ball][0].goto(x + balls[ball][1], y + balls[ball][2])

window.mainloop()

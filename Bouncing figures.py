import random
import turtle

window = turtle.Screen()
window.bgcolor('red')
window.tracer(20)

border = turtle.Turtle()
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.goto(-250, 250)
border.down()
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250, 250)

balls = []
count = 50
forms = ['circle', 'square', 'triangle', 'turtle']

for i in range(count):
    ball = turtle.Turtle(shape=random.choice(forms))
    ball.hideturtle()
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red, green, blue)
    ball.up()
    ball.goto(random.randint(-200, 200), random.randint(100, 300))
    ball.showturtle()
    ball.speed_y = 0
    ball.speed_x = random.randint(-3, 3)
    ball.angle = random.randint(-5, 5)
    ball.gravity = random.randint(1, 30) * 0.1
    balls.append(ball)


while True:
    window.update()
    for ball in balls:
        ball.left(ball.angle)
        ball.speed_y = ball.speed_y - ball.gravity
        ball.goto(ball.xcor() + ball.speed_x, ball.ycor() + ball.speed_y)

        if ball.ycor() <= -250:
            ball.sety(-250)
            ball.speed_y = - ball.speed_y
        if ball.xcor() >= 250 or ball.xcor() <= -250:
            ball.speed_x = - ball.speed_x


window.mainloop()
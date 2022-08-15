import turtle
import winsound
from time import sleep

wn = turtle.Screen()
wn.title("Pong Py")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    paddle_a.sety(y+20)


def paddle_a_down():
    y = paddle_a.ycor()
    paddle_a.sety(y-20)


def paddle_b_up():
    y = paddle_b.ycor()
    paddle_b.sety(y+20)


def paddle_b_down():
    y = paddle_b.ycor()
    paddle_b.sety(y-20)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Reflect the ball
    if ball.xcor() >= 390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() <= -390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.ycor() >= 290:
        ball.dy = -ball.dy
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        sleep(0.05)
    if ball.ycor() <= -290:
        ball.dy = -ball.dy
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        sleep(0.05)
    # Paddle and ball collisions
    if (360 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        sleep(0.05)

    if (-340 > ball.xcor() > -360) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        sleep(0.05)

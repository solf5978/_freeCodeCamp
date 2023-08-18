import turtle

# Create A Window Application
wn = turtle.Screen()
wn.title("Simple Ping Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# Prevent Windows Session From Auto-Refreshing
wn.tracer(0)

# Paddle A Gameer
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color("lightgreen")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B Gamer
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color("coral")
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("lightblue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Turtle Pen For Scoring
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Wokring Part
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "S")
wn.onkeypress(paddle_b_up, "I")
wn.onkeypress(paddle_b_down, "K")

while True:
    wn.update()

    # Moving The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy = ball.dy * -1

    elif ball.ycor() < -300:
        ball.sety(-300)
        ball.dy = ball.dy * -1


    if ball.xcor() > 350:
        score_a = score_a + 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = ball.dx * -1


    elif ball.xcor() < -350:
        score_b = score_b + 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = ball.dx * -1

    # Paddle Ball Collisions
    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx = ball.dx * -1    
    elif ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx = ball.dx * -1
    
import turtle

wn = turtle.Screen()
wn.title("Pong by Shihab")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #Stops the game from updating so speeds up game


# Score 
score_a = 0
score_b = 0

# Paddle A

paddle_a = turtle.Turtle() #Turtle object
paddle_a.speed(0) #Speed of animation no paddle itself. Sets them to maximum speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #Increases the with of the paddle
paddle_a.penup() #Turtle draws a line when moving. This stops them from doing so.
paddle_a.goto(-350, 0) #Starting position of turtle


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
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1 #Change in x coordinate so moves by 2 px
ball.dy = 1 #Change in y coordinate so moves by 2 px #moves up and diagonally

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 PLayer B: 0", align="center", font=('courier', 24, "normal"))

# Functionality (movements of the paddles)

def paddle_a_up():
    y = paddle_a.ycor() #gives the y coordinate of the paddle
    y += 20 #Adds 20 pixels to the y cordinate
    paddle_a.sety(y) #Sets y to the new y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 20 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) 

#Keyboard binding

wn.listen() #Tells to listen for key input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop

while True:
    wn.update() #updates the game everytime the loop runs

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #Adds 2 px everytime the ball moves
    ball.sety(ball.ycor() + ball.dy) #Adds 2 px everytime the ball moves

    # Border checking (top and bottom)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #Reverses the movement
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #Reverses the movement

    # Border checking (left and right)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} PLayer B: {}".format(score_a, score_b), align="center", font=('courier', 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} PLayer B: {}".format(score_a, score_b), align="center", font=('courier', 24, "normal"))
    
    # Paddle and ball collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


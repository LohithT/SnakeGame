import turtle
import time

# Score
score_a = 0
score_b = 0

#Setting up the screen, title, background color, width etc.
# must return the window created
def setUpScreen():
    # Set up the screen
    wn = turtle.Screen()
    # Set background color
    wn.bgcolor("light blue")
    # Set height and width
    wn.setup(width=800, height=600)
    # Turns off the screen updates
    wn.tracer(0)
    return wn

# Create and return the paddle
# a and b will give the position of the paddle on the screen
def createPaddle(a, b):
    paddle = turtle.Turtle()
    # Set speed, shape, color and penup
    paddle.speed(5)
    paddle.shape('square')
    paddle.color("white")
    paddle.penup()
    # move paddle to the left/right of the screen
    paddle.goto(a,b)
    # position of the paddle is given by a and b
    paddle.shapesize(5, 1)
    return paddle

# Create and return the ball
def createBall():
    ball = turtle.Turtle()
    # Set speed, shape, color and penup
    ball.speed(15)
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    # setting delta for the ball movement 
    ball.dx = 2 
    ball.dy = 2
    return ball

# Write score and highscore on the screen
# when a player will miss the ball score is given to the other player
def trackScoreOnScreen():
    pen = turtle.Turtle()
    # Set color, speed
    pen.color("white")
    pen.speed(0)
    # penup and hide turtle
    pen.penup()
    pen.hideturtle()
    # Move the score to top of screen
    pen.goto(0, 250)
    pen.write("Player A: 0  Player B: 0", align='center', font=('Freestyle Script', 35, 'bold'))
    return pen

# Function to call to move the ball automatically
# should be called from the main loop. 
def moveBall():
    # Moving Ball
    x = ball.xcor()
    y = ball.ycor()
    ball.setx(x + ball.dx)
    ball.sety(y + ball.dy)
  
# Function to be called by pressing up key 
# It will help to move paddle A in upwards to save ball from touching the border
def paddle_a_up():
    y = paddle_a.ycor()
    if (y < 300):
        y += 20
    paddle_a.sety(y)

# Function to be called by pressing 'a' key 
# It will help to move paddle B in upwards to save ball from touching the border
def paddle_b_up():
    y = paddle_b. ycor()
    if (y < 300):
        y += 20
    paddle_b.sety(y)
    
# Function to be called by pressing down key 
# It will help to move paddle A in downwards to save ball from touching the border
def paddle_a_down():
    y = paddle_a.ycor()
    if (y > -300):
        y -= 20
    paddle_a.sety(y)
   
# Function to be called by pressing 'z' key 
# It will help to move paddle B in downwards to save ball from touching the border
def paddle_b_down():
    y = paddle_b.ycor()
    if  (y > -300):
        y -= 20
    paddle_b.sety(y)
    

# Bind 'a', 'z', 'up' and 'down' keys with their function
def bindKeyboardKeys(wn):
    wn.listen()
    wn.onkeypress(paddle_a_up, 'a')
    wn.onkeypress(paddle_a_down, 'z')
    wn.onkeypress(paddle_b_up, 'Up')
    wn.onkeypress(paddle_b_down, 'Down')
    # remove print statement after implementing this function
    print("bindKeyboardKeys function called")

# detect collision of ball with the borders, 
# increment the score
# handle the bounce of the ball
def detectHandleBallCollisionWithBorders(ball, trackScore):
    global score_a
    global score_b
    
    # checking if ball touching top or bottom of the screen
    # reverse the direction of the ball wrt y axis 
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
    
    # check if ball touches right side border of the screen
    if ball.xcor() > 390:
        # reset ball at origin and move the ball
        ball.goto(0, 0)
        ball.dx *= -1
        # increment score for player A
        score_a += -1
        # update the score on the top of the screen
        trackScore.clear()
        trackScore.write("Player A: {} Player B: {}".format(score_a, score_b),align='center', font=("Freestyle Script", 35, 'bold' ))
        time.sleep(1)
        print('detect ball collision on the right side of the screen')

    # check if ball touches left side border of the screen
    if ball.xcor() < -390:
        # reset ball at origin and move the ball
        ball.goto(0, 0)
        ball.dx *= -1
        # increment score for player B
        # update the score on the top of the screen
        trackScore.clear()
        trackScore.write("Player A: {} Player B: {}".format(score_a, score_b),align='center', font=("Freestyle Script", 35, 'bold' ))
        
        time.sleep(1)
        print('detect ball collision on the left side of the screen')

    

def detectHandleBallCollisionWithPaddle(ball):
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1
  

    
######################################
#   Start of the main function     #
#                                  #
####################################

#Call Functions in main program
wn = setUpScreen()
ball = createBall()
paddle_a = createPaddle(-350, 0)
paddle_b = createPaddle(350, 0)
trackScore = trackScoreOnScreen()
bindKeyboardKeys(wn)

# Main game loop
while True:
    wn.update()

    # Moving Ball
    moveBall()

    # Border checking
    detectHandleBallCollisionWithBorders(ball, trackScore)
    
    # Paddle and ball collisions
    detectHandleBallCollisionWithPaddle(ball)
        
    time.sleep(0.01)

wn.mainloop
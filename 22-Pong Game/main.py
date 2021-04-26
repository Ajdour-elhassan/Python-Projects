from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("red")
screen.setup(width=800, height=600)
screen.title("Pong Game")

# Fix that animation
screen.tracer(0)

#  Paddle Shape
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

#  Ball shape 
ball = Ball()

screen.listen()
# Control the Right Paddle
screen.onkey(r_paddle.go_up, "a")
screen.onkey(r_paddle.go_down, "z")


# Control the left Paddle
screen.onkey(l_paddle.go_up, "d")
screen.onkey(l_paddle.go_down, "s")


Game_is_on = True

while Game_is_on :
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #  Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
 
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        
    #  Detect Right paddle  when the ball has missed
    if ball.xcor() > 380 :
        ball.rest_position()
    
    #  Detect Left paddle  when the ball has missed
    if ball.xcor() > -380 :
        ball.rest_position()
        
        
screen.exitonclick()

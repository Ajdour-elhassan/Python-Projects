from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)
    
def turn_left() :
    tim.left(45)
      
def turn_right() :
    tim.right(45)

def clear() :
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
# screen.onkey(key="space" , fun=move_forward)
screen.onkey(move_forward, 'space')
screen.onkey(move_backward , "b")
screen.onkey(turn_left, 'r')
screen.onkey(turn_right, 'l')
screen.onkey(clear, 'c')
screen.exitonclick()
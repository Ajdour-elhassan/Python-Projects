from turtle import Screen, Turtle
import random 

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.listen()
user_guess = screen.textinput(title="Make your bet ?" , prompt="whicj turtle would win a race ? choose a color!")
print(user_guess)

colors = ["red" , "orange" , "yellow" , "blue" , "green" , "purple" ]

y_position = [0, 30, -30, 60, -60, 90, -90]

all_turtles = []

for turtle_index  in range(0, 6) :
    tim = Turtle(shape="turtle") 
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-240, y=y_position[turtle_index])
    all_turtles.append(tim)
   
if user_guess :
    is_race_on = True

while is_race_on : 
    for turtle in all_turtles :
        if turtle.xcor() > 230 :
            is_race_on = False
            wining_color = turtle.pencolor()
            if  wining_color == user_guess :
                print(f"You won! , The winner is : {wining_color} ")
            else :
                print(f"You lost! , The winner is : {wining_color}")
                
        rand_race = random.randint(0, 10)
        turtle.forward(rand_race)
        
screen.exitonclick()
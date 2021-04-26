from turtle import Screen , Turtle


#  Paddle inherinted Turtle Here

class Paddle(Turtle):

    #  Attribute  Get Paramete called Position
    def __init__(self, position) :
        super().__init__()
        # paddle Shape()
        self = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        # Position()
        self.goto(position)
        
    #  Move Down Postion
    def go_up(self):
        position_y = self.ycor() + 20
        self.goto(self.xcor(), position_y)
 
    def go_down() :
       position_y  = self.ycor() - 20 
       self.goto(paddle.xcor(), position_y)
    

   
        
  
    
    
    
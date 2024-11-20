import turtle

screen = turtle.Screen()
screen.bgcolor("red")

square_turtle = turtle.Turtle()
square_turtle.shape("turtle")
square_turtle.color("blue")
square_turtle.speed(2)


for i in range(4):
    square_turtle.forward(100)  
    square_turtle.left(90)  


turtle.done()

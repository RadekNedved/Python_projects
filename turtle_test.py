# opens windows with short animation of the turtle named turtlee
from turtle import Turtle, Screen

# window setting
my_screen = Screen()
my_screen.bgcolor("dark goldenrod")

# turtlee setting
turtlee = Turtle()
turtlee.shape("turtle")
turtlee.color("black", "green")
turtlee.shapesize(3, 3, 3)
turtlee.penup()
turtlee.speed(2)

for _ in range(2):
    turtlee.forward(300)
    turtlee.left(90)

turtlee.forward(500)
turtlee.left(90)
turtlee.forward(250)
turtlee.left(90)
turtlee.forward(200)
turtlee.left(810)

# eggs setting
# egg one
vejce1 = Turtle()
vejce1.penup()
vejce1.goto(0, 0)
vejce1.shape("circle")
vejce1.color("#FFEBCD")
vejce1.shapesize(1, 1, 1)

# egg two
turtlee.right(45)
vejce2 = Turtle()
vejce2.penup()
vejce2.goto(-25.00, 0.00)
vejce2.shape("circle")
vejce2.color("#FFEBCD")
vejce2.shapesize(1, 1, 1)

# egg three
turtlee.left(90)
vejce3 = Turtle()
vejce3.penup()
vejce3.goto(25.00, 0.00)
vejce3.shape("circle")
vejce3.color("#FFEBCD")
vejce3.shapesize(1, 1, 1)

turtlee.right(45)
turtlee.forward(50)

my_screen.exitonclick()
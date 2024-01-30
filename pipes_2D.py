# imitates old-times Windows screen saver
from turtle import Turtle, Screen
import random
i = True
rotation_angles = [90, 270]

# window setting
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.colormode(255)
print(f"screensize: height: {my_screen.canvheight}, widht:{my_screen.canvwidth}")

# pen setting
pen = Turtle()
pen.shape("circle")
pen.width(10)
pen.shapesize(0.1, 0.1, 0.1)
pen.color(int(random.randrange(0, 255)), int(random.randrange(0, 255)), int(random.randrange(0, 255)))

# drawing setting
pen.speed(10)

# drawing movement
while i :
    pen.color(int(random.randrange(0, 255)), int(random.randrange(0, 255)), int(random.randrange(0, 255)))
    for _ in range(100):
        random_movement = random.randrange(10, 100)
        random_rotation = random.choice(rotation_angles)
        pen.forward(random_movement)
        pen.left(random_rotation)
        print(F"coordinates: x:{int(pen.xcor())}, y:{int(pen.ycor())}")
# if it would go off the screen
        if abs(int(pen.xcor())) > 400 or abs((pen.ycor())) > 300 :
            pen.penup()
            pen.goto(int(random.randrange(-100, 100)), int(random.randrange(-100, 100)))
            pen.setheading(0)
            pen.pendown()
            pen.color(int(random.randrange(0, 255)), int(random.randrange(0, 255)), int(random.randrange(0, 255)))
    pen.clear()

my_screen.exitonclick()
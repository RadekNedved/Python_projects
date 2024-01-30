# imitates old-times Windows screen saver
from turtle import Turtle, Screen
import random
i = True
rotation_angles = [90, 270]
actual_width = 20

# window setting
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.colormode(255)

# pen setting
pen = Turtle()
pen.shape("circle")
pen.width(10)
pen.shapesize(0.1, 0.1, 0.1)
pen.shapesize(outline=5)


# drawing movement
while i :
    pen.color(int(random.randrange(0, 255)), int(random.randrange(0, 255)), int(random.randrange(0, 255)))
    
    for _ in range(50):

# making a 3D effect
        if actual_width > 15 and actual_width < 60 :
            actual_width = actual_width + random.randrange(-10, 10)
        else :
            actual_width = 20
        pen.width(actual_width)
        pen.speed(round(actual_width / 10) + 1)

        random_movement = random.randrange(10, 200)
        random_rotation = random.choice(rotation_angles)
        pen.forward(random_movement)
        pen.speed(10)
        pen.left(random_rotation)

# if it would go off the screen
        if abs(int(pen.xcor())) > 400 or abs((pen.ycor())) > 300 :
            pen.penup()
            pen.goto(int(random.randrange(-200, 200)), int(random.randrange(-200, 200)))
            pen.setheading(0)
            pen.pendown()
            pen.color(int(random.randrange(0, 255)), int(random.randrange(0, 255)), int(random.randrange(0, 255)))
    pen.clear()

# close
my_screen.exitonclick()
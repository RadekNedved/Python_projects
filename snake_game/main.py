from turtle import Turtle, Screen
import time
import random

# screen setting
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game v0.1")
screen.setup(width=600, height=600)
screen.tracer(False)
screen.listen()

# head setting
head = Turtle("circle")
head.width(10)
head.color("khaki")
head.penup()
head.direction = "stop"

# body setting
body_parts = []

# food setting
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

# score sign setting
score = 0
highest_score = 0
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("SCORE: 0 HIGHEST SCORE: 0", align="center", font=("Arial", 18))

# moving functions
def move() :
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down" :
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left" :
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right" :
        x = head.xcor()
        head.setx(x + 20)

def move_up() :
    if head.direction != "down" :
        head.direction = "up"

def move_down() :
    if head.direction != "up" :
        head.direction = "down"

def move_left() :
    if head.direction != "right" :
        head.direction = "left"

def move_right() :
    if head.direction != "left" :
        head.direction = "right"

def body_move() :
    for index in range(len(body_parts) - 1, 0, -1) :
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)

    if len(body_parts) > 0 :
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

# screen edge collision control 
def screen_collision() :
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290 :
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"
        for one_body_part in body_parts :
            one_body_part.goto(5000, 5000)
        body_parts.clear()
        global score
        score = 0
        score_sign.clear()
        score_sign.write(f"SCORE: {score} HIGHEST SCORE: {highest_score}", align="center", font=("Arial", 18))

# head and body collision control
def head_collision() :    
    for one_body_part in body_parts :
        if one_body_part.distance(head) < 20 :
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"
            for one_body_part in body_parts :
                one_body_part.goto(5000, 5000)
            body_parts.clear()
            global score
            score = 0
            score_sign.clear()
            score_sign.write(f"SCORE: {score} HIGHEST SCORE: {highest_score}", align="center", font=("Arial", 18))

# eating functions
def eating() :
    if head.distance(apple) < 20 :
        randomX = random.randint(-200, 200)
        randomY = random.randint(-200, 200)
        apple.goto(randomX, randomY)

        # apple generated on snakes body
        for one_body_part in body_parts :
            if one_body_part.distance(apple) < 20 :
                randomX = random.randint(-200, 200)
                randomY = random.randint(-200, 200)
                apple.goto(randomX, randomY)

        global score
        score += 1
        global highest_score
        if score >= highest_score :
            highest_score = score
        score_sign.clear()
        score_sign.write(f"SCORE: {score} HIGHEST SCORE: {highest_score}", align="center", font=("Arial", 18))
        growing()


# growing functions
def growing() :
    new_body_part = Turtle("circle")
    new_body_part.width(10)
    new_body_part.color("grey")
    new_body_part.penup()
    body_parts.append(new_body_part)
    x = head.xcor()
    y = head.ycor()
    body_parts[len(body_parts) - 1].goto(x, y)


# controls
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# main cycle
while True :
    screen.update()
    screen_collision()
    head_collision()
    body_move()
    eating()
    move()
    time.sleep(0.2)



screen.update()

screen.exitonclick()

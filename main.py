from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
start_position_y = -120
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=start_position_y)
    start_position_y += 50
    turtles.append(turtle)

if user_bet:
    is_race_on = True

finish_position = 220
while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(75,100)
        x_position = turtle.xcor() + random_distance
        if x_position > finish_position:
            x_position = finish_position
            is_race_on = False
        turtle.goto(x_position, turtle.ycor())
        if not is_race_on:
            break

turtle_color = ""
for index in range(0, len(turtles)):
    if turtles[index].xcor() == finish_position:
        turtle_color = turtles[index].color()

if turtle_color[0] == user_bet:
    print(f"You've won! The {user_bet} finished first!")
else:
    print(f"You've lost! The {user_bet} didn't finish first!")

screen.exitonclick()

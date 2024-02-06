from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
#user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
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

for turtle in turtles:
    print(turtle.pos())

screen.exitonclick()

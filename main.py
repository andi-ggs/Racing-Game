from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Welcome to the world of betting!")
screen.bgpic('road.gif')
ALIGN = "right"
FONT = ("Courier", 28, "bold")

y_positions = [-260, -172, -85, 2, 85, 172, 260]
colors = ["white", "pink", "blue", "green", "purple", "cyan", "yellow"]
all_turtles = []
user_bet = screen.textinput('Enter your bet', prompt= 'Which turtle (color):')

for index in range(0,7):
    turtle = Turtle(shape="turtle")
    turtle.shapesize(2)
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(x = - 400, y = y_positions[index])
    turtle.color(colors[index])
    all_turtles.append(turtle)

is_on = True

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 390:
            is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                turtle.write(f'You won! The {winner} turtle is winner', font=FONT, align=ALIGN)
            else:
                turtle.write(f'You lost!:( The {winner} turtle is winner', font=FONT, align=ALIGN)
        random_pace = random.randint(0, 20)
        turtle.forward(random_pace)

screen.exitonclick()
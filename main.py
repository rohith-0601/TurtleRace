from turtle import Turtle ,Screen
import random
screen = Screen()
screen.setup(width =600,height = 600)
user_guess = screen.textinput("who wins","choose the turtle colour")
print(user_guess)
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
is_race_on = False
all_turtles = []

y = -175
for i in range(6):
    turtle = Turtle("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-275,y)
    all_turtles.append(turtle)
    y += 75

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_guess.lower():
                print(f"you have won! {winning_color} turtle is the winner")
            else:
                print(f"you have lost! {winning_color} turtle is the winner")

        move = random.randint(0,10)
        turtle.forward(move)


screen.exitonclick()


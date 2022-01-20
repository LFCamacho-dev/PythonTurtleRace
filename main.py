from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["lucho", "maria", "jose", "juan", "pedro", "carlos"]
all_turtles = []
y_value = -150


# Set turtles in their right positions
def set_positions(y_val):
    # is_race_on = False

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle", )
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_val)

        all_turtles.append(new_turtle)

        y_val += 60

    get_bet()


def get_bet():
    user_bet = (screen.textinput(title="Make your bet!",
                                 prompt="Which turtle will win the race?  Enter a color: "))

    if user_bet in colors:
        print(f"Your money is on: {user_bet}. Good Luck!")
    else:
        print("Wrong color name, try again")
        get_bet()

    is_race_on = True

    while is_race_on:
        for t in all_turtles:
            if t.xcor() > 230:
                is_race_on = False
                winner_color = t.pencolor()
                if winner_color == user_bet:
                    print(f"You Won! The {winner_color} turtle won the race!")
                else:
                    print(f"You Lost! The {winner_color} turtle won the race!")

            rand_distance = random.randint(0, 10)
            t.forward(rand_distance)


set_positions(y_value)
screen.exitonclick()

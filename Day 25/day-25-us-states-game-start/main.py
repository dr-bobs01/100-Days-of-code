import turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

guess_left = 0
guessed_states = []
list_states = data["state"].tolist()
while True:
    user_awnser = screen.textinput(title=f"Guess the state {guess_left}/50", prompt="what's another  state's name?").title()
    if user_awnser == "Exit":
        break
    if user_awnser in list_states:
        if not user_awnser in guessed_states:
            state_collumn = data[data.state == f"{user_awnser}"]
            writer.goto(state_collumn.x.values[0], state_collumn.y.values[0])
            writer.write(arg=f"{user_awnser}", align="center")
            guessed_states.append(user_awnser)
            guess_left = len(guessed_states)
        else:
            print("Already guessed!")
    else:
        print("Not a state!")

unknown_states = list_states
print(guessed_states)
for state in guessed_states:
    unknown_states.remove(state)
print(unknown_states)
print(list_states)

databot = pandas.DataFrame(unknown_states)
databot.to_csv("unknown_states.csv")

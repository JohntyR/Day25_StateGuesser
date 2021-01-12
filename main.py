from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)
state_df = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state name?"
)


def get_coords(state):
    pass


print(answer_state)
screen.mainloop()
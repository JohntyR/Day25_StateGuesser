from turtle import Screen, Turtle
import pandas

FONT = "Tahoma"
FONT_SIZE = 10
FONT_WEIGHT = "normal"

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)
state_df = pandas.read_csv("50_states.csv")
guessed_states = []
num_of_states = len(state_df.index)


def correct_guess(state):
    return not state_df[state_df["state"] == state].empty


def get_coords(state):
    row = state_df[state_df["state"] == state]
    if row.empty == False:
        print(row)
        x_pos = int(row.x)
        y_pos = int(row.y)
        return (x_pos, y_pos)


def write_state_name(state_name, state_xpos, state_ypos):
    state_writer_turtle = Turtle()
    state_writer_turtle.penup()
    state_writer_turtle.speed("fastest")
    state_writer_turtle.hideturtle()
    state_writer_turtle.goto(x=state_xpos, y=state_ypos)
    state_writer_turtle.write(
        state_name, align="center", font=(FONT, FONT_SIZE, FONT_WEIGHT)
    )


while len(guessed_states) < num_of_states:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{num_of_states} States Correct",
        prompt="What's another state name?",
    ).title()

    if answer_state == "Exit":
        missing_states = [
            state for state in state_df["state"].tolist() if not state in guessed_states
        ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if correct_guess(answer_state) and not answer_state in guessed_states:
        state_coords = get_coords(answer_state)
        write_state_name(answer_state, state_coords[0], state_coords[1])
        guessed_states.append(answer_state)

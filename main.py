from turtle import Screen, Turtle

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state name?"
)
print(answer_state)
screen.mainloop()
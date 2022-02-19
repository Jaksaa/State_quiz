import turtle

def map_answer(coordinates,answer):
    place_answer = turtle.Turtle()
    place_answer.hideturtle()
    place_answer.penup()
    place_answer.goto(coordinates)
    place_answer.write(arg=f"{answer}")
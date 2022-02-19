import turtle
import pandas
import answer_on_map

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
dict_states_data = states_data.to_dict(orient="list")
is_on = True
correct_answer = []


while is_on:
    max_score = len(dict_states_data["state"])
    score = len(correct_answer)
    answer = screen.textinput(title=f"Guess the state {score}/{max_score}", prompt="What's another state's name?").title()
    if answer == "Exit":
        states_to_review = [state for state in dict_states_data["state"] if state not in correct_answer]
        df = pandas.DataFrame(states_to_review)
        df.to_csv("Unguessed states to review.csv")
        break
    if answer in dict_states_data["state"]:
        if answer in correct_answer:
            answer = screen.textinput(title=f"Guess the state {score}/{max_score}", prompt="You have already guessed that state. What's another state's name?").title()
        answer_index = dict_states_data["state"].index(answer)
        coordinates = (int(dict_states_data["x"][answer_index]), int(dict_states_data["y"][answer_index]))
        answer_on_map.map_answer(coordinates, answer)
        correct_answer.append(answer)
        if score == max_score:
            is_on = False
            turtle.write(arg="Congratulations you have guessed all states in US", align="center", font=("Arial", 20,"normal"))



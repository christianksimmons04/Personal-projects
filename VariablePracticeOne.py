# Written by Christian Simmons
# Python stuff

import random

# Random numbers
int_1 = random.randint(5, 20)
int_2 = random.randint(1, 5)
int_3 = random.randint(10, 50)

# Gets a total
total = int_1 + int_2 + int_3

# Produces an output for the integers
print(f"If I combine {int_1}, {int_2}, {int_3} then I get: {total}.")

# Random facts
fact_one = "I like the color"
fact_two = "My favorite drink is"
fact_three = "I root for"

# Random fact answers
answers_for_fact_one = ["Orange", "Green", "Purple"]
answers_for_fact_two = ["Water", "Gatorade", "Coca-Cola"]
answers_for_fact_three = [
    "the Tennessee Volunteers, the best in the land!", # A fact
    "the Alabama Crimson Tide, I used to win.",
    "the Auburn Tigers, I am not particularly happy."
]

# Produces facts and answers
print(f"{fact_one}: {random.choice(answers_for_fact_one)}")
print(f"{fact_two}: {random.choice(answers_for_fact_two)}")
print(f"{fact_three}: {random.choice(answers_for_fact_three)}\n")

# Easy betting predictor
# Teams
teams_one = ["Tennessee", "South Carolina", "Oklahoma"]
teams_two = ["Alabama", "Auburn", "Texas"]

# Pick a random team
chosen_team_one = random.choice(teams_one)
chosen_team_two = random.choice(teams_two)

# Get a random winner
winner = random.choice([chosen_team_one, chosen_team_two])

# Scoring methods
points_one = 3
points_two = 7

# Combo variables tp get a real football score
point_combo_one = points_one * random.randint(0,4)
point_combo_two = points_two * random.randint(0,5)
point_combo_three = points_one * random.randint(0,4)
point_combo_four = points_two * random.randint(0,5)

# Finalize the scores
random_score_one = point_combo_one + point_combo_two
random_score_two = point_combo_three + point_combo_four

if random_score_one > random_score_two:
    differential = random_score_one - random_score_two
else:
    differential = random_score_two - random_score_one

# Gives you a prediction to bet high amounts of income on
print(f"If I had to make a prediction between {chosen_team_one} and {chosen_team_two}, I would pick: {winner}.")
print(f"The final score of the game would be {random_score_one} - {random_score_two}, {winner}.")
print(f"The point differential is: {differential}.")
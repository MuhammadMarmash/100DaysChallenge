from art import *
from game_data import *
import random


def random_choice():
    random1 = random.randint(0, len(data) - 1)
    random2 = random.randint(0, len(data) - 1)
    while random2 == random1:
        random2 = random.randint(0, len(data) - 1)
    return random1, random2


end = False
score = 0
while not end:
    choice1, choice2 = random_choice()
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(
        f"Compare A: {data[choice1]['name']}, {data[choice1]['description']},"
        f" from {data[choice1]['country']}")
    print(vs)
    print(
        f"Against B: {data[choice2]['name']}, {data[choice2]['description']},"
        f" from {data[choice2]['country']}")
    print("Who has more followers? Type 'A' or 'B':")
    answer = str(input()).lower()
    correct_answer = data[choice1]['follower_count'] > data[choice2]['follower_count']
    if (correct_answer and answer == "a") or (not correct_answer and answer == "b"):
        score += 1
        print("\n" * 80)
    else:
        print("\n" * 80)
        print(f"Sorry, that's wrong. Final score: {score}.")
        end = True

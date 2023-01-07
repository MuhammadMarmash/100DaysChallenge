import art
import game_data
import random


def random_choice():
    random1 = random.randint(0, len(game_data.data) - 1)
    random2 = random.randint(0, len(game_data.data) - 1)
    while random2 == random1:
        random2 = random.randint(0, len(game_data.data) - 1)
    return random1, random2


end = False
score = 0
while not end:
    choice1, choice2 = random_choice()
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(
        f"Compare A: {game_data.data[choice1]['name']}, {game_data.data[choice1]['description']},"
        f" from {game_data.data[choice1]['country']}")
    print(art.vs)
    print(
        f"Against B: {game_data.data[choice2]['name']}, {game_data.data[choice2]['description']},"
        f" from {game_data.data[choice2]['country']}")
    print("Who has more followers? Type 'A' or 'B':")
    answer = str(input()).lower()
    correct_answer = game_data.data[choice1]['follower_count'] > game_data.data[choice2]['follower_count']
    if (correct_answer and answer == "a") or (not correct_answer and answer == "b"):
        score += 1
        print("\n" * 80)
    else:
        print("\n" * 80)
        print(f"Sorry, that's wrong. Final score: {score}.")
        end = True

#display art
from art import logo , vs
from game_data import data
import random
def format_data(account):
    """Format the account data and return the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f" {account_name}, a {account_descr}, a {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """take a user's guess and the followers counts and return if they got it right """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
#make the game repeatable
while game_should_continue:
    #generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"compare A: {format_data(account_a)}.")
    print(vs)
    print(f"compare B: {format_data(account_b)}.")
    #ask user for a guess
    guess =input("who has more followers? type 'A' or 'B': ").lower()
    #check if user is correct
    #makihg account at position B become the next account at position A
    print("\n" *20)
    print(logo)
    ##GEt follower count of each account
    a_followers_count = account_a["followers_count"]
    b_followers_count = account_b["followers_count"]
    ##Use if statement to check if user is correct
    is_correct = check_answer(guess, a_followers_count, b_followers_count)


    #give user feedback on their guess

    #score keeping
    if is_correct:
        score += 1
        print(f"you're right! current score {score}")
    else:
        print(f"sorry, that's wrong. final score: {score}")
        game_should_continue = False



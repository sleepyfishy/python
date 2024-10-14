import random

user_wins = 0
computer_wins = 0

def score():
    print(f"wins: {user_wins}, losses: {computer_wins}")

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("type r/p/s or Q to quit: ").lower()
    if user_input == "q":
        quit()
    
    if user_input not in ["r", "p", "s"]:
        continue
    
    random_number = random.randint(0, 2)
    #rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print(f"computer picked: {computer_pick}")

    if user_input == "r" and computer_pick == "scissors":
        print("you win")
        user_wins += 1
        
    elif user_input == "p" and computer_pick == "rock":
        print("you win")
        user_wins += 1
        
    elif user_input == "s" and computer_pick == "paper":
        print("you win")
        user_wins += 1
       
    elif user_input == "r" and computer_pick == "paper":
        print("you lost")
        computer_wins += 1

    elif user_input == "p" and computer_pick == "scissors":
        print("you lost")
        computer_wins += 1

    elif user_input == "s" and computer_pick == "rock":
        print("you lost")
        computer_wins += 1
    
    else:
        print("draw")
    
    score()

print(f"you won {user_wins} times and lost {computer_wins} times.")
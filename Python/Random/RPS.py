import random
print("Let's Play Rock Paper Scissors!")
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice = input("Make your Choice: rock, paper, scissors? ")

# Run Conditionals

# Tie
if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")

# Rock
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")

# Paper
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose!")

# Scissors
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scisssors! You lose!")
import random

list_of_choices = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(list_of_choices).lower()

user_choice = input("Pick your choice! Do you pick Rock, Paper, Or Scissors! ").lower()

if user_choice == "rock" and computer_choice == "scissors":
    print("Congratulations! Rock Beats Scissors! You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Congratulations! Paper beats Rock! You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Congratulations! Scissors beats Paper! You win!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Oh No! Paper Beats Rock! You lose!")
elif user_choice == "paper" and computer_choice =="scissors":
    print("Oh No! Scissors Beats Paper! You Lose!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("Oh No! Rock Beats Scissors! You Lose!")
elif user_choice == computer_choice:
    print("Woah! A tie! Try again!")
else:
    print("C'mon! You gotta try and play!")

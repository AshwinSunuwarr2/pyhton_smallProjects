import random

user_win = 0
computer_win = 0
options = ["rock", "paper", "scissor"]

while True:
    user_pick = input("Pick Rock/Paper/Scissor or Press Q to quit: ").lower()
    if user_pick == "q":
        break
    if  user_pick not in options:
        continue

    random_num = random.randint(0, 2)
    computer_pick = options[random_num]
    print(f"Computer picked: {computer_pick}")

    if user_pick == "rock" and computer_pick == "scissor":
        print("You've won!")
        user_win += 1
    elif user_pick == "paper" and computer_pick == "rock":
        print("You've won!")
        user_win += 1
    elif user_pick == "scissor" and computer_pick == "paper":
        print("You've won!")
        user_win += 1
    else:
        print("Computer won!")
        computer_win += 1

print(f"You've won {user_win} times and computer won {computer_win} times.")
print("Goodbye!!")
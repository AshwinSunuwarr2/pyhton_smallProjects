import random 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter number greater than 0 next time.")
        quit()

else:
    print("Enter a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guess_count = 0
lives = 3

while True:
    print("You've got "+ str(lives) +" lives")
    lives -= 1
    guess_count += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time.")
        continue

    if user_guess == random_number:
        print("YOu've got it")    
        print("You took ",guess_count," guesses")
        break
    elif lives != 0:
        if user_guess > random_number:
            print("you were above the number.")
        else:
            print("You were below the number.")
    else:
        print("Out of lives :(")
        break   


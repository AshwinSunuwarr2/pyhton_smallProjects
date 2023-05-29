import random

choice = input("Do you want to go on a adventure? (Yes/No): ").lower()
if choice == "no":
    print("Well then, GoodBye!!")
    quit()

elif choice == "yes":
    name = input("Enter your name: ")
    print(f"Hello {name}. I'm just a voice inside you. Lets begin our adventure!!")

    answer = input("We spawned on a jungle. Do you wanna take right or left? (Right/Left): ").lower()
    if answer == "right":
        answer = input("You turned right and came to a river. Do you wanna swim across or walk alongside the river? (swim/walk): ").lower()
        if answer == "swim":
            print("You dived into the river and got eaten by an aligator. You lose :(")
        elif answer == "walk":
            answer = input("You walked for miles and reached an abandoned house. Do you wanna enter the house or keep walking? (enter/walk): ").lower()
            if answer == "walk":
                print("You've walked around for days and died of hunger. :(")
            elif answer == "enter":
                answer = input("Inside house you saw some food and ate it. Do you want to stay on the house or continue your journey? (stay/continue): ").lower()
                if answer == "stay":
                    print("That night you were haunted by ghosts and died. :(")
                elif answer == "continue":
                    answer = input("After walking around for days, you've reached the highway and a car was comming your way. Do you want to hitchhike or continue walking? (hitchhike/continue): ").lower()
                    if answer == "continue":
                        print("You died after walking several days. :(")
                    elif answer == "hitchhike":
                        answer = input("The driver was helpful and dropped you at your home. You've won. :)")
                    else:
                        print("Wrong answer. You lost. :(")
            else:
                print("You chose wrong. You lose :(")
        else:
            print("You chose wrong. You lose :(")

    elif answer == "left":
        print("Fell throug the cliff and you died..")

    else:
        print("You chose wrong. You lose :(")

else:
    print(f"You have to type either Yes or No")



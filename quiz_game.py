print("Welcome To Quiz Game..")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets Play  :)")
score = 0
questions_count = 0

answer = input("What does CPU stands for? >> ").lower()
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
questions_count +=1

answer = input("What does GPU stands for? >> ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
questions_count += 1

answer = input("What does RAM stands for? >> ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
questions_count += 1

answer = input("What does ROM stands for? >> ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
questions_count += 1

answer = input("What does PSU stands for? >> ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
questions_count += 1

print("You've got " + str(score) + " questions correct")
print("You've got " + str((score/questions_count)*100) + "%.")
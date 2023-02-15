print("Welcome to my computer quiz")

#start of game if else statements
playing = input("Do you want to play? ")
if playing != "yes":
    print("Okay goodbye then :(")
    quit()
else:
    print("Okay! Let's play :)")

#questions
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
else: 
    print('wrong answer buddy')

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print('Correct!')
else: 
    print('wrong answer buddy')

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
else: 
    print('wrong answer buddy')

answer = input("What does PSU stand for? ")
if answer == "power supply unit":
    print('Correct!')
else: 
    print('wrong answer buddy')


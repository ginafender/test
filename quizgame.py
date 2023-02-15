print("Welcome to my computer quiz")

#start of game if else statements
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    print("Okay goodbye then :(")
    quit()
else:
    print("Okay! Let's play :)")
score = 0

#questions
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else: 
    print('wrong answer buddy')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else: 
    print('wrong answer buddy')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else: 
    print('wrong answer buddy')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else: 
    print('wrong answer buddy')

#final score
print("You got " + str(score / 4 *100) + "%")
if score <= 2:
    print("Wow, that's embarassing!")
else:
    print("Good job..I guess?")
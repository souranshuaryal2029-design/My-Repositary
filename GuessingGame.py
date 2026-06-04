import random
attempt = 0
computer_guess = random.randint(0, 20)
play = "yes"

while play.lower()=="yes":
    myguess = int(input("Try to guess number: "))
    if myguess == computer_guess:
        print("You have guest the right number")
        break
    else:
        print("Nice try but its wrong number.")
    play = input("Do you want to continue? Yes/No: ")
    attempt += 1

print("number of attempts: ", attempt)
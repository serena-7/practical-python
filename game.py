import random

user_name = input("Howdy, what's your name?\n(type in your name) ")
comp_number = random.randint(1,100)

print(user_name + ", I'm thinking of a number between 1 and 100")

try_num = 0
while(True):
    user_guess = int(input("Your guess? "))
    try_num += 1
    if(user_guess < comp_number):
        print("Your guess is too low, try again.")
    elif(user_guess > comp_number):
        print("Your guess is too high, try again.")
    else:
        print("Well done, " + user_name + "! You found my number in " + str(try_num) + " tries!")
        break
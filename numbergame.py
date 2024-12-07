import random 
play = True
ask = str(random.randint(10,20))
print("I will generate a number from 18 to 26 and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")
while play:
    guess = input("Give me your best guess! \n")
    if ask == guess:
        print("You win the game")
        print("The number was:", ask)
        break
    else:
        print("Your guess wasn't quite right, try again")
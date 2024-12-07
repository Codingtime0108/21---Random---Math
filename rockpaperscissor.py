import random
possibilty = ["Rock","Paper","Scissors"]
action = random.choice(possibilty)

variable = input(("Enter a value: Rock, Paper or Scissors"))
print(f"\nYou have chosen:",{variable},",computer choose:",{action})

if variable == action:
    print("Its a tie")
elif variable == "Rock" and action == "Scissors":
    print("You win") 
elif variable == "Paper" and action == "Scissors":
    print("You lose")
elif variable == "Scissors" and action == "Rock":
    print("You lose")  
elif variable == "Paper" and action == "Rock":
    print("You win")    
elif variable == "Rock" and action == "Paper":
    print("You lose")        
elif variable == "Scissors" and action == "Paper":
    print("You lose")
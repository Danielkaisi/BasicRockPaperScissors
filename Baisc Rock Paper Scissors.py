import random

#After importing random, random range gets set to output 1 2 or 3
ComputerChoiceRNG = random.randrange(1,4,1)

#Depending on output, ComputerChoice gets set to Rock, Paper or Scissors

if ComputerChoiceRNG == 1:
    ComputerChoice = "Rock"
if ComputerChoiceRNG == 2:
    ComputerChoice = "Paper"
if ComputerChoiceRNG == 3:
    ComputerChoice = "Scissors"

#UserChoice gets set to false for the while loop
UserChoice = False

#Completely hardcoded for simplicity, and cause I don't know how to code
while UserChoice == False:
    UserChoice = input("Please choose Rock, Paper or Scissors ")
    print("You chose " + UserChoice)
    print("Computer chose " + ComputerChoice)
    if ComputerChoice == "Rock" and UserChoice in ["Rock", "rock"]:
        print("Draw!")
    elif ComputerChoice == "Paper" and UserChoice in ["Paper", "paper"]:
        print("Draw!")
    elif ComputerChoice == "Scissors" and UserChoice in ["Scissors", "scissors"]:
        print("Draw!")
    elif ComputerChoice == "Rock" and UserChoice in ["Paper", "paper"]:
        print("You win! Paper covers Rock")
    elif ComputerChoice == "Paper" and UserChoice in ["Scissors", "scissors"]:
        print("You win! Scissors cuts Paper")
    elif ComputerChoice == "Scissors" and UserChoice in ["Rock", "rock"]:
        print("You win! Rock dulls Scissors")
    elif ComputerChoice == "Rock" and UserChoice in ["Scissors", "scissors"]:
        print("You lose! Rock dulls Scissors")
    elif ComputerChoice == "Paper" and UserChoice in ["Rock", "rock"]:
        print("You lose! Paper covers Rock")
    elif ComputerChoice == "Scissors" and UserChoice in ["Paper", "paper"]:
        print("You lose! Scissors cuts Paper")
    else:
        print("Input invalid, make sure to either capitalize only the first lever or use full lowercase")
    
    #Both variables get set back to their original setting to continue the while loop
    
    #Turned to comments because I prefer it not looping while testing
    #UserChoice = False
    #ComputerChoiceRNG = random.randrange(1,4,1)
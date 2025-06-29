import random

# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

play = True
while(play):
    options = [rock, paper, scissor]

    userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

    if userChoice < 0 or userChoice > 2:
        print("Invalid choice. Please choose 0, 1, or 2.")

    else:

        print("You chose:")
        print(options[userChoice])

        computerChoice =random.randint(0, 2)

        print("Computer choose")
        print(options[computerChoice])

        if userChoice == computerChoice:
            print("It's a draw!") 
        elif (userChoice == 0 and computerChoice == 2) or \
            (userChoice == 1 and computerChoice == 0) or \
            (userChoice == 2 and computerChoice == 1):
            print("You win!")
        else:       
            print("You lose")

        if input("Do you want to play again? (Y / N) : ") == 'Y':
            play = True
        else:
            play = False

        
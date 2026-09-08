import random 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

player = int(input(
    "Choose:\n"
    "0 - Rock\n"
    "1 - Paper\n"
    "2 - Scissors\n"
    "> "
))

computer = random.randint(0, 2)

print("\nYou chose:")
print(options[player])

print("\nComputer chose:")
print(options[computer])


if player == computer:
    print("Draw!")

elif player == 0 and computer == 2:
    print("You win!")

elif player == 1 and computer == 0:
    print("You win!")

elif player == 2 and computer == 1:
    print("You win!")

else:
    print("You lose!")
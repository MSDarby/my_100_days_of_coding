import random

#The rules of the rock paper scissors game
#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_input = [rock, paper, scissors]

print("Welcome to my rock, paper, scissors game!")

player_choice = int(input("To play please Type 0 rock, 1 for "
                      "paper and 2 for scissors:\n"))
if player_choice >=0 and player_choice <=2:
    computer_choice = random.randint(0,2)
    if player_choice == computer_choice:
        print(f"You choose {game_input[player_choice]}")
        print(f"Computer choose {game_input[computer_choice]}")
        print("It's a draw!")
    elif player_choice==0 and computer_choice==2 or \
         player_choice==2 and computer_choice==1 or \
         player_choice==1 and computer_choice==0:
        print(f"You choose {game_input[player_choice]}")
        print(f"Computer choose {game_input[computer_choice]}")
        print("You win!")
    else:
        print(f"You choose {game_input[player_choice]}")
        print(f"Computer choose {game_input[computer_choice]}")
        print("You lose!")
else:
    print("Invalid choice\nGame Over!")

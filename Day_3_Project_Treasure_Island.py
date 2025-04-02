print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_decision = input("You\'re at a cross road. "
                       "Where do you want to go, left or right? "
                       "Please type left or right: ").upper()
if first_decision == 'LEFT':
    second_decision = input("You are at a lake. Do you want to "
                            "swim across or wait for the boat?"
                            "Please type swim or wait: ").upper()
    if second_decision == 'WAIT':
        third_decision = input("You are at a cross road. Which "
                               "door do you want to go through? "
                               "Please type red, blue or yellow: ").upper()
        if third_decision == 'YELLOW':
            print("You win!!!")
        elif third_decision == 'RED':
            print("You have been burnt by fire.\nGame Over!")
        elif third_decision == 'BLUE':
            print("You have been eaten by beasts.\nGame Over!")
        else:
            print("Invalid option chosen.\nGame Over!")
    elif second_decision == 'SWIM':
        print("You have been attacked by trout.\nGame Over!")
    else:
        print("Invalid option chosen.\nGame Over!")
elif first_decision == 'RIGHT':
    print("You have fallen into a hole.\nGame Over!")
else:
    print("Invalid option chosen.\nGame Over!")

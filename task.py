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

first_decision = input("You must turn left or right to continue. "
                       "Please type left or right: ")
if first_decision == 'left':
    second_decision = input("You now have a large lake to cross. Do you "
                            "want to swim across or wait for the boat? "
                            "Please type swim or wait: ")
    if second_decision == 'wait':
        third_decision = input("You are now at a cross road. "
                               "you will need to choose a door to pass through"
                               "Please choose the red, blue or yellow door."
                               "Please type red, blue or yellow: ")
        if third_decision == 'yellow':
            print("You win!!!")
        elif third_decision == 'red':
            print("You have been burnt by fire.\nGame Over!")
        elif third_decision == 'blue':
            print("You have been eaten by beasts.\nGame Over!")
        else:
            print("Invalid option chosen.\nGame Over!")
    elif second_decision == 'swim':
        print("You have been attacked by trout.\nGame Over!")
    else:
        print("Invalid option chosen.\nGame Over!")
elif first_decision == 'right':
    print("You have fallen into a hole.\nGame Over!")
else:
    print("Invalid option chosen.\nGame Over!")


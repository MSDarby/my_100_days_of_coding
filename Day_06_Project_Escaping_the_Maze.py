# using the link here https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Maze&url=%2Fworlds%2Ftutorial_en%2Fmaze1.json
#to get to the world with the maze and run the code to escape the maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while not at_goal(): 
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()

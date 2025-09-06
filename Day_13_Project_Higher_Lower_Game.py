import random
from higherlower_art import logo, vs
from higherlowergame_data import data


def format_data(num): 
    '''This is a function to format the A and B message in the game'''
    name=data[num]['name']
    describe=data[num]['description']
    country=data[num]['country']
    return f"{name}, a {describe}, from {country}."


def check_guess(guess, A_count, B_count):
    '''This is the function which checks which account had more followers'''
    if A_count > B_count:
        return guess == 'A'
    else: 
        return guess == 'B'
    
print(logo)
score= 0
winning = True
B = random.choice(data)

#creating a loop so that game repeats when correct
while winning:
    A=B
    B = random.choice(data)
    if A == B: 
        B = random.choice(data)
        
    print(f"Compare A: {format_data(A)}.")
    print(vs)
    print(f"Against B: {format_data(B)}.")


    A_count=data[A]['follower_count']
    B_count=data[B]['follower_count']

    
    guess = input("Who has more followers? Type A or B: \n").upper()

    is_correct = check_guess(guess, A_count, B_count)
    if is_correct:
        score+=1
        print(f'''You're right! Current score: {score}.''')
    else: 
        print(f'''Sorry, that's wrong. Final score: {score}.''')
        winning = False

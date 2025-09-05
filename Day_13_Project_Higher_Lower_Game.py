import random
import higherlower_art
import higherlowergame_data

A = random.randint(0, len(higherlowergame_data.data)-1)

winning = True
score= 0
while winning:
    print(higherlower_art.logo) 
    A_name=higherlowergame_data.data[A]['name']
    A_describe=higherlowergame_data.data[A]['description']
    A_country=higherlowergame_data.data[A]['country']
    A_count=higherlowergame_data.data[A]['follower_count']

    print(f"Compare A: {A_name}, a {A_describe}, from {A_country}.")

    print(higherlower_art.vs)

    B = A+1 
    B_name=higherlowergame_data.data[B]['name']
    B_describe=higherlowergame_data.data[B]['description']
    B_country=higherlowergame_data.data[B]['country']
    B_count=higherlowergame_data.data[B]['follower_count']

    print(f"Against B: {B_name}, a {B_describe}, from {B_country}.")

    Ans = input("Who has more followers? Type A or B: \n").upper()

    if Ans == 'A':
        if A_count > B_count:
            score+=1
            print(f'''You're right! Current score: {score}.''')
            A = B
        if A_count < B_count:
            print(f'''Sorry, that's wrong. Final score: {score}.''')
            winning = False
    elif Ans == 'B':
        if B_count > A_count:
            score+=1
            print(f'''You're right! Current score: {score}.''')
            A = B
        if B_count < A_count:
            print(f'''Sorry, that's wrong. Final score: {score}.''')
            winning = False
    else: 
        print(f'''Sorry, you inputed an invalid number. Final score: {score}.''')
        winning = False
import blackjack_art
import random

def play_game():
    print(blackjack_art.logo)
    def deal_card():
        """ returns a random card"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def calculate_score(lists):
        """ this function calculate the total of the cards in the list
            but also check for blackjack 21
        """
        if sum(lists)==21 and len(lists)==2:
            return 0
        elif sum(lists) > 21 and 11 in lists:
            lists.remove(11)
            lists.append(1)
        else:
            return sum(lists)

    def compare(u_score, d_score):
        """ This compares the total from the calculated score and state whether
            its a win, lose or draw"""
        if u_score == d_score:
            print("Its a draw")
        elif d_score == 0:
            print("Dealer won!!! try again!")
        elif u_score == 0:
            print("You won!!!")
        elif u_score > 21:
            print("Dealer won!!! try again!")
        elif d_score > 21:
            print("You won!!!")
        elif d_score > u_score:
            print("Dealer won!!! try again!")
        else:
            print("You won!!!")


    dealer_cards = []
    dealer_score = -1
    user_cards = []
    user_score = -1
    is_game_over = False

    for num in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score =  calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"your cards {user_cards}, your score is {user_score}")
        print(f"dealer's first card is {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            new_deal = input("Type 'y' to get another card or 'n' to pass: \n").lower()
            if new_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while dealer_score!=0 and dealer_score<17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)


    print(f"You final hand was {user_cards} and your final score was {user_score}")
    print(f"the dealer final hand was {dealer_cards} and their final score was {dealer_score}")
    print(compare(user_score, dealer_score))


while input("Do you want to play a hand of blackjack? type yes or no: \n") == "yes":
    print("\n" * 20)
    play_game()

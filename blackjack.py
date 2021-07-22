from card import Card
import random

# Gets the score of a player's hand
def get_score(hand):
    score = 0
    for card in hand:
        for key, value in card.items():
            score += value[1]

    return score

# Recieve's player's hand and turn it into a list of Cards
def get_cards(hand):
    cards = []
    for card in hand:
        for key, value in card.items():
            new_card = Card(key, value[0])
            cards.append(new_card)
    return cards

# Checks a player's hand for an Ace and returns true if found
def find_ace(hand):
    ace = False
    index = None
    for card in hand:
        for key, value in card.items():
            if value[0] == "A":
                ace = True
                index = hand.index(card)
    return ace, index


suits = ["♥", "♠", "♣", "♦"]
values = [["A", 11], ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("J", 10), ("Q", 10), ("K", 10)]

# Create the deck from which the cards are drawn
deck = []
for suit in suits:
    for value in values:
        deck.append({suit: value})

user_hand = []
user_cards = []


def game():
    user_hand.append(random.choice(deck))
    user_hand.append(random.choice(deck))
    user_score = get_score(user_hand)


    should_continue = True

    user_over_21 = False
    while should_continue and not user_over_21:
        user_score = get_score(user_hand)
        user_cards = get_cards(user_hand)
        print("In your hand:")
        print(" ".join(str(card) for card in user_cards))
        if input("Would you like another card? (y/n)") == 'y':
            user_hand.append(random.choice(deck))
            user_score = get_score(user_hand)
            if user_score > 21:
                ace, index = find_ace(user_hand)
                if not ace:
                    user_over_21 = True
                else:
                    for key, value in user_hand[index].items():
                        value[1] = 1
        else:
            should_continue = False
    if user_over_21:
        print("You went over 21. You Lose")

game()
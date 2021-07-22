from card import Card
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

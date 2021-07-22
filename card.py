class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    def __repr__(self):
        self.card = ""
        if len(self.value) == 2:
            self.card = """
    ┌─────────┐
    │{}       │
    │         │
    │         │
    │    {}    │
    │         │
    │         │
    │       {}│
    └─────────┘""" .format(self.value, self.suit, self.value)
        else:
            self.card = """
    ┌─────────┐
    │{}        │
    │         │
    │         │
    │    {}    │
    │         │
    │         │
    │        {}│
    └─────────┘""" .format(self.value, self.suit, self.value)

        return self.card
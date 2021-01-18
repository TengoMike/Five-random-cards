import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []
hand =[]

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

deck_len = len(deck)

print(f'There are {deck_len} cards in the deck.')
print('Dealing...')

while len(hand) < 5:
    chosen_card = random.choice(deck)
    hand.append(chosen_card)
    deck.remove(chosen_card)

deck_len = len(deck)

print(f'There are {deck_len} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand) 

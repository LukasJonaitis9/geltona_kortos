import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = f"{suit} {rank}"
        self.weight = self.calculate_weight()

    def calculate_weight(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.shuffle()
        self.ensure_no_same_weight_adjacent()

    def shuffle(self):
        random.shuffle(self.cards)

    def ensure_no_same_weight_adjacent(self):
        for skip in range(1, len(self.cards)):
            while self.cards[skip].weight == self.cards[skip - 1].weight:
                self.shuffle()

    def deal_card(self):
        return self.cards.pop()

def war():
    deck = Deck()
    player1_cards = deck.cards[:len(deck.cards)//2]
    player2_cards = deck.cards[len(deck.cards)//2:]

    while player1_cards and player2_cards:
        player1_card = player1_cards.pop(0)
        player2_card = player2_cards.pop(0)

        print(f"Žaidėjas 1: {player1_card.sign} prieš Žaidėjas 2: {player2_card.sign}")

        if player1_card.weight > player2_card.weight:
            print("Žaidėjas 1 laimi šį raundą!\n")
            player1_cards.extend([player1_card, player2_card])
        elif player1_card.weight < player2_card.weight:
            print("Žaidėjas 2 laimi šį raundą!\n")
            player2_cards.extend([player1_card, player2_card])
        else:
            print("Karas!")
            while True:
                if len(player1_cards) < 4 or len(player2_cards) < 4:
                    print("Nepakanka kortų karo metu. Žaidimas baigiamas.")
                    return

                war_cards = [player1_card, player2_card]
                for _ in range(4):
                    war_cards.extend([player1_cards.pop(0) for _ in range(4)])
                    war_cards.extend([player2_cards.pop(0) for _ in range(4)])

                war_card1 = war_cards[-1]
                war_card2 = war_cards[-2]

                print(f"Karo kortelė 1: {war_card1.sign} | Karo kortelė 2: {war_card2.sign}")

                if war_card1.weight > war_card2.weight:
                    print("Žaidėjas 1 laimi karą!\n")
                    player1_cards.extend(war_cards)
                    break
                elif war_card1.weight < war_card2.weight:
                    print("Žaidėjas 2 laimi karą!\n")
                    player2_cards.extend(war_cards)
                    break

if __name__ == "__main__":
    war()



    #KORTU KALadė
# Korta: objektas
# -- rank (2-9, T, J, Q, K, A)
# -- suit (spades, clubs, hearts, diamonds)
# -- sign (suit + rank)
# -- weight
# Kortų kaladė
# -- cards - sąrašas kortų
# -- shuffle
# -- take from top
# -- take from bottom
# -- take random
# mastom apie žaidimą
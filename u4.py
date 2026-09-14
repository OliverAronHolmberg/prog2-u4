import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit} - {self.value}"


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def show_all(self):
        for card in self.cards:
            print(card)

    def draw_card(self, num):
        cards_dealt = self.cards[:num]
        self.cards = self.cards[num:]
        return cards_dealt

    def cards_left(self):
        print(len(self.cards))

    def shuffle_cards(self):
        random.shuffle(self.cards)

    @staticmethod
    def make_cards():
        cards = []
        suits = ["♠", "♥", "♣", "♦"]
        values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for suit in suits:
            for value in values:
                cards.append(Card(suit, value))
        return cards


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def take_cards(self, cards):
        self.hand.extend(cards)

    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop()
        else:
            return None


def get_card_category(card):
    if card.value in (2, 3, 4, 5, 6, 7):
        return "Lågt kort"
    else:
        return "Högt kort"


def play_game():
    player1 = Player("Player1")
    player2 = Player("Player2")

    cards = Deck.make_cards()
    deck = Deck(cards)
    deck.shuffle_cards()

    while True:
        if len(deck.cards) < 2:
            print("Korten i leken är slut!")
            break

        player1.take_cards(deck.draw_card(1))
        player2.take_cards(deck.draw_card(1))

        card1 = player1.play_card()
        card2 = player2.play_card()

        
        cat1 = get_card_category(card1)
        cat2 = get_card_category(card2)

        print(f"{player1.name}: {card1} ({cat1}) | {player2.name}: {card2} ({cat2})")

        if cat1 == "Högt kort" and cat2 == "Lågt kort":
            print(f"-> {player1.name} Vinner!\n")
        elif cat2 == "Högt kort" and cat1 == "Lågt kort":
            print(f"-> {player2.name} Vinner!\n")
        else:
            print("-> Oavgjort\n")

        y = input("Vill du spela en runda till? (Y/N): ")
        if y.upper() == "N":
            break


play_game()
from . import Card
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.__cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.__cards += [card]

    def remove_card(self, card_name: str) -> None:

        for index in range(len(self.__cards)):
            if self.__cards[index].name == card_name:
                del self.__cards[index]

    def shuffle(self) -> None:
        self.__cards = shuffle(self.__cards)

    def draw_card(self) -> Card:
        return self.__cards[-1]

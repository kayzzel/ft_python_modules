from . import Card
from random import shuffle


class Deck:
    def __init__(self) -> None:
        self.__cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.__cards += [card]

    def remove_card(self, card_name: str) -> bool:
        for index in range(len(self.__cards)):
            if self.__cards[index].name == card_name:
                del self.__cards[index]
                return True
        return False

    def shuffle(self) -> None:
        self.__cards = shuffle(self.__cards)

    def draw_card(self) -> Card:
        return self.__cards.pop()

    def get_deck_stats(self) -> dict:
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        total_cost: float = 0

        for card in self.__cards:
            if card.__class__.__name__ == "CreatureCard":
                creatures += 1
            elif card.__class__.__name__ == "ArtifactCard":
                artifacts += 1
            elif card.__class__.__name__ == "SpellCard":
                spells += 1
            total_cost += card.cost

        return {
                "card_count": len(self.__cards),
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost": round(total_cost / len(self.__cards), 2)
                }

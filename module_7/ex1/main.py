#!/usr/bin/env python3

from ex0 import CreatureCard
from . import Deck, SpellCard, ArtifactCard


def main() -> None:
    deck: Deck = Deck()

    print("=== DataDeck Deck Builder ===")

    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare",
                               4, "Permanent: 1 mana per turn"))
    deck.add_card(SpellCard("Lightning Bolt", 3,
                            "Epic", "Deal 3 damage to target"))

    deck.shuffle()
    player1: dict = {
            "available_mana": 50,
            "deck": deck,
            "hand": [],
            "board": []
            }
    print()
    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print()
    print("Drawing and playing cards:")
    for _ in range(3):
        player1['hand'].append(deck.draw_card())

        print()
        print(f"Drew: {player1['hand'][0].name}")
        print(f"Play result: {player1['hand'][0].play(player1)}")

    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()

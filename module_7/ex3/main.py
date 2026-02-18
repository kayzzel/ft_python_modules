#!/usr/bin/env python3

from .FantasyCardFactory import FantasyCardFactory
from ex0.Card import Card

if __name__ == "__main__":
    factorie: FantasyCardFactory = FantasyCardFactory()

    cards: Card = factorie.create_themed_deck(10)
    print("Creatures")
    for creature in cards["creatures"]:
        print(creature.get_card_info())
    print("\nSpells")
    for spell in cards["spells"]:
        print(spell.get_card_info())

    print("\nArtifacts")
    for artifact in cards["artifacts"]:
        print(artifact.get_card_info())

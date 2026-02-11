from . import Deck, SpellCard, ArtifactCard, CreatureCard, Card


def main() -> None:
    deck: Deck = Deck()
    game_state: dict = {
            "available_mana": 50
            }

    print("=== DataDeck Deck Builder ===")

    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare",
                               4, "Permanent: +1 mana per turn"))
    deck.add_card(SpellCard("Lightning Bolt", 3,
                            "Epic", "Deal 3 damage to target"))

    print()
    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print()
    print("Drawing and playing cards:")
    for _ in range(3):
        drew: Card = deck.draw_card()

        print()
        print(f"Drew: {drew.name}")
        print(f"Play result: {drew.play(game_state)}")

    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()

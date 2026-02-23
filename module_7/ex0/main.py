#!/usr/bin/env python3

from . import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")

    player1: dict = {
            "available_mana": 10,
            "hand": [CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)],
            "board": []
            }
    player2: dict = {
            "available_mana": 10,
            "hand": [CreatureCard("Goblin Warrior", 3, "Rare", 4, 5)],
            "board": []
            }

    print()
    print("Testing Abstract Base Class Design:")

    print()
    print("CreatureCard Info:")
    print(player1["hand"][0].get_card_info())
    player2["hand"][0].play(player2)
    print()
    print("Playing Fire Dragon with 6 mana available:")
    print(
            "Playable: "
            f"{player1['hand'][0].is_playable(player1['available_mana'])}"
        )
    print(f"Play result: {player1['hand'][0].play(player1)}")

    print()
    print("Fire Dragon attacks Goblin Warrior:")
    print(
            f"Attack result: "
            f"{player1['board'][0].attack_target(player2['board'][0])}"
        )

    player1['available_mana'] = 3
    print()
    print("Testing insufficient mana (3 available):")
    print(
            "Playable: "
            f"{player1['board'][0].is_playable(player1['available_mana'])}"
        )

    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()

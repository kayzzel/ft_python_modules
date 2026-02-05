from . import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")

    game_state: dict = {
            "available_mana": 10
            }

    fire_dragon: CreatureCard = CreatureCard(
            "Fire Dragon", 5, "Legendary", 7, 5
            )

    goblin_warrior: CreatureCard = CreatureCard(
            "Goblin Warrior", 3, "Rare", 4, 5
            )

    print()
    print("Testing Abstract Base Class Design:")

    print()
    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    goblin_warrior.play(game_state)
    print()
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(game_state['available_mana'])}")
    print(f"Play result: {fire_dragon.play(game_state)}")

    print()
    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    game_state['available_mana'] = 3
    print()
    print("Testing insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(game_state['available_mana'])}")

    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()

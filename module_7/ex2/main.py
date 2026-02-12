#!/usr/bin/env python3

from .EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("""
=== DataDeck Ability System ===

EliteCard capabilities:
- Card: ['play', 'get_card_info', 'is_playable']
- Combatable: ['attack', 'defend', 'get_combat_stats']
- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']
""")

    game_state: dict = {
            "available_mana": 50
            }

    arcane_warrior: EliteCard = EliteCard(
            "Arcane Warrior",
            5,
            "super_rare",
            15,
            5,
            3,
            2,
            1,
            {"Fireball": 4}
            )

    enemy: CreatureCard = CreatureCard(
            "Enemy",
            3,
            "common",
            7,
            3
            )

    enemy2: CreatureCard = CreatureCard(
            "Enemy2",
            3,
            "common",
            7,
            3
            )

    arcane_warrior.play(game_state)
    enemy.play(game_state)

    print(
            "Playing Arcane Warrior (Elite Card):\n"
            "\n"
            "Combat phase:"
            )

    print(f"Attack result: {arcane_warrior.attack(enemy)}")
    print(f"Defence result: {arcane_warrior.defend(5)}")

    print()
    print("Magic phase:")

    arcane_warrior.channel_mana(8)
    print(f"Spell cast: \
{arcane_warrior.cast_spell('Fireball', [enemy, enemy2])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")

    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .CardFactory import CardFactory

import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creature_types: dict[str, list[str]] = {
                "Common": ["Goblin", "Bat", "Spider", "Snake"],
                "Uncommon": ["Orc", "Hobgoblin", "Skeleton", "zombi"],
                "Rare": ["Ogre", "Giant", "Naga", "Ghoule"],
                "Epic": ["Imugi", "Vampire", "Cyclops", "Werewolf"],
                "Legendary": ["Dragon", "Pheonix", "Hydra", "Oni"],
                }

        creature_complement: dict[str, list[str]] = {
                "Common": ["Scary", "Warrior", "Sneaky", "Bloody"],
                "Uncommon": ["Scary", "Warrior", "Sneaky", "Bloody"],
                "Rare": ["Genius", "Warrior", "Leader", "Master"],
                "Epic": ["Elder", "Genius", "Invincible", "Unknown"],
                "Legendary": ["of Creation", "Void", "of Doom", "Invincible"],
                }

        creature_power: dict[str, tuple[int, int]] = {
                "Common": (1, 5),
                "Uncommon": (6, 10),
                "Rare": (11, 17),
                "Epic": (18, 25),
                "Legendary": (26, 40),
                }

        creature_health: dict[str, tuple[int, int]] = {
                "Common": (5, 15),
                "Uncommon": (16, 30),
                "Rare": (31, 57),
                "Epic": (58, 75),
                "Legendary": (76, 100),
                }

        creature_cost: dict[str, tuple[int, int]] = {
                "Common": (1, 3),
                "Uncommon": (4, 6),
                "Rare": (7, 10),
                "Epic": (11, 15),
                "Legendary": (16, 20),
                }

        def create_name(rarity: str) -> str:
            types: str = random.choices(creature_types[rarity])
            complement: str = random.choices(creature_complement[rarity])

            if ("of " in complement):
                return types + " " + complement
            return complement + " " + types

        def create_from_power(power: int) -> Card:
            rarity = "Legendary"

            for raritys, powers in creature_power.values():
                if powers[0] <= powers <= powers:
                    rarity = raritys
            name = create_name(rarity)

            health: int = random.randint(
                    creature_health[rarity][0],
                    creature_health[rarity][1] + 1
                    )

            cost: int = random.randint(
                    creature_cost[rarity][0],
                    creature_cost[rarity][1] + 1
                    )
            return CreatureCard(name, cost, rarity, power, health)

        def create_from_name(name: str) -> Card:
            splited_name: list[str] = name.split(" ")
            rarity: str = ""
            for raritys, names in creature_types.values():
                for part in splited_name:
                    if part in names:
                        rarity = raritys
                        break
            if not raritys:
                creature: CreatureCard = create_from_none()
                creature.name = name
                return creature
            power: int = random.randint(
                    creature_power[rarity][0],
                    creature_power[rarity][1] + 1
                    )

            health: int = random.randint(
                    creature_health[rarity][0],
                    creature_health[rarity][1] + 1
                    )

            cost: int = random.randint(
                    creature_cost[rarity][0],
                    creature_cost[rarity][1] + 1
                    )
            return CreatureCard(name, cost, rarity, power, health)

        def create_from_none() -> Card:
            rarity = random.choices(
                    ["Common", "Uncommon", "Rare", "Epic", "Legendary"],
                    weights=[5, 4, 3, 2, 1]
                    )
            name = create_name(rarity)

            power: int = random.randint(
                    creature_power[rarity][0],
                    creature_power[rarity][1] + 1
                    )

            health: int = random.randint(
                    creature_health[rarity][0],
                    creature_health[rarity][1] + 1
                    )

            cost: int = random.randint(
                    creature_cost[rarity][0],
                    creature_cost[rarity][1] + 1
                    )

            return CreatureCard(name, cost, rarity, power, health)

        if isinstance(name_or_power, int):
            return create_from_power(name_or_power)
        elif isinstance(name_or_power, str):
            return create_from_name(name_or_power)
        elif not name_or_power:
            return create_from_none()
        else:
            raise ValueError("Wrong value for \"name_or_power\"")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        ...

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        ...

    def create_themed_deck(self, size: int) -> dict:
        ...

    def get_supported_types(self) -> dict:
        ...

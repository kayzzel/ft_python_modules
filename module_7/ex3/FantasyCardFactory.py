#!/usr/bin/env python3

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory

import random
from typing import Callable


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
            types: str = random.choice(creature_types[rarity])
            complement: str = random.choice(creature_complement[rarity])

            if ("of " in complement):
                return types + " " + complement

            return complement + " " + types

        def create_from_power(power: int) -> Card:
            rarity = "Legendary"

            for raritys, (min_p, max_p) in creature_power.items():
                if min_p <= power <= max_p:
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
            rarity: str = random.choices(
                    ["Common", "Uncommon", "Rare", "Epic", "Legendary"],
                    weights=[5, 4, 3, 2, 1],
                    k=1
                    )[0]
            name: str = create_name(rarity)

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

        spell_types: dict[str, list[str]] = {
            "Common": [
                "Spark", "Minor Heal", "Frost Touch", "Poison Mist"
                ],
            "Uncommon": [
                "Fireball", "Greater Heal", "Shadow Strike", "Ice Shard"
                ],
            "Rare": [
                "Chain Lightning", "Revitalize", "Soul Drain", "Meteor Shard"
                ],
            "Epic": [
                "Inferno", "Mass Heal", "Void Blast", "Blizzard"
                ],
            "Legendary": [
                "Apocalypse", "Divine Blessing", "World Ender", "Eternal Light"
                ],
        }

        spell_power: dict[str, tuple[int, int]] = {
            "Common": (1, 5),
            "Uncommon": (6, 10),
            "Rare": (11, 18),
            "Epic": (19, 30),
            "Legendary": (31, 50),
        }

        spell_cost: dict[str, tuple[int, int]] = {
            "Common": (1, 3),
            "Uncommon": (4, 6),
            "Rare": (7, 10),
            "Epic": (11, 15),
            "Legendary": (16, 20),
        }

        def create_name(rarity: str) -> str:
            return random.choice(spell_types[rarity])

        def create_from_power(power: int) -> Card:
            rarity = "Legendary"

            for raritys, (min_p, max_p) in spell_power.items():
                if min_p <= power <= max_p:
                    rarity = raritys

            name = create_name(rarity)

            effect: str = f"deal {power} damage"
            if "Divine" in name or "Heal" in name:
                effect = f"heal {power} health"

            cost = random.randint(
                spell_cost[rarity][0],
                spell_cost[rarity][1]
            )

            return SpellCard(name, cost, rarity, effect)

        def create_from_name(name: str) -> Card:
            rarity = None
            for raritys, names in spell_types.items():
                if name in names:
                    rarity = raritys
                    break

            if rarity is None:
                spell: SpellCard = create_from_none()
                spell.name = name
                return spell

            power = random.randint(
                spell_power[rarity][0],
                spell_power[rarity][1] + 1
            )

            effect: str = f"deal {power} damage"
            if "Divine" in name or "Heal" in name:
                effect = f"heal {power} health"

            cost = random.randint(
                spell_cost[rarity][0],
                spell_cost[rarity][1] + 1
            )

            return SpellCard(name, cost, rarity, effect)

        def create_from_none() -> Card:
            rarity = random.choices(
                ["Common", "Uncommon", "Rare", "Epic", "Legendary"],
                weights=[5, 4, 3, 2, 1],
                k=1
            )[0]

            name = create_name(rarity)

            power = random.randint(
                spell_power[rarity][0],
                spell_power[rarity][1] + 1
            )

            effect: str = f"deal {power} damage"
            if "Divine" in name or "Heal" in name:
                effect = f"heal {power} health"

            cost = random.randint(
                spell_cost[rarity][0],
                spell_cost[rarity][1] + 1
            )

            return SpellCard(name, cost, rarity, effect)

        if isinstance(name_or_power, int):
            return create_from_power(name_or_power)
        elif isinstance(name_or_power, str):
            return create_from_name(name_or_power)
        elif name_or_power is None:
            return create_from_none()
        else:
            raise ValueError('Wrong value for "name_or_power"')

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:

        artifact_types: dict[str, list[str]] = {
            "Common": ["Wooden Wand", "Rusty Blade", "Old Amulet"],
            "Uncommon": ["Enchanted Ring", "Crystal Orb", "Steel Relic"],
            "Rare": ["Ancient Tome", "Runed Blade", "Sacred Idol"],
            "Epic": ["Cursed Crown", "Orb of Eternity", "Demon Relic"],
            "Legendary": ["World Shard", "Divine Relic", "Core of Creation"],
        }

        artifact_power: dict[str, tuple[int, int]] = {
            "Common": (1, 5),
            "Uncommon": (6, 10),
            "Rare": (11, 18),
            "Epic": (19, 30),
            "Legendary": (31, 50),
        }

        artifact_cost: dict[str, tuple[int, int]] = {
            "Common": (1, 3),
            "Uncommon": (4, 6),
            "Rare": (7, 10),
            "Epic": (11, 15),
            "Legendary": (16, 20),
        }

        artifact_durability: dict[str, tuple[int, int]] = {
            "Common": (1, 3),
            "Uncommon": (2, 4),
            "Rare": (3, 6),
            "Epic": (4, 8),
            "Legendary": (5, 10),
        }

        effect_templates = [
            "deal {power} damage",
            "heal {power} health",
            "restore {power} mana"
        ]

        def create_from_power(power: int) -> Card:
            rarity: str = "Legendary"

            for raritys, (min_p, max_p) in artifact_power.items():
                if min_p <= power <= max_p:
                    rarity = raritys

            name: str = random.choice(artifact_types[rarity])

            effect: str = random.choice(effect_templates).format(power=power)

            cost: int = random.randint(
                artifact_cost[rarity][0],
                artifact_cost[rarity][1] + 1
            )

            durability: int = random.randint(
                artifact_durability[rarity][0],
                artifact_durability[rarity][1] + 1
            )

            return ArtifactCard(name, cost, rarity, durability, effect)

        def create_from_name(name: str) -> Card:
            rarity = None
            for r, names in artifact_types.items():
                if name in names:
                    rarity = r
                    break

            if rarity is None:
                artifac: ArtifactCard = create_from_none()
                artifac.name = name
                return artifac

            power: int = random.randint(
                artifact_power[rarity][0],
                artifact_power[rarity][1] + 1
            )

            effect = random.choice(effect_templates).format(power=power)

            cost: int = random.randint(
                artifact_cost[rarity][0],
                artifact_cost[rarity][1] + 1
            )

            durability: int = random.randint(
                artifact_durability[rarity][0],
                artifact_durability[rarity][1] + 1
            )

            return ArtifactCard(name, cost, rarity, durability, effect)

        def create_from_none() -> Card:
            rarity = random.choices(
                ["Common", "Uncommon", "Rare", "Epic", "Legendary"],
                weights=[5, 4, 3, 2, 1],
                k=1
            )[0]

            name = random.choice(artifact_types[rarity])

            power: int = random.randint(
                artifact_power[rarity][0],
                artifact_power[rarity][1] + 1
            )

            effect = random.choice(effect_templates).format(power=power)

            cost: int = random.randint(
                artifact_cost[rarity][0],
                artifact_cost[rarity][1] + 1
            )

            durability: int = random.randint(
                artifact_durability[rarity][0],
                artifact_durability[rarity][1] + 1
            )

            return ArtifactCard(name, cost, rarity, durability, effect)

        if isinstance(name_or_power, int):
            return create_from_power(name_or_power)
        elif isinstance(name_or_power, str):
            return create_from_name(name_or_power)
        elif name_or_power is None:
            return create_from_none()
        else:
            raise ValueError('Wrong value for "name_or_power"')

    def create_themed_deck(self, size: int) -> dict:
        created_card: dict[str, list[Card]] = {
                "creatures": [],
                "spells": [],
                "artifacts": []
                }
        for _ in range(size):
            create_card: Callable = random.choice([
                lambda:
                created_card["creatures"].append(self.create_creature()),
                lambda:
                created_card["spells"].append(self.create_spell()),
                lambda:
                created_card["artifacts"].append(self.create_artifact())
                ])
            create_card()

        created_card["all_card"] = [
                created_card["creatures"] +
                created_card["spells"] +
                created_card["artifacts"]
                ]

        return created_card

    def get_supported_types(self) -> dict:
        return {
            "creature": self.create_creature,
            "spell": self.create_spell,
            "artifact": self.create_artifact
        }

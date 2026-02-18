#!/usr/bin/env python3

from . import Card

from typing_extensions import override


class ArtifactCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
            ) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect
        self.played = False

    @override
    def get_card_info(self) -> dict:
        return {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "durability": self.durability,
                "effect": self.effect
                }

    def play(self, game_state: dict) -> dict:
        if self.played:
            print(f"Spell {self.name} already played")
        elif not self.is_playable(game_state["available_mana"]):
            print(f"Not enougth mana to play {self.name} need at least\
{self.cost} mana")
            print(f"Available mana: {game_state['available_mana']}")
        else:
            self.played = True
            return {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": self.effect
                    }
        return {}

    def activate_ability(self, targets: list | None = None) -> dict:
        if not self.played:
            print(f"{self.name} is not in play.")
            return {}

        if self.durability <= 0:
            print(f"{self.name} has no durability left.")
            return {}

        try:
            power = int([s for s in self.effect.split() if s.isdigit()][0])
        except Exception:
            print("ERROR: No numeric value found in artifact effect.")
            return {}

        result = {
            "artifact": self.name,
            "effect": self.effect,
            "durability_before": self.durability
        }

        # Apply effect
        if "damage" in self.effect and targets:
            total_damage = 0
            killed = 0
            for target in targets:
                if hasattr(target, "health") and target.played:
                    target.health -= power
                    total_damage += power
                    if target.health <= 0:
                        killed += 1

            result.update({
                "total_damage": total_damage,
                "targets_killed": killed
            })

        elif "heal" in self.effect and targets:
            total_heal = 0
            healed = 0
            for target in targets:
                if hasattr(target, "health") and target.played:
                    target.health += power
                    total_heal += power
                    healed += 1

            result.update({
                "total_heal": total_heal,
                "targets_healed": healed
            })

        elif "mana" in self.effect:
            result.update({
                "mana_restored": power
            })

        # Reduce durability
        self.durability -= 1
        result["durability_after"] = self.durability

        return result

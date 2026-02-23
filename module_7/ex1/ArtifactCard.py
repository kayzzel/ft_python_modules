#!/usr/bin/env python3

from . import Card


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
        self.__played = False

        self.attack: int = [
                int(s) for s in self.effect.split() if s.isdigit()
                ][0]

    @property
    def played(self) -> bool:
        return self.__played

    @played.setter
    def played(self, played: bool) -> None:
        raise ValueError("Can't change played from the outside")

    def get_card_info(self) -> dict:
        return {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "attack": self.attack,
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
            self.__played = True
            game_state["available_mana"] -= self.cost

            card_index: int = next(
                    (
                        i for i, c in enumerate(game_state["hand"])
                        if c.name == self.name
                        ),
                    None)
            game_state["board"].append(game_state["hand"].pop(card_index))
            return {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": self.effect
                    }
        return {}

    def activate_ability(self, targets: list | None = None) -> dict:
        if not self.played:
            print("/!\\ Error: played")
            return {}

        if self.durability <= 0:
            print("/!\\ Error: durability")
            return {}

        self.durability -= 1

        # Apply effect
        if ("mana" in self.effect or "heal" in self.effect) and targets:
            total_heal = 0
            healed = 0
            for target in targets:
                if hasattr(target, "health") and target.played:
                    target.health += self.attack
                    total_heal += self.attack
                    healed += 1

            return {
                "artifact": self.name,
                "effect": self.effect,
                "durability_before": self.durability + 1,
                "durability_after": self.durability,
                "total_heal": total_heal,
                "targets_healed": healed
            }

        total_damage: int = 0
        killed: list = []
        for target in targets:
            if hasattr(target, "health") and target.played:
                target.health -= self.attack
                total_damage += self.attack
                if target.health <= 0:
                    killed.append(target)

        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_before": self.durability,
            "durability_after": self.durability,
            "total_damage": total_damage,
            "targets_killed": killed
        }

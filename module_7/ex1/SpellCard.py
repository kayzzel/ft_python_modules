#!/usr/bin/env python3

from . import Card


class SpellCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str
                 ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type
        self.played: bool = False
        self.used: bool = False

    def play(self, game_state: dict) -> dict:
        if self.played:
            print(f"Spell {self.name} already consumed")
        elif not self.is_playable(game_state["available_mana"]):
            print(f"Not enougth mana to play {self.name} need at least\
{self.cost} mana")
            print(f"Available mana: {game_state['available_mana']}")
        else:
            self.played = True
            return {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": self.effect_type
                    }
        return {}

    def resolve_effect(self, targets: list) -> dict:

        if not self.played:
            print("Can't use a spell that is not played")
            return {}

        if self.used:
            print()
            return {}

        try:
            power: int = [
                    int(s) for s in self.effect_type.split() if s.isdigit()
                    ][0]
        except Exception:
            print("ERROR: No power in the effect")
            return {}
        else:
            if "heal" in self.effect_type:
                total_heal: int = 0
                healed: int = 0
                for target in targets:
                    if target.played:
                        target.health += power
                        healed += 1
                        total_heal += power
                return {
                        "effect": self.effect_type,
                        "targets": targets,
                        "healed_target": healed,
                        "total_heal": total_heal
                        }

            killed: int = 0
            total_damage: int = 0
            for target in targets:
                if target.played:
                    target.health += power
                    total_damage += power
                    if target.health <= 0:
                        killed += 1
            return {
                    "effect": self.effect_type,
                    "targets": targets,
                    "targets_killed": killed,
                    "total_damage": total_heal
                    }

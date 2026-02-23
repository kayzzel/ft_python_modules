#!/usr/bin/env python3

from ex0.Card import Card


class SpellCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str
                 ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type
        self.__played: bool = False
        self.used: bool = False

        self.attack: int = [
                int(s) for s in self.effect_type.split() if s.isdigit()
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
                "effect_type": self.effect_type
                }

    def play(self, game_state: dict) -> dict:
        if self.__played:
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
                    "effect": self.effect_type
                    }
        return {}

    def resolve_effect(self, targets: list) -> dict:

        if not self.__played:
            print("/!\\ Error: played")
            return {}

        if self.used:
            print("/!\\ Error: used")
            return {}
        self.used = True
        if "heal" in self.effect_type:
            total_heal: int = 0
            healed: int = 0
            for target in targets:
                if target.played:
                    target.health += self.attack
                    healed += 1
                    total_heal += self.attack
            return {
                    "effect": self.effect_type,
                    "targets": targets,
                    "healed_target": healed,
                    "total_heal": total_heal
                    }

        killed: list = []
        total_damage: int = 0
        for target in targets:
            if target.played:
                target.health -= self.attack
                total_damage += self.attack
                if target.health <= 0:
                    killed.append(target)
        return {
                "effect": self.effect_type,
                "targets": targets,
                "targets_killed": killed,
                "total_damage": total_damage
                }

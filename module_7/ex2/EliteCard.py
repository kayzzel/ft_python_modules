#!/usr/bin/env python3

from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            health: int,
            attack_damage: int,
            defence: int,
            magical_attack: int,
            magical_defence: int,
            known_spell: dict[str, int]
            ) -> None:
        super().__init__(name, cost, rarity)

        self.health: int = health

        self.attack_damage: int = attack_damage
        self.defence: int = defence

        self.magical_attack: int = magical_attack
        self.magical_defence: int = magical_defence
        self.known_spell: dict[str, int] = known_spell

        self.__played: bool = False
        self.__mana_chanelled: int = 0

    @property
    def attack_damage(self) -> int:
        return self.__attack

    @attack_damage.setter
    def attack_damage(self, attack: int) -> None:
        if not isinstance(attack, int):
            raise ValueError(f"{attack} is not an integer")
        elif not isinstance(attack, int):
            raise ValueError(f"{attack} is not an positive number")
        else:
            self.__attack = attack

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int) -> None:
        if not isinstance(health, int):
            raise ValueError(f"{health} is not an integer")
        else:
            self.__health = health

    @property
    def played(self) -> bool:
        return self.__played

    @played.setter
    def played(self, played: bool) -> None:
        raise ValueError("Can't change \"played\" from the outside")

    def play(self, game_state: dict) -> dict:
        if self.played:
            print(f"Card {self.name} already played")
        elif not self.is_playable(game_state["available_mana"]):
            print(f"Not enougth mana to play {self.name} need at least\
{self.cost} mana")
            print(f"Available mana: {game_state['available_mana']}")
        else:
            game_state["available_mana"] -= self.cost
            self.__played = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
                }
        return {}

    def attack(self, target) -> dict:
        if not self.__played:
            print(f"Card {self.name} need to be played to attack")
        elif not target.played:
            print(f"Cannot attack! {target.name} is not played")
        else:
            target.health -= self.attack_damage
            return {
                    "attacker": self.name,
                    "target": target.name,
                    "damage_dealt": self.attack_damage,
                    "combat_type": "melee"
                    }
        return {}

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked: int = self.defence
        if incoming_damage - damage_blocked < 0:
            damage_blocked = incoming_damage
        self.health -= incoming_damage - damage_blocked
        return {
                "defender": self.name,
                "domage_taken": incoming_damage - damage_blocked,
                "domage_blocked": damage_blocked,
                "still_alive": self.health > 0
                }

    def get_combat_stats(self) -> dict:
        return {
                "health": self.health,
                "attack": self.attack_damage,
                "defence": self.defence
                }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not isinstance(targets, list) or len(targets) < 1:
            print("Not enought enemy!")
        if spell_name in self.known_spell.keys():
            if self.__mana_chanelled >= self.known_spell[spell_name]:
                self.__mana_chanelled -= self.known_spell[spell_name]
                return {
                        "caster": self.name,
                        "spell": spell_name,
                        "targets": [target.name for target in targets],
                        "mana_used": self.known_spell[spell_name]
                        }
            else:
                print(
                        f"Not enought mana chanelled to cast {spell_name}\n"
                        f"Mana needed: {self.known_spell[spell_name]}"
                      )
        else:
            print(f"{spell_name} is not known by {self.name}")
        return {}

    def channel_mana(self, amount: int) -> dict:
        self.__mana_chanelled += amount
        return {
                "chaneled": amount,
                "total_mana": self.__mana_chanelled
                }

    def get_magic_stats(self) -> dict:
        return {
                "health": self.health,
                "magical_attack": self.magical_attack,
                "magical_defence": self.magical_defence,
                "mana_chanelled": self.__mana_chanelled
                }

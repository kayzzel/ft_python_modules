from . import Card
from typing_extensions import override


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
            ) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health
        self.played: bool = False

    @property
    def attack(self) -> int:
        return self.__attack

    @attack.setter
    def attack(self, attack: int) -> None:
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
        elif not isinstance(health, int):
            raise ValueError(f"{health} is not an positive number")
        else:
            self.__health = health

    @override
    def get_card_info(self) -> dict:
        return {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": "Creature",
                "attack": self.attack,
                "health": self.health
                }

    def play(self, game_state: dict) -> dict:
        if self.played:
            print(f"Card {self.name} already played")
        elif not self.is_playable(game_state["available_mana"]):
            print(f"Not enougth mana to play {self.name} need at least\
{self.cost} mana")
            print(f"Available mana: {game_state['available_mana']}")
        else:
            game_state["available_mana"] -= self.cost
            self.played = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
                }
        return {}

    def attack_target(self, target) -> dict:
        if not self.played:
            print(f"Card {self.name} need to be played to attack")
        elif not target.played:
            print(f"Cannot attack! {target.name} is not played")
        else:
            target.health -= self.attack
            return {
                    "attacker": self.name,
                    "target": target.name,
                    "damage_dealt": self.attack,
                    "combat_resolved": target.health <= 0
                    }
        return {}

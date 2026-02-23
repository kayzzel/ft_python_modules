#!/usr/bin/env python3

from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
            ) -> None:
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.health = health

        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name}

    def attack(self, target) -> dict:
        damage = self.attack_power
        result = target.defend(damage)

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": damage,
            "target_remaining_health": result["remaining_health"]
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {
            "remaining_health": self.health
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

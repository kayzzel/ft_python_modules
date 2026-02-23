#!/usr/bin/env python3

from .TournamentCard import TournamentCard
import random


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.lower().replace(' ', '_')}_{len(self.cards)+1}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner, loser = random.choice(
            [(card1, card2), (card2, card1)]
        )

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": card1_id if winner == card1 else card2_id,
            "loser": card2_id if winner == card1 else card1_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        return sorted(
            self.cards.values(),
            key=lambda card: card.calculate_rating(),
            reverse=True
        )

    def generate_tournament_report(self) -> dict:
        avg_rating = sum(
            card.calculate_rating() for card in self.cards.values()
        ) / len(self.cards)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": int(avg_rating),
            "platform_status": "active"
        }

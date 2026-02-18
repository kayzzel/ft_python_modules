#!/usr/bin/env python3

from .GameStrategy import GameStrategy
from .CardFactory import CardFactory
from ex1.Deck import Deck
from ex0.Card import Card


class GameEngine:
    def __init__(self):
        self.__configured: bool = False
        self.__game: dict = {}

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy
            ) -> None:
        if self.__configured:
            print("ERROR: Game Engine Already configured")

        if not (isinstance(factory, CardFactory)
                and isinstance(strategy, GameStrategy)):
            print("ERROR: Wrong type of factory/strategy!")
            return None

        self.__factory = factory
        self.__strategy = strategy
        self.__configured = True

        def create_player(factory: CardFactory) -> dict:
            name: str = input("what is your username: ")

            deck: Deck = Deck()

            for card in factory.create_themed_deck(15)["all_card"]:
                deck.add_card(card)

            deck.shuffle()

            hand: list[Card] = [deck.draw_card() for _ in range(5)]

            return {
                    "name": name,
                    "deck": deck,
                    "hand": hand,
                    "board": [],
                    "available_mana": 10
                    }

        self.__game["player1"] = create_player(self.factory)
        self.__game["player2"] = create_player(self.factory)
        self.__game["turn_nbr"] = 0

    def simulate_turn(self) -> dict:
        ...

    def get_engine_status(self) -> dict:
        status: dict = self.game
        status["factory"] = self.factory
        status["strategy"] = self.strategy
        return status

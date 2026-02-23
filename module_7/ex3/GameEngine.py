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
            self,
            factory: CardFactory,
            strategy: GameStrategy
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

        def create_player(factory: CardFactory, player: str) -> dict:
            name: str = player

            deck: Deck = Deck()

            for card in factory.create_themed_deck(15)["all_card"]:
                deck.add_card(card)

            deck.shuffle()

            hand: list[Card] = [deck.draw_card() for _ in range(5)]

            return {
                    "name": name,
                    "health": 5,
                    "deck": deck,
                    "hand": hand,
                    "board": [],
                    "active_artifacts": [],
                    "available_mana": 15
                    }

        self.__game["player1"] = create_player(self.__factory, "player1")
        self.__game["player2"] = create_player(self.__factory, "player2")
        self.__game["turn_nbr"] = 0

    def simulate_turn(self) -> dict:
        turn_result: dict = {}

        self.__game["turn_nbr"] += 1

        turn_result["player1"] = self.__strategy.execute_turn(
                self.__game["player1"]["hand"],
                [self.__game, "player1", "player2"]
                )
        self.__game["player1"]["available_mana"] += 10

        turn_result["player2"] = self.__strategy.execute_turn(
                self.__game["player2"]["hand"],
                [self.__game, "player2", "player1"]
                )
        self.__game["player2"]["available_mana"] += 10

        turn_result["turn_nbr"] = self.__game["turn_nbr"]

        return turn_result

    def get_engine_status(self) -> dict:
        status: dict = self.__game
        status["factory"] = self.__factory
        status["strategy"] = self.__strategy
        return status

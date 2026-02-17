#!/usr/bin/env python3

from .GameStrategy import GameStrategy
from .CardFactory import CardFactory


class GameEngine:
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        ...

    def simulate_turn(self) -> dict:
        ...

    def get_engine_status(self) -> dict:
        ...

#!/usr/bin/env python3

from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        ...

    def get_strategy_name(self) -> str:
        ...

    def prioritize_targets(self, available_targets: list) -> list:
        ...

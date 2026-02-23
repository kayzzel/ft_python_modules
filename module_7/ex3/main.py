#!/usr/bin/env python3

from ex0.Card import Card
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


def main():
    factorie: FantasyCardFactory = FantasyCardFactory()
    strategy: AggressiveStrategy = AggressiveStrategy()

    game_engine: GameEngine = GameEngine()

    game_engine.configure_engine(factorie, strategy)

    status: dict = game_engine.get_engine_status()

    for player in ["player1", "player2"]:
        print(f"player name: {status[player]['name']}")
        print(f"player health: {status[player]['health']}")
        print("player hand:")
        print("\n".join(
            str(card.get_card_info()) for card in status[player]['hand']
            ))
        print()

    next_turn = True
    while (next_turn):
        if input("continue (y/N) ") not in ["y", "Y"]:
            next_turn = False
            break
        turn: dict = game_engine.simulate_turn()

        print(f"turn: {turn['turn_nbr']}")
        for player in ["player1", "player2"]:
            print(f"player turn: {status[player]['name']}")
            print(f"player health: {status[player]['health']}")
            print(f"player mana: {status[player]['available_mana']}")
            if turn[player]["card_draw"]:
                print("\ncard draw:")
                print("\n".join(
                    str(card.get_card_info())
                    if isinstance(card, Card) else
                    card
                    for card in turn[player]["card_draw"]
                    ))
            if turn[player]["played_card"]:
                print("\nplayed card:")
                print("\n".join(
                    attack for attack in turn[player]["played_card"]
                    ))
            if turn[player]["attacks"]:
                print("\nattacks:")
                print("\n".join(
                    attack for attack in turn[player]["attacks"]
                    ))
            if turn[player]["artifacts"]:
                print("\nartifacts:")
                print("\n".join(
                    artifact for artifact in turn[player]["artifacts"]
                    ))
            if turn[player]["enemy_died"]:
                print()
                print(f"player {status[player]['name']} won")
                return ()
            print("\n")


if __name__ == "__main__":
    main()

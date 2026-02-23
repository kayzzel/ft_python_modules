#!/usr/bin/env python3

from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard


def main():

    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 8, 30)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 6, 25)

    print()
    print("Registering Tournament Cards...")

    id1 = platform.register_card(dragon)
    id2 = platform.register_card(wizard)

    print(
            f"\n{dragon.name} (ID: {id1}):\n"
            "- Interface: [Card, Combatable, Rankable]\n"
            f"- Rating: {dragon.calculate_rating()}\n"
            f"- Record: {dragon.get_rank_info()['wins']}-"
            f"{dragon.get_rank_info()['losses']}"
        )

    print(
            f"\n{wizard.name} (ID: {id1}):\n"
            "- Interface: [Card, Combatable, Rankable]\n"
            f"- Rating: {wizard.calculate_rating()}\n"
            f"- Record: {wizard.get_rank_info()['wins']}-"
            f"{wizard.get_rank_info()['losses']}"
        )

    print("\nCreating tournament match...")
    result = platform.create_match(id1, id2)

    print("Match result:", result)

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        stats = card.get_tournament_stats()
        print(
                f"{i}. {stats['name']} "
                f"- Rating: {stats['rating']} ({stats['record']})"
            )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously")


if __name__ == "__main__":
    main()

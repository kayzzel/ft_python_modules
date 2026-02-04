#!/usr/bin/env python3

def display_players_achivements(players: dict[str, set[str]]) -> None:
    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")


def achievement_rarity(players: dict[str, set[str]]) -> None:
    first: bool = True

    for achievements in players.values():
        if first:
            all_a: set[str] = achievements
            common: set[str] = achievements
            rare: set[str] = achievements
            first = False
        else:
            common = common.intersection(achievements)
            rare = (rare - achievements).union(achievements - all_a)
            all_a = all_a.union(achievements)

    print(f"All unique achievements: {all_a}")
    print("Total unique achievements:", len(all_a))

    print()
    print(f"Common to all players: {common if len(common) > 0 else 'None'}")
    print(f"Rare achievements (1 player): {rare if len(rare) > 0 else 'None'}")


def achievement_comp(
    name1: str,
    set1: set[str],
    name2: str,
    set2: set[str]
) -> None:
    print(f"{name1} vs {name2} common: {set1.intersection(set2)}")
    print(f"{name1} unique: {set1.difference(set2)}")
    print(f"{name2} unique: {set2.difference(set1)}")


def main() -> None:
    players: dict[str, set[str]] = {
            "Alice":
            set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']),
            "Bob":
            set(['first_kill', 'level_10', 'boss_slayer', 'collector']),
            "Charlie":
            set(['level_10', 'treasure_hunter', 'boss_slayer',
                 'speed_demon', 'perfectionist'])
            }

    print("=== Achievement Tracker System ===")

    print()
    display_players_achivements(players)

    print()
    print("=== Achievement Analytics ===")
    achievement_rarity(players)

    print()
    achievement_comp("Alice", players["Alice"],
                     "Bob", players["Bob"])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def display_players_achivements(players: dict[str, set[str]]) -> None:
    """
    Display each player's achievements.

    Args:
        players (dict[str, set[str]]): Dictionary mapping player names
        to their set of achievements.

    Returns:
        None
    """
    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")


def all_achievements(players: dict[str, set[str]]) -> None:
    """
    Display all unique achievements across all players.

    Args:
        players (dict[str, set[str]]): Dictionary mapping player names
        to their set of achievements.

    Returns:
        None
    """
    total_achievements: set[str] = set()

    for achievements in players.values():
        total_achievements = total_achievements.union(achievements)

    print(f"All unique achievements: {total_achievements}")
    print("Total unique achievements:", len(total_achievements))


def achievement_rarity(players: dict[str, set[str]]) -> None:
    """
    Determine common and rare achievements among players.

    - Common achievements: obtained by all players
    - Rare achievements: obtained by only one player

    Args:
        players (dict[str, set[str]]): Dictionary mapping player names
        to their set of achievements.

    Returns:
        None
    """
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

    print(f"Common to all players: {common if len(common) > 0 else 'None'}")
    print(f"Rare achievements (1 player): {rare if len(rare) > 0 else 'None'}")


def achievement_comp(
    name1: str,
    set1: set[str],
    name2: str,
    set2: set[str]
) -> None:
    """
    Compare achievements between two players.

    Displays:
      - Common achievements
      - Achievements unique to each player

    Args:
        name1 (str): First player's name.
        set1 (set[str]): First player's achievements.
        name2 (str): Second player's name.
        set2 (set[str]): Second player's achievements.

    Returns:
        None
    """
    print(f"{name1} vs {name2} common: {set1.intersection(set2)}")
    print(f"{name1} unique: {set1.difference(set2)}")
    print(f"{name2} unique: {set2.difference(set1)}")


if __name__ == "__main__":

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
    all_achievements(players)

    print()
    achievement_rarity(players)

    print()
    achievement_comp("Alice", players["Alice"],
                     "Bob", players["Bob"])

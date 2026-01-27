#!/usr/bin/env python3

class Player:
    """
    Represents a player with name, score, active region, and achievements.
    """

    def __init__(
        self,
        name: str,
        score: int,
        active_region: str,
        achievements: set[str]
    ) -> None:
        """
        Initialize a Player instance.

        Args:
            name (str): Player name.
            score (int): Player score.
            active_region (str): Player active region.
            achievements (set[str]): Set of player achievements.
        """
        self.name: str = name
        self.score: int = score
        self.active_region: str = active_region
        self.achievements: set[str] = achievements


def list_comprehension(players: list[Player]) -> None:
    """
    Demonstrate list comprehension-like operations using loops.

    Args:
        players (list[Player]): List of Player objects.

    Returns:
        None
    """
    hight_scorer: list[str] = []
    doubled_score: list[int] = []
    active_player: list[str] = []

    for player in players:
        if player.score > 2000:
            hight_scorer += [player.name]
        doubled_score += [(player.score * 2)]
        if player.active_region != "":
            active_player += [player.name]

    print("=== List Comprehension Examples ===")
    print(f"Hight scorers (>2000): {hight_scorer}")
    print(f"Scores doubled: {doubled_score}")
    print(f"Active players: {active_player}")


def dict_comprehension(players: list[Player]) -> None:
    """
    Demonstrate dictionary comprehension-like operations using loops.

    Args:
        players (list[Player]): List of Player objects.

    Returns:
        None
    """
    player_score: dict[str, int] = {}
    achivement_count: dict[str, int] = {}

    for player in players:
        player_score[player.name] = player.score
        if player.active_region != "":
            achivement_count[player.name] = len(player.achievements)

    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_score}")
    print(f"Achievement count: {achivement_count}")


def set_comprehension(players: list[Player]) -> None:
    """
    Demonstrate set comprehension-like operations using loops.

    Args:
        players (list[Player]): List of Player objects.

    Returns:
        None
    """
    player_name: set[str] = set()
    active_region: set[str] = set()
    all_a: set[str] = set()
    rare: set[str] = set()

    for player in players:
        player_name = player_name.union([player.name])
        rare = (rare - player.achievements).union(player.achievements - all_a)
        all_a = all_a.union(player.achievements)
        if player.active_region != "":
            active_region = active_region.union([player.active_region])

    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {player_name}")
    print(f"Unique achievements: {rare}")
    print(f"Active regions: {active_region}")


def combine_analytics(players: list[Player]) -> None:
    """
    Combine multiple analytics into one output.

    Args:
        players (list[Player]): List of Player objects.

    Returns:
        None
    """
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: \
{len({ach for player in players for ach in player.achievements})}")
    print(f"Average score: \
{sum([player.score for player in players]) / len(players)}")
    print(f"Top performer: \
{(best:=max(players, key=lambda p: p.score)).name}  \
({best.score} points, {len(best.achievements)} achievements)")


if __name__ == "__main__":

    players: list[Player] = [
            Player("alice", 2300, "north",
                   set(
                       ['first_kill', 'level_10',
                        'treasure_hunter', 'speed_demon']
                       )),
            Player("bob", 1800, "east",
                   set(
                       ['first_kill', 'level_10',
                        'boss_slayer', 'collector']
                       )),
            Player("charlie", 2150, "central",
                   set(
                       ['level_10', 'treasure_hunter', 'boss_slayer']
                       )),
            Player("diana", 2050, "",
                   set(
                       ['level_10', 'treasure_hunter', 'boss_slayer',
                        'speed_demon', 'perfectionist']
                       ))
            ]

    print("=== Game Analytics Dashboard ===")

    print()
    list_comprehension(players)

    print()
    dict_comprehension(players)

    print()
    set_comprehension(players)

    print()
    combine_analytics(players)

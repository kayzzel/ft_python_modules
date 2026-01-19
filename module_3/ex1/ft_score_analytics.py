import sys
from typing import List


def score_analytics() -> None:
    """
    Analyze and display basic statistics for player scores.

    Reads integer scores from command line arguments and prints:
      - list of scores
      - number of players
      - total score
      - average score
      - highest score
      - lowest score
      - score range

    If no scores are provided, it prints usage instructions.
    If a non-integer argument is found, it prints an error.

    Returns:
        None
    """
    print("=== Player Score Analytics ===")

    args: List[str] = sys.argv

    if len(args) <= 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return

    try:
        scores: List[int] = [int(score) for score in args[1:]]
    except ValueError as err:
        print("Error:", err)
    else:
        total_scores: int = sum(scores)
        average_score: float = total_scores / len(scores)
        high_score: int = max(scores)
        low_score: int = min(scores)
        score_range: int = high_score - low_score

        print(f"Scores Processed: {scores}")
        print(f"Total Player:     {len(scores)}")
        print(f"Total Score:      {total_scores}")
        print(f"Average Score:    {average_score}")
        print(f"High Score:       {high_score}")
        print(f"Low Score:        {low_score}")
        print(f"Score Range:      {score_range}")


if __name__ == "__main__":
    score_analytics()

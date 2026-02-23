# Global Variables
__all__: list[str] = [
    "Card",
    "CreatureCard",
    "SpellCard",
    "ArtifactCard",
    "Deck",
    "Combatable",
    "Magical",
    "EliteCard",
    "GameEngine",
    "GameStrategie",
    "CardFactory",
    "AggressiveStrategy",
    "FantasyCardFactory",
    "Rankable",
    "TournamentCard",
    "TournamentPlatform"
]


# Imports
from .ex0 import Card, CreatureCard

from .ex1 import SpellCard, ArtifactCard, Deck

from .ex2 import Combatable, Magical, EliteCard

from .ex3 import GameEngine
from .ex3 import GameStrategie, CardFactory
from .ex3 import AggressiveStrategy, FantasyCardFactory

from .ex4 import Rankable, TournamentCard, TournamentPlatform

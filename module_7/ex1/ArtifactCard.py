from . import Card


class ArtifactClass(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
            ) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect
        self.played = False

    def play(self, game_state: dict) -> dict:
        if self.played:
            print(f"Spell {self.name} already consumed")
        elif not self.is_playable(game_state["available_mana"]):
            print(f"Not enougth mana to play {self.name} need at least\
{self.cost} mana")
            print(f"Available mana: {game_state['available_mana']}")
        else:
            self.played = True
            return {
                    "card_played": self.name,
                    "mana_used": self.cost,
                    "effect": self.effect
                    }
        return {}

    def activate_ability(self) -> dict:
        return {}

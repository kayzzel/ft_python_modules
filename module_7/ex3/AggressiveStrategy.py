#!/usr/bin/env python3

from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:

        action_made: int = 0
        turn_result: dict = {
                "card_draw": [],
                "played_card": [],
                "attacks": [],
                "artifacts": [],
                "enemy_died": False
                }

        player: dict = battlefield[0][battlefield[1]]
        enemy: dict = battlefield[0][battlefield[2]]

        while (len(hand) < 5):
            card: Card = player["deck"].draw_card()
            if not card:
                turn_result["card_draw"].append(
                        "no more card to draw in the deck"
                        )
                break
            player["hand"].append(card)
            turn_result["card_draw"].append(card)

        if (len(player["board"]) < 2
                and player["deck"].get_deck_stats()["card_count"] > 0):
            cheapest: Card = min(
                    player["hand"],
                    key=lambda card: card.get_card_info()["cost"]
                    )

            if cheapest.get_card_info()["cost"] <= player["available_mana"]:
                cheapest.play(player)

                action_made += 1
                turn_result["played_card"].append(
                       f"played {cheapest.name} for {cheapest.cost} mana"
                        )
            else:
                turn_result["played_card"].append(
                    "not enought mana to play a card"
                    )

        if (battlefield[0]["turn_nbr"] == 1):
            cheapest: Card = min(
                    player["hand"],
                    key=lambda card: card.get_card_info()["cost"]
                    )

            if cheapest.get_card_info()["cost"] <= player["available_mana"]:
                cheapest.play(player)
                action_made += 1
                turn_result["played_card"].append(
                       f"played {cheapest.name} for {cheapest.cost} mana"
                        )
            return turn_result

        while (action_made < 2):
            if not player["board"]:
                return turn_result
            action_made += 1
            max_damage: Card = max(
                    player["board"],
                    key=lambda card: card.get_card_info()["attack"]
                    )
            targets = [
                    card for card in enemy["board"]
                    if isinstance(card, CreatureCard)
                       ]

            if not targets:
                enemy["health"] -= 1
                turn_result["attacks"].append(
                        f"{player['name']} inflicted one damage to "
                        f"{enemy['name']}"
                        )
                if enemy["health"] <= 0:
                    turn_result["enemy_died"] = True
                    return turn_result
                continue

            if isinstance(max_damage, CreatureCard):
                min_health: Card = max(
                        targets,
                        key=lambda card: card.get_card_info()["health"]
                    )
                result: dict = max_damage.attack_target(min_health)

                if result["combat_resolved"]:
                    card_index: int = next(
                            (
                                i for i, c in enumerate(enemy["board"])
                                if c == min_health
                                ),
                            None)

                    enemy["board"].pop(card_index)
                    turn_result["attacks"].append(
                            f"{max_damage.name} dealed {max_damage.attack} to "
                            f"{min_health.name}\n"
                            f"{max_damage.name} killed {min_health.name}"
                            )

                else:
                    turn_result["attacks"].append(
                            f"{max_damage.name} dealed {max_damage.attack} to "
                            f"{min_health.name}"
                            )

            elif isinstance(max_damage, SpellCard):
                card_index: int = next(
                        (
                            i for i, c in enumerate(player["board"])
                            if c == max_damage
                            ),
                        None)

                player["board"].pop(card_index)

                if "heal" not in max_damage.effect_type:
                    result: dict = max_damage.resolve_effect(targets)
                    if not result["targets_killed"]:
                        turn_result["attacks"].append(
                                f"{max_damage.name} dealt {max_damage.attack} "
                                f"to {[target.name for target in targets]} "
                                f"(total damage: {result['total_damage']})"
                                )
                        continue
                    enemy["board"] = [
                                c for c in enemy["board"]
                                if isinstance(c, CreatureCard) and c.health > 0
                            ]
                    turn_result["attacks"].append(
                            f"{max_damage.name} dealt {max_damage.attack} "
                            f"to {[target.name for target in targets]} "
                            f"(total damage: {result['total_damage']})\n"
                            f"{max_damage.name} killed "
                            f"\
{[kill.name for kill in result['targets_killed']]}"
                            )
                else:
                    result: dict = max_damage.resolve_effect(
                            [target for target in player["board"]
                             if isinstance(target, CreatureCard)]
                            )
                    turn_result["attacks"].append(
                            f"{max_damage.name} healt {max_damage.attack} "
                            f"to {[target.name for target in targets]} "
                            f"(total heal: {result['total_heal']})"
                            )

            elif isinstance(max_damage, ArtifactCard):
                card_index: int = next(
                        (
                            i for i, c in enumerate(player["board"])
                            if c == max_damage
                            ),
                        None)

                player["active_artifacts"].append(
                        player["board"].pop(card_index)
                        )

                turn_result["attacks"].append(
                        f"{player['name']} used the artifact {max_damage.name}"
                        f"it will do {max_damage.effect} "
                        f"for {max_damage.durability} turn"
                        )

        player["active_artifacts"] = [
                artifact for artifact in player["active_artifacts"]
                if artifact.durability > 0
                ]
        for artifact in player["active_artifacts"]:
            if ("mana" in artifact.effect or "heal" in artifact.effect):
                heal_targets: list = [target for target in player["board"]
                                      if isinstance(target, CreatureCard)]
                if not heal_targets:
                    continue
                result: dict = artifact.activate_ability(heal_targets)
                turn_result["artifacts"].append(
                        f"{artifact.name} healt {artifact.attack} "
                        f"to {[target.name for target in targets]} "
                        f"(total heal: {result['total_heal']})"
                        )
            else:
                result: dict = artifact.activate_ability(targets)
                if not result["targets_killed"]:
                    turn_result["attacks"].append(
                            f"{artifact.name} dealt {artifact.attack} "
                            f"to {[target.name for target in targets]} "
                            f"(total damage: {result['total_damage']})"
                            )
                    continue
                enemy["board"] = [
                        c for c in enemy["board"]
                        if isinstance(c, CreatureCard) and c.health > 0
                        ]
                turn_result["artifacts"].append(
                        f"{artifact.name} dealt {artifact.attack} "
                        f"to {[target.name for target in targets]} "
                        f"(total damage: {result['total_damage']})\n"
                        f"{artifact.name} killed "
                        f"\
{[kill.name for kill in result['targets_killed']]}"
                        )

        return turn_result

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return [target for target in available_targets
                if isinstance(target, CreatureCard)]

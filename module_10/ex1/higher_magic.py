from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    target: str = "dragon"
    return lambda: (spell1(target), spell2(target))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda: (base_spell() * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda: (
            spell() if condition() else "Spell fizzled"
            )


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda: ([spell() for spell in spells])


def main() -> None:

    combined: Callable = spell_combiner(
            lambda x: 'Fireball hits ' + x,
            lambda x: 'Heals' + x
            )

    power: Callable = power_amplifier(
            lambda: 10,
            3
            )

    print("Testing spell combiner...")
    print(f"Combined spell result: {combined()}")

    print()
    print("Testing power amplifier...")
    print(f"Original: 10, Amplified: {power()}")


if __name__ == "__main__":
    main()

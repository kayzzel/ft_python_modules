from typing import Callable
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    result: int
    match operation:
        case "add":
            result = reduce(lambda a, b: a + b, spells)

        case "multiply":
            result = reduce(lambda a, b: a * b, spells)

        case "max":
            result = reduce(lambda a, b: a if a >= b else b, spells)

        case "min":
            result = reduce(lambda a, b: a if a < b else b, spells)
        case _:
            raise ValueError(
                    f"Unsuported operation: {operation} not in "
                    "[add, multiply, max, min]"
                             )

    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
            "fire_enchant": partial(
                base_enchantment, power=50, element="fire"
                ),
            "ice_enchant": partial(
                base_enchantment, power=50, element="ice"
                ),
            "lightning_enchant": partial(
                base_enchantment, power=50, element="lightning"
                ),
            }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(spell):
        return f"Unknown spell type: {type(spell).__name__}"

    @cast.register
    def _(spell: int) -> str:
        return f"Casting damage spell for {spell} HP!"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchanting target with '{spell}'!"

    @cast.register
    def _(spell: list) -> list:
        return [cast(s) for s in spell]

    return cast

from typing import Callable, Any


def mage_counter() -> Callable:
    call_count: int = 0

    def call_counter() -> int:
        nonlocal call_count
        call_count += 1
        return call_count

    return call_counter


def spell_accumulator(initial_power: int) -> Callable:
    power: int = initial_power

    def add_power(power_to_add: int) -> int:
        nonlocal power
        power += power_to_add
        return power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant_item(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant_item


def memory_vault() -> dict[str, Callable]:
    vault: dict = {}

    def store(key: Any, value: Any) -> None:
        vault[key] = value

    def recall(key: Any) -> Any:
        if key not in vault.keys():
            return "Memory not found"
        return vault[key]

    return {
            "store": store,
            "recall": recall
            }


def main() -> None:
    counter: Callable = mage_counter()
    factory_fire: Callable = enchantment_factory("fire")
    factory_sharp: Callable = enchantment_factory("sharp")

    print("Testing mage counter...")
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())
    print("Call 4:", counter())

    print()
    print("Testing enchantment factory...")
    print(factory_fire("sword"))
    print(factory_sharp("sword"))
    print(factory_fire("shield"))
    print(factory_sharp("shield"))


if __name__ == "__main__":
    main()

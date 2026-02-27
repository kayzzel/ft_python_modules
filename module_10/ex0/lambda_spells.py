def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=(lambda a: a["power"]))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
            "max_power": max(mages, key=(lambda m: m["power"])),
            "min_power": min(mages, key=(lambda m: m["power"])),
            "avg_power": round(
                sum(mage["power"] for mage in mages) / len(mages),
                2
                )
            }


def main() -> None:
    mages: list[dict] = [
            {"name": "mage1", "power": 10, "element": "fire"},
            {"name": "mage2", "power": 20, "element": "earth"},
            {"name": "mage3", "power": 5, "element": "water"},
            {"name": "mage4", "power": 1, "element": "wind"},
        ]

    artifacts: list[dict] = [
            {"name": "artifact1", "power": 1, "type": "wind"},
            {"name": "artifact2", "power": 3, "type": "fire"},
            {"name": "artifact3", "power": 9, "type": "earth"},
            {"name": "artifact4", "power": 10, "type": "water"},
        ]

    spells: list[str] = [
            "fireball",
            "heal",
            "shield",
            ]

    print("test artifact sorter...")
    print("\n".join([str(a) for a in artifact_sorter(artifacts)]))

    print()
    print("test power filter...")
    print("\n".join([str(m) for m in power_filter(mages, 8)]))

    print()
    print("test spells transformer...")
    print(" ".join(spell_transformer(spells)))

    print()
    print("test mage stats...")
    print("\n".join(
        [f"{key}: {value}" for key, value in mage_stats(mages).items()]
        ))


if __name__ == "__main__":
    main()

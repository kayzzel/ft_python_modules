import alchemy.elements as elem


def healing_potion() -> str:
    return f"Healing potion brewed with {elem.create_fire()} \
and {elem.create_water()}"


def strenght_potion() -> str:
    return f"Strenght potion brewed with {elem.create_earth()} \
and {elem.create_fire()}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {elem.create_air()} \
and {elem.create_water()}"


def wisdom_potion() -> str:
    return f"Wisdom potion brewed with all elements: \
{elem.create_fire()}, \
{elem.create_water()}, \
{elem.create_earth()}, \
{elem.create_air()}, "

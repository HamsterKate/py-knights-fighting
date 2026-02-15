from app.knight import Knight
from typing import Dict


def fight(knight1: Knight, knight2: Knight) -> None:
    power1 = knight1.battle_power
    power2 = knight2.battle_power

    knight1.take_damage(power2)
    knight2.take_damage(power1)


def battle(knights_config: Dict) -> Dict[str, int]:
    # Create Knight objects
    knights = []

    for key in knights_config:
        knights.append(Knight(**knights_config[key]))

    # Prepare all knights
    for knight in knights:
        knight.prepare_for_battle()

    # Pair and fight dynamically
    for i in range(0, len(knights) - 1, 2):
        fight(knights[i], knights[i + 1])

    # Commit battle results
    for knight in knights:
        knight.commit_battle()

    # Return final HP
    return {
        knight.name: knight.hp
        for knight in knights
    }

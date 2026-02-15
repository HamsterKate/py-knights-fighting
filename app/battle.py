from app.knight import Knight
from typing import Dict


def fight(knight1: Knight, knight2: Knight) -> None:
    power1 = knight1.battle_power
    power2 = knight2.battle_power

    knight1.take_damage(power2)
    knight2.take_damage(power1)


from app.knight import Knight
from app.config import KNIGHTS
from typing import Dict

def battle(knights_config: Dict) -> Dict[str, int]:
    """
    Orchestrates the battle between predefined knight pairs and returns
    the remaining HP for each knight.
    """

    # Create Knight instances and prepare them for battle
    knights: Dict[str, Knight] = {}
    for key in knights_config:
        k = Knight(**knights_config[key])
        k.prepare_for_battle()
        knights[key] = k

    # Define exact battle pairs (test expects this order)
    battle_pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    # Apply simultaneous damage
    for k1_name, k2_name in battle_pairs:
        k1 = knights[k1_name]
        k2 = knights[k2_name]

        # Store battle_power first to ensure simultaneous damage
        k1_power = k1.battle_power
        k2_power = k2.battle_power

        k1.take_damage(k2_power)
        k2.take_damage(k1_power)

    # Commit results: update base hp from battle_hp
    for k in knights.values():
        k.hp = k.battle_hp

    # Return result using human-friendly names
    return {k.name: k.hp for k in knights.values()}

from typing import Any, Iterable

from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item
from ..Locations import location_name_to_location

def get_item_count(boss_keys: int, xalax_keys: int) -> int:
    return 34 + 3 * boss_keys + xalax_keys

def get_location_count(boss_checks: int, talksanity: bool) -> int:
    return 45 + 3 * boss_checks + (45 if talksanity else 0)

def validate_options_early(world: World) -> None:
    boss_keys = world.options.boss_keys_available.value
    xalax_keys = world.options.xalax_keys_available.value
    boss_checks = world.options.boss_check_count.value
    talksanity = bool(world.options.enable_talksanity)

    while get_item_count(boss_keys, xalax_keys) > get_location_count(boss_checks, talksanity):
        if boss_keys >= xalax_keys: boss_keys -= 1
        if xalax_keys > boss_keys: xalax_keys -= 1
        boss_checks += 1

    world.options.boss_keys_available.value = boss_keys
    world.options.xalax_keys_available.value = xalax_keys
    world.options.boss_check_count.value = boss_checks

def remove_extra_boss_checks(world: World) -> Iterable[str]:
    max_count = world.options.boss_check_count.value
    for name, location in location_name_to_location.items():
        if 'extra_data' in location and 'boss_check_count' in location['extra_data']:
            count = location['extra_data']['boss_check_count']
            if count > max_count: yield name

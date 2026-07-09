from typing import Any, Iterable

from math import floor
from .func import random_weight, debug
from worlds.AutoWorld import World # pyright: ignore[reportMissingImports]
from BaseClasses import MultiWorld, CollectionState, Item # pyright: ignore[reportMissingImports]
from ..Locations import location_name_to_location
from ..Items import item_name_to_item

def get_item_count(boss_keys: int, xalax_keys: int) -> int:
    return 34 + 3 * boss_keys + xalax_keys

def get_location_count(boss_checks: int, npc_checks: bool) -> int:
    return 45 + 3 * boss_checks + (45 if npc_checks else 0)

def validate_options_early(world: World) -> None:
    boss_keys = world.options.boss_keys_available.value
    xalax_keys = world.options.xalax_keys_available.value
    boss_checks = world.options.boss_check_count.value
    npc_checks = bool(world.options.enable_npc_checks.value)

    debug(lambda: f'boss_keys: {boss_keys}')
    debug(lambda: f'xalax_keys: {xalax_keys}')
    debug(lambda: f'boss_checks: {boss_checks}')
    debug(lambda: f'npc_checks: {npc_checks}')

    debug(lambda: f'get_item_count(): {get_item_count(boss_keys, xalax_keys)}')
    debug(lambda: f'get_location_count(): {get_location_count(boss_checks, npc_checks)}')

    while get_item_count(boss_keys, xalax_keys) > get_location_count(boss_checks, npc_checks) - 5:
        debug(lambda: f'Discrepancy detected! Correcting...')

        if boss_keys >= xalax_keys: boss_keys = max(1, boss_keys - 1)
        if xalax_keys > boss_keys: xalax_keys = max(1, xalax_keys - 1)
        boss_checks = min(10, boss_checks + 1)

        debug(lambda: f'boss_keys: {boss_keys}')
        debug(lambda: f'boss_keys: {xalax_keys}')
        debug(lambda: f'boss_keys: {boss_checks}')
        debug(lambda: f'boss_keys: {npc_checks}')

        debug(lambda: f'get_item_count(): {get_item_count(boss_keys, xalax_keys)}')
        debug(lambda: f'get_location_count(): {get_location_count(boss_checks, npc_checks)}')

    world.options.boss_keys_available.value = boss_keys
    world.options.xalax_keys_available.value = xalax_keys
    world.options.boss_check_count.value = boss_checks

def remove_extra_boss_checks(world: World) -> Iterable[str]:
    max_count = world.options.boss_check_count.value
    for name, location in location_name_to_location.items():
        if 'extra_data' in location and 'boss_check_count' in location['extra_data']:
            count = location['extra_data']['boss_check_count']
            if count > max_count: yield name

def correct_bonus_counts(item_config: dict[str, int|dict], world: World) -> None:
    grips = world.options.weight_grip.value
    shields = world.options.weight_shield.value
    powers = world.options.weight_power.value

    while grips + shields + powers < 10:
        match world.random.randint(1, 3):
            case 1: grips += 1
            case 2: shields += 1
            case 3: powers += 1

    if grips + shields + powers > 10:
        list = ['grip'] * grips + ['shield'] * shields + ['power'] * powers
        world.random.shuffle(list)
        list = list[0:10]
        grips = len([item for item in list if item == 'grip'])
        shields = len([item for item in list if item == 'shield'])
        powers = len([item for item in list if item == 'power'])

    item_config['Shield Upgrade'] = shields
    item_config['Grip Upgrade'] = grips
    item_config['Power Upgrade'] = powers

def correct_key_counts(world: World) -> tuple[int, int, int, int]:
    boss_keys_available = world.options.boss_keys_available.value
    boss_keys_need_pct = world.options.boss_keys_needed.value
    boss_keys_need_count = max(floor((boss_keys_need_pct + 0.99) / 100 * boss_keys_available), 1)
    boss_keys_useful_count = boss_keys_available - boss_keys_need_count
    xalax_keys_available = world.options.xalax_keys_available.value
    xalax_keys_need_pct = world.options.xalax_keys_needed.value
    xalax_keys_need_count = max(floor((xalax_keys_need_pct + 0.99) / 100 * xalax_keys_available), 1)
    xalax_keys_useful_count = xalax_keys_available - xalax_keys_need_count

    return boss_keys_need_count, boss_keys_useful_count, xalax_keys_need_count, xalax_keys_useful_count

def update_item_config(item_config: dict[str, int|dict], world: World) -> dict[str, int|dict]:
    correct_bonus_counts(item_config, world)

    boss_prog, boss_use, xalax_prog, xalax_use = correct_key_counts(world)

    boss_checks = world.options.boss_check_count.value
    npc_checks = bool(world.options.enable_npc_checks)

    debug(lambda: f'boss_prog: {boss_prog}')
    debug(lambda: f'boss_use: {boss_use}')
    debug(lambda: f'xalax_prog: {xalax_prog}')
    debug(lambda: f'xalax_use: {xalax_use}')

    item_count = get_item_count(boss_prog + boss_use, xalax_prog + xalax_use)
    location_count = get_location_count(boss_checks, npc_checks)

    debug(lambda: f'item_count: {item_count}')
    debug(lambda: f'location_count: {location_count}')

    filler_count = location_count - item_count

    debug(lambda: f'filler_count: {filler_count}')

    filler_weight: dict[str, int] = {}
    filler_weight_sum = 0

    for name, item in item_name_to_item.items():
        if 'extra_data' in item:
            data = item['extra_data']
            if 'boss_key_type' in data:
                match data['boss_key_type']:
                    case 'boss':
                        item_config[name] = {
                            'progression': boss_prog,
                            'useful': boss_use
                        }
                    case 'xalax':
                        item_config[name] = {
                            'progression': xalax_prog,
                            'useful': xalax_use
                        }
            elif 'item_weighting' in data:
                filler_weight[name] = getattr(world.options, data['item_weighting']).value
                filler_weight_sum += filler_weight[name]

    if filler_weight_sum == 0:
        filler_weight['Cheese Wedge Brick'] = 1

    for _ in range(filler_count):
        debug(lambda: 'Generating a filler/trap:')
        selected_trap = random_weight(filler_weight, world.random)
        debug(lambda: f'Selected: {selected_trap}')
        selected_config = item_config[selected_trap]
        debug(lambda: f'Its config: {selected_config}')
        if isinstance(selected_config, int):
            item_config[selected_trap] = selected_config + 1
        else:
            item_config[selected_trap] = 1
        debug(lambda: f'New config: {item_config[selected_trap]}')

    return item_config

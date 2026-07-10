from inspect import stack
from numbers import Number
import random
from typing import Callable, TypeVar

T = TypeVar('T')

DEBUG_ENABLED = True
DEBUG_FUNCTIONS = [
    # 'adjust_filler_items',
    # 'after_create_regions',
    # 'validate_options_early',
    # 'update_item_config',
    'grant_settings_items'
]

def debug(msg: Callable[[], str]) -> None:
    """
    Prints a given message with function info if it's an allowlisted function.
    """
    if not DEBUG_ENABLED: return
    stk = stack()
    if len(stk) < 2: return
    if stk[1].function in DEBUG_FUNCTIONS:
        print(f'[Manual_LEGORacers2_Nixill / {stk[1].function} @ {stk[1].lineno}] {msg()}')

def random_weight(weights: dict[T, int], randomizer: random.Random | None) -> T:
    total_weight = sum(weights.values())

    if total_weight <= 0:
        raise ValueError('dict object is empty or has total weight <= 0')

    selection = (randomizer or random).randint(0, total_weight - 1)

    for item, weight in weights.items():
        if weight > selection:
            return item
        else:
            selection -= weight

    raise IndexError('I don\'t know how you got here.')

from typing import Iterable

from mod.classes import Category, Item, ItemClassification
from data.worlds import LegoWorld
import data.worlds as worlds
import data.strings as txt
from . import categories
from mod.json_types import JsonObject

def get_sort_key(category: Category, world: LegoWorld | None = None, index: int | None = None) -> str:
  world_index = 0
  if world: world_index = world.world_index

  key_string = ''

  match category:
    case categories.race_keys:
      key_string = txt.Items.SortKeys.RACE_KEYS
    case categories.boss_keys:
      key_string = txt.Items.SortKeys.BOSS_KEYS
    case categories.bonus_game_keys:
      key_string = txt.Items.SortKeys.BONUS_GAME_KEYS
    case categories.traps:
      key_string = txt.Items.SortKeys.TRAPS
    case categories.car_bonuses:
      key_string = txt.Items.SortKeys.CAR_BONUSES
    case categories.exploration_keys:
      key_string = txt.Items.SortKeys.EXPLORATION_KEYS

  return key_string.format(world_index=world_index, index=index)

race_keys_dict = {
  race_name: Item(
    name=txt.Items.RACE_KEY.format(race=race_name),
    item_class=ItemClassification.PROGRESSION,
    count = 1,
    category=[categories.race_keys, categories.for_world(world)],
    sort_key=get_sort_key(categories.race_keys, world, index)
  )
  for world in worlds.all_worlds
  for index, race_name in enumerate(world.race_names, 1)
}
'''Mapping of race name to race key item.'''

boss_keys_dict = {
  world.name: Item(
    name=txt.Items.BOSS_KEY.format(world=world.name),
    classification_count={
      ItemClassification.PROGRESSION: 1,
      ItemClassification.USEFUL: 1
    },
    category=[categories.boss_keys, categories.for_world(world)],
    sort_key=get_sort_key(categories.boss_keys, world)
  )
  for world in worlds.boss_worlds
}
'''Mapping of world name to boss key item.'''

exploration_keys_dict = {
  world.name: Item(
    name=txt.Items.EXPLORATION_KEY.format(world=world.name),
    item_class=ItemClassification.PROGRESSION,
    count=1,
    category=[categories.exploration_keys, categories.for_world(world)],
    sort_key=get_sort_key(categories.exploration_keys, world)
  )
  for world in worlds.all_worlds
}

car_bonuses = [
  Item(
    name=name,
    item_class=ItemClassification.PROGRESSION,
    count=10,
    category=[categories.car_bonuses],
    sort_key=get_sort_key(categories.car_bonuses, index=index)
  )
  for index, name in enumerate(
    [txt.Items.Bonus.GRIP, txt.Items.Bonus.SHIELD, txt.Items.Bonus.POWER],
    start=1
  )
]

grip_upgrade = car_bonuses[0]
shield_upgrade = car_bonuses[1]
power_upgrade = car_bonuses[2]

all_items: list[Item] = [
  *race_keys_dict.values(),
  *boss_keys_dict.values(),
  *exploration_keys_dict.values(),
  *car_bonuses,
]

item_table: JsonObject = Item.to_json_output(all_items)

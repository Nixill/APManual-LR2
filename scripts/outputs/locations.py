from typing import Iterable

from mod.classes import Category, Item, ItemClassification, Location
from mod import requires as req
from data.worlds import LegoWorld
import data.worlds as worlds
import data.strings as txt
from mod.json_types import JsonObject
from . import categories, items, options, regions

def get_sort_key(category: Category, world: LegoWorld | None = None, index: int | None = None) -> str:
  world_index = world.world_index if world else 0

  key_string = ''

  match category:
    case categories.standard_races:
      key_string = txt.Locations.SortKeys.STANDARD_RACES
    case categories.boss_races:
      key_string = txt.Locations.SortKeys.BOSS_RACES
    case categories.golden_bricks:
      key_string = txt.Locations.SortKeys.GOLDEN_BRICKS
    case categories.bonus_games:
      key_string = txt.Locations.SortKeys.BONUS_GAMES
    case categories.npcs:
      key_string = txt.Locations.SortKeys.NPCS
    case categories.bonus_game_unlocks:
      key_string = txt.Locations.SortKeys.BONUS_GAME_UNLOCKS

  return key_string.format(world_index=world_index, index=index)

race_check_dict = {
  race_name: Location(
    name=txt.Locations.STANDARD_RACE.format(index=index, race_name=race_name),
    requires=req.item(items.race_keys_dict[race_name]),
    region=regions.for_world(world),
    category=[categories.standard_races, categories.for_world(world)],
    sort_key=get_sort_key(categories.standard_races, world, index)
  )
  for world in worlds.all_worlds
  for index, race_name in enumerate(world.race_names, 1)
}
'''Maps Race Name → Location'''

# Does not count Xalax (and Sandy Bay has no bosses)
boss_check_dict = {
  world.name: {
    index: Location(
      name=txt.Locations.BOSS_RACE.format(name=world.boss_race_name, i=index),
      requires=req.option_count_percent(item=items.boss_keys_dict[world.name], option=options.boss_keys_needed),
      region=regions.for_world(world),
      category=[categories.boss_races, categories.for_world(world)]
    )
    for index in range(1, 6)
  }
  for world in worlds.mid_worlds
}

boss_check_dict[worlds.xalax.name] = {
  index: Location(
    name=txt.Locations.BOSS_RACE.format(name=worlds.xalax.boss_race_name, i=index),
    requires=req.option_count_percent(item=items.boss_keys_dict[worlds.xalax.name], option=options.xalax_keys_needed)
  )
  for index in range(1, 6)
}

golden_brick_dict = {
  world.name: {
    brick: Location(
      name=txt.Locations.GOLDEN_BRICK.format(world=world.name, name=brick),
      requires=req.item(item=items.exploration_keys_dict[world.name]),
      region=regions.for_world(world),
      category=[categories.exploration_keys, categories.for_world(world)],
      sort_key=get_sort_key(categories.exploration_keys, world, index)
    )
    for index, brick in enumerate(world.golden_brick_names, 1)
  }
  for world in worlds.all_worlds
}

all_locations: list[Location] = [
  *race_check_dict.values(),
  *[boss_race
    for world in boss_check_dict.values()
    for boss_race in world.values()],
  *[golden_brick
    for world in golden_brick_dict.values()
    for golden_brick in world.values()],
]

location_table: JsonObject = Location.to_json_output(all_locations)

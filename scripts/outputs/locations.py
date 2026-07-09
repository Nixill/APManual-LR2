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
  for world in worlds.boss_worlds
  for index, race_name in enumerate(world.race_names, 1)
}
'''Maps Race Name → Location'''

_sandy_bay_keys: list[Item] = []
for index, race_name in enumerate(worlds.sandy_bay.race_names, 1):
  requirement = ''
  this_race_key = items.race_keys_dict[race_name]
  if _sandy_bay_keys:
    requirement = req.all(
      req.any(
        req.yaml_compare(options.save_mode, '>=', 2),
        req.all(*(req.item(key) for key in _sandy_bay_keys))),
      req.item(this_race_key))
  else:
    requirement = req.item(this_race_key)
  race_check_dict[race_name] = Location(
    name=txt.Locations.STANDARD_RACE.format(index=index, race_name=race_name),
    requires=requirement,
    region=regions.for_world(worlds.sandy_bay),
    category=[categories.standard_races, categories.for_world(worlds.sandy_bay)],
    sort_key=get_sort_key(categories.standard_races, worlds.sandy_bay, index)
  )
  _sandy_bay_keys.append(this_race_key)

# Does not count Xalax (and Sandy Bay has no bosses)
boss_check_dict = {
  world.name: {
    index: Location(
      name=txt.Locations.BOSS_RACE.format(name=world.boss_race_name, i=index),
      requires=req.all(
        req.item(item=items.boss_keys_dict[world.name], all=True),
        req.any(
          req.all(*(
            req.item(item=items.race_keys_dict[race_name])
            for race_name in world.race_names
          )),
          req.yaml_compare(options.save_mode, '=', 3)
        )
      ),
      region=regions.for_world(world),
      extra_data={
        'boss_check_count': index
      },
      category=[categories.boss_races, categories.for_world(world)]
    )
    for index in range(1, 11)
  }
  for world in worlds.mid_worlds
}

# # To be messed with when I actually have other goals.
# boss_check_dict[worlds.xalax.name] = {
#   index: Location(
#     name=txt.Locations.BOSS_RACE.format(name=worlds.xalax.boss_race_name, i=index),
#     requires=req.item(item=items.boss_keys_dict[worlds.xalax.name], all=True),
#     region=regions.for_world(worlds.xalax),
#     extra_data={
#       'boss_check_count': index
#     },
#     category=[categories.boss_races, categories.for_world(worlds.xalax), categories.final_boss_races]
#   )
#   for index in range(1, 11)
# }

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

bonus_game_unlocks: list[Location] = [
  Location(
    name=txt.Locations.BONUS_GAME_UNLOCK.format(i=index),
    requires=req.category(categories.car_bonuses, index),
    place_item_category=[categories.bonus_game_keys],
    sort_key=get_sort_key(categories.bonus_game_unlocks, index=index)
  )
  for index in range(1, 11)
]

bonus_game_completions: dict[str, dict[bool, Location]] = {
  world.name: {
    diff_is_hard: Location(
      name=txt.Locations.BONUS_GAME_COMPLETE.format(world=world.name, diff='Hard' if diff_is_hard else 'Easy'),
      requires=req.all(
        req.item(items.bonus_game_keys_dict[world.name], count=2 if diff_is_hard else 1),
        req.item(items.exploration_keys_dict[world.name])
      ),
      category=[categories.bonus_games, categories.for_world(world)],
      sort_key=get_sort_key(categories.bonus_games, world=world, index=2 if diff_is_hard else 1)
    )
    for diff_is_hard in [False, True]
  }
  for world in worlds.all_worlds
}

npc_list: list[Location] = [
  Location(
    name=txt.Locations.NPC.format(name=npc),
    requires=req.item(items.exploration_keys_dict[world.name]),
    category=[categories.npcs, categories.for_world(world)]
  )
  for world in worlds.all_worlds
  for npc in world.npc_names
]

victory = Location(
  name=txt.Locations.BOSS_RACE.format(name=worlds.xalax.boss_race_name, i=1),
  requires=req.all(
    req.item(item=items.boss_keys_dict[worlds.xalax.name], all=True),
    req.any(
      req.all(*(
        req.item(item=items.race_keys_dict[race_name])
        for race_name in worlds.xalax.race_names
      )),
      req.yaml_compare(options.save_mode, '=', 3)
    )
  ),
  region=regions.for_world(worlds.xalax),
  extra_data={
    'boss_check_count': 1
  },
  category=[categories.boss_races, categories.for_world(worlds.xalax)],
  victory=True
)

all_locations: list[Location] = [
  *race_check_dict.values(),
  *[boss_race
    for world in boss_check_dict.values()
    for boss_race in world.values()],
  *[golden_brick
    for world in golden_brick_dict.values()
    for golden_brick in world.values()],
  *bonus_game_unlocks,
  *[comp
    for world in bonus_game_completions.values()
    for comp in world.values()],
  *npc_list,
  victory,
]

location_table: JsonObject = Location.to_json_output(all_locations)

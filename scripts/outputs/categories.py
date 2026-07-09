from data.worlds import LegoWorld, all_worlds
from mod.classes import Category
import data.strings as txt
from mod.json_types import JsonObject
from . import options

world_categories: dict[str, Category] = {
  world.name: Category(txt.Categories.WORLDS.format(index=world.world_index, world_name=world.name))
  for world in all_worlds
}

def for_world(world: LegoWorld) -> Category:
  return world_categories[world.name]

bonus_game_keys = Category(txt.Categories.Items.BONUS_GAME_KEYS)
boss_keys = Category(txt.Categories.Items.BOSS_KEYS)
car_bonuses = Category(txt.Categories.Items.CAR_BONUSES)
exploration_keys = Category(txt.Categories.Items.EXPLORATION_KEYS)
race_keys = Category(txt.Categories.Items.RACE_KEYS)
traps = Category(txt.Categories.Items.TRAPS)

item_categories: list[Category] = [
  bonus_game_keys,
  boss_keys,
  car_bonuses,
  exploration_keys,
  race_keys,
  traps,
]

standard_races = Category(txt.Categories.Locations.STANDARD_RACES)
boss_races = Category(txt.Categories.Locations.BOSS_RACES)
golden_bricks = Category(txt.Categories.Locations.GOLDEN_BRICKS)
bonus_games = Category(txt.Categories.Locations.BONUS_GAMES)
npcs = Category(
  name=txt.Categories.Locations.NPCS,
  options=[options.enable_npc_checks]
)
bonus_game_unlocks = Category(txt.Categories.Locations.BONUS_GAME_UNLOCKS)
final_boss_races = Category(
  txt.Categories.Locations.FINAL_BOSS,
  hidden=True
)

location_categories = [
  standard_races,
  boss_races,
  golden_bricks,
  bonus_games,
  npcs,
  bonus_game_unlocks,
  final_boss_races,
]

boss_race_events = Category(txt.Categories.Events.BOSS_RACES, hidden=True)

event_categories = [
  boss_race_events
]

all_categories: list[Category] = [
  *world_categories.values(),
  *item_categories,
  *location_categories,
  *event_categories,
]

category_table: JsonObject = Category.to_json_output(all_categories)

class Categories:
  # Category names are plural.
  WORLDS = '[{index}] {world_name}'
  class Events:
    BOSS_RACES = 'Boss Race Events'
  class Items:
    BONUS_GAME_KEYS = '[0.3] Bonus Game Keys'
    BOSS_KEYS = '[7] Boss Keys'
    CAR_BONUSES = '[0.2] Car Bonuses'
    EXPLORATION_KEYS = '[8] Exploration Keys'
    RACE_KEYS = '[6] Race Keys'
    TRAPS = '[0.1] Traps'
  class Locations:
    BONUS_GAME_UNLOCKS = '[0] Bonus Game Unlocks'
    BONUS_GAMES = '[9] Bonus Games'
    BOSS_RACES = '[7] Boss Races'
    FINAL_BOSS = 'Final Boss'
    GOLDEN_BRICKS = '[8] Golden Bricks'
    NPCS = '[A] NPCs'
    STANDARD_RACES = '[6] Standard Races'

class ExtraData:
  class Keys:
    RACE_NAME = 'race_name'

class Items:
  # Item names are singular.
  class Bonus:
    GRIP = 'Grip Upgrade'
    POWER = 'Power Upgrade'
    SHIELD = 'Shield Upgrade'
  BONUS_GAME_KEY = '{world} Bonus Game Key'
  BOSS_KEY = '{world} Boss Key'
  CHEESE_WEDGE = 'Cheese Wedge Brick'
  EXPLORATION_KEY = '{world} Exploration Key'
  RACE_KEY = '{race} Race Key'
  class SortKeys:
    RACE_KEYS = '{world_index}-1-{index}'
    BOSS_KEYS = '{world_index}-2'
    EXPLORATION_KEYS = '{world_index}-3'
    BONUS_GAME_KEYS = '{world_index}-4'
    TRAPS = '0-1-{index}'
    CAR_BONUSES = '0-2-{index}'
  TRAP_LIST = [
    'Item embargo',
    'Freeze',
    'Destroy your car',
    'No pitstops',
    'No shortcuts',
    'Drive in reverse',
    'Top-down camera',
    'Quit adventure'
  ]
  TRAP_TEMPLATE = 'TRAP - {name}'
  class Values:
    GB_FOR_MARS = 'gold_bricks_for_mars'
    GB_FOR_ARCTIC = 'gold_bricks_for_arctic'
    SANDY_BAY = 'sandy_bay_races'

class Locations:
  BONUS_GAME_COMPLETE = 'Bonus Game: {world} {diff}'
  BONUS_GAME_UNLOCK = 'Bonus Game Unlock #{i}'
  BOSS_RACE = 'Boss Race: {name} (Check {i})'
  GOLDEN_BRICK = '{world} {name} Golden Brick'
  NPC = 'NPC: {name}'
  STANDARD_RACE = 'Race #{index}: {race_name}'
  class SortKeys:
    STANDARD_RACES = '{world_index}-1-{index}'
    BOSS_RACES = '{world_index}-2'
    GOLDEN_BRICKS = '{world_index}-3-{index}'
    BONUS_GAMES = '{world_index}-4-{index}'
    NPCS = '{world_index}-5-{index}'
    BONUS_GAME_UNLOCKS = '0-{index}'

class Options:
  class Groups:
    ITEM_WEIGHTING = 'Item Weighting'
    KEY_GENERATION = 'Key Generation'
    OTHERS = 'Others'
    SETUP_OPTIONS = 'Setup Options'

class Regions:
  EPHEMERAL = 'Ephemeral'

class Requirements:
  HAS_GOLDEN_BRICKS = 'HasGoldenBricks'
  HAS_XALAX_ACCESS = 'HasXalaxAccess'

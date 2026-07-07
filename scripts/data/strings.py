class Categories:
  # Category names are plural.
  WORLDS = '[{index}] {world_name}'
  class Items:
    BONUS_GAME_KEYS = '[03] Bonus Game Keys'
    BOSS_KEYS = '[7] Boss Keys'
    CAR_BONUSES = '[02] Car Bonuses'
    EXPLORATION_KEYS = '[8] Exploration Keys'
    RACE_KEYS = '[6] Race Keys'
    TRAPS = '[01] Traps'
  class Locations:
    BONUS_GAME_UNLOCKS = '[0] Bonus Game Unlocks'
    BONUS_GAMES = '[5] Bonus Games'
    BOSS_RACES = '[3] Boss Races'
    GOLDEN_BRICKS = '[4] Golden Bricks'
    NPCS = '[6] NPCs'
    STANDARD_RACES = '[2] Standard Races'

class ExtraData:
  class Keys:
    RACE_NAME = 'race_name'

class Items:
  # Item names are singular.
  class Bonus:
    GRIP = 'Grip Upgrade'
    POWER = 'Power Upgrade'
    SHIELD = 'Shield Upgrade'
  BOSS_KEY = '{world} Boss Key'
  EXPLORATION_KEY = '{world} Exploration Key'
  RACE_KEY = '{race} Race Key'
  class SortKeys:
    RACE_KEYS = '{world_index}-1-{index}'
    BOSS_KEYS = '{world_index}-2  '
    EXPLORATION_KEYS = '{world_index}-3'
    BONUS_GAME_KEYS = '{world_index}-4'
    TRAPS = '0-1-{index}'
    CAR_BONUSES = '0-2-{index}'

class Locations:
  BOSS_RACE = 'Boss Race: {name} (Check {i})'
  GOLDEN_BRICK = '{world} {name} Golden Brick'
  STANDARD_RACE = 'Race #{index}: {race_name}'
  class SortKeys:
    STANDARD_RACES = '{world_index}-1-{index}'
    BOSS_RACES = '{world_index}-2'
    GOLDEN_BRICKS = '{world_index}-3-{index}'
    BONUS_GAMES = '{world_index}-4-{index}'
    NPCS = '{world_index}-5-{index}'
    BONUS_GAME_UNLOCKS = '0-{index}'

class Requirements:
  HAS_GOLDEN_BRICKS = 'HasGoldenBricks'
  HAS_XALAX_ACCESS = 'HasXalaxAccess'

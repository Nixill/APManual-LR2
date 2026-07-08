from textwrap import wrap

import data.strings as txt

from mod.classes import DeathLinkOption, FillerTrapsOption, Option, RangeOption, ToggleOption, ChoiceOption
from mod.json_types import JsonObject
from mod.func import snake_case

death_link = DeathLinkOption(
  default=False,
  display_name='Death Link',
  description=[
    *wrap('Enable death link?'),
    '',
    *wrap('Send a death whenever you lose, reset, or leave any race or minigame, or if your game crashes.'),
    '',
    *wrap('If you receive a death during a race or minigame, restart that race or minigame immediately.')
  ]
)

filler_traps = FillerTrapsOption(
  hidden=True
)

save_mode = ChoiceOption(
  name='save_mode',
  values={
    'new_game': 1,
    'new_game_with_cheats': 2,
    'finished_save': 3
  },
  default=1,
  display_name='Game Save Mode',
  description=[
    *wrap('Defines the game completion prior to the start of the Archipelago run.'),
    *wrap('- NEW GAME: Start a new game and play through normally.', subsequent_indent='  '),
    *wrap('- NEW GAME WITH CHEATS: Start a new game. Allows using cheats to skip around.', subsequent_indent='  '),
    *wrap('- FINISHED SAVE: Start with a save file that has all races unlocked.', subsequent_indent='  '),
  ],
  group=txt.Options.Groups.SETUP_OPTIONS
)

boss_keys_available = RangeOption(
  name='boss_keys_available',
  range_start=1,
  range_end=10,
  default=4,
  display_name='Boss Keys Generated',
  description=wrap('Number of keys per boss race, except on Xalax, generated in the multiworld.'),
  group=txt.Options.Groups.KEY_GENERATION,
)

boss_keys_needed = RangeOption(
  name='boss_keys_needed',
  range_start=10,
  range_end=100,
  default=80,
  display_name='Boss Keys Needed (%)',
  description=[
    *wrap('Percentage of generated keys that are needed to partake in a boss race.'),
    '',
    *wrap('Rounds down, with a minimum of 1, except that truncated decimals round up (for example, 33% of 6 keys is 2).')
  ],
  group=txt.Options.Groups.KEY_GENERATION,
)

xalax_keys_available = RangeOption(
  name='xalax_keys_available',
  range_start=1,
  range_end=10,
  default=5,
  display_name='Xalax Keys Generated',
  description=wrap('Number of keys to The Grand Finale generated in the multiworld.'),
  group=txt.Options.Groups.KEY_GENERATION,
)

xalax_keys_needed = RangeOption(
  name='xalax_keys_needed',
  range_start=10,
  range_end=100,
  default=80,
  display_name='Xalax Keys Needed (%)',
  description=[
    *wrap('Percentage of generated keys that are needed to partake in The Grand Finale.'),
    '',
    *wrap('Rounds down, with a minimum of 1, except that truncated decimals round up (for example, 33% of 6 keys is 2).')
  ],
  group=txt.Options.Groups.KEY_GENERATION,
)

boss_check_count = RangeOption(
  name='boss_check_count',
  range_start=1,
  range_end=10,
  default=5,
  display_name='Boss Check Count',
  description=[
    *wrap('How many checks is each boss race worth?'),
    '',
    *wrap('The Grand Finale is not worth any checks, as finishing that race is simply The Goal. ' \
      'In a future version of this AP with customizable goal support, The Grand Finale will be adjustable here.')
  ],
  group=txt.Options.Groups.OTHERS,
)

item_weightings = [
  RangeOption(
    name=f'weight_{snake_case(trap)}',
    range_start=0,
    range_end=100,
    default=50,
    display_name=f'Weight of {trap}',
    description=[
      *wrap(f'Relative weight for generating {trap} as filler.')
    ],
    group=txt.Options.Groups.ITEM_WEIGHTING
  )
  for trap in [*txt.Items.TRAP_LIST, 'Cheese Wedge Brick']
]

enable_talksanity = ToggleOption(
  name='enable_talksanity',
  display_name='Enable Talksanity',
  description=[
    *wrap('Enable talksanity?'),
    '',
    *wrap('Adds a check for every NPC in the game. This check is performed when you see the named character speak in any situation.')
  ],
  default=False,
  group=txt.Options.Groups.OTHERS
)

all_options = [
  death_link,
  filler_traps,
  save_mode,
  boss_keys_available,
  boss_keys_needed,
  xalax_keys_available,
  xalax_keys_needed,
  boss_check_count,
  *item_weightings,
]

option_table: JsonObject = Option.to_json_output(all_options)

from textwrap import wrap

from mod.classes import Option, RangeOption, ToggleOption, ChoiceOption
from mod.json_types import JsonObject

boss_keys_available = RangeOption(
  name='boss_keys_available',
  range_start=1,
  range_end=10,
  default=4,
  display_name='Boss Keys Generated',
  description=wrap('Number of keys per boss race, except on Xalax, generated in the multiworld.')
)

boss_keys_needed = RangeOption(
  name='boss_keys_needed',
  range_start=10,
  range_end=100,
  default=80,
  display_name='Boss Keys Needed (%)',
  description=wrap(
'''
Percentage of generated keys that are needed to partake in a boss race.

Rounds down, with a minimum of 1, except that truncated decimals round up (for example, 33% of 6 keys is 2).
''')
)

xalax_keys_available = RangeOption(
  name='xalax_keys_available',
  range_start=1,
  range_end=10,
  default=5,
  display_name='Xalax Keys Generated',
  description=wrap('Number of keys to The Grand Finale generated in the multiworld.')
)

xalax_keys_needed = RangeOption(
  name='xalax_keys_needed',
  range_start=10,
  range_end=100,
  default=80,
  display_name='Xalax Keys Needed (%)',
  description=wrap(
'''
Percentage of generated keys that are needed to partake in The Grand Finale.

Rounds down, with a minimum of 1, except that truncated decimals round up (for example, 33% of 6 keys is 2).
'''
  )
)

all_options = [
  boss_keys_available,
  boss_keys_needed,
  xalax_keys_available,
  xalax_keys_needed
]

option_table: JsonObject = Option.to_json_output(all_options)

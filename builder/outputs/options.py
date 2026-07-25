from textwrap import wrap

import data.strings as txt

from mod.classes import DeathLinkOption, FillerTrapsOption, Option, RangeOption, ToggleOption, ChoiceOption
from mod.json_types import JsonObject
from mod.func import snake_case

# death_link = DeathLinkOption(
#   default=False,
#   display_name='Death Link',
#   description=[
#     *wrap('Enable death link?'),
#     '',
#     *wrap('Insert death link description here.'),
#   ]
# )

# filler_traps = FillerTrapsOption(
#   hidden=True
# )

all_options = [
  # death_link,
  # filler_traps,
]

option_table: JsonObject = Option.to_json_output(all_options)

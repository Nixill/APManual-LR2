import data.strings as txt
from mod.classes import Category, Item, ItemClassification, Location
from mod.json_types import JsonObject
from . import categories, items, options, regions

victory = Location(
  name='Victory',
  requires='',
)

all_locations: list[Location] = [
  victory,
]

location_table: JsonObject = Location.to_json_output(all_locations)

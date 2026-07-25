import data.strings as txt
from mod.classes import Category, Item, ItemClassification, Location, Region
from mod.json_types import JsonObject
from . import categories, items, options

all_regions_dict: dict[str, Region] = {}

region_table: JsonObject = Region.to_json_output(all_regions_dict.values())

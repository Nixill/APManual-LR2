from typing import Iterable

import data.strings as txt
from mod.classes import Category, Item, ItemClassification, Value
from mod.json_types import JsonObject
from . import categories

all_items: list[Item] = [
]

item_table: JsonObject = Item.to_json_output(all_items)

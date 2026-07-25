import data.strings as txt
from mod.classes import Category
from mod.json_types import JsonObject
from . import options

all_categories: list[Category] = []

category_table: JsonObject = Category.to_json_output(all_categories)

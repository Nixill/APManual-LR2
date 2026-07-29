from mod.classes import Category, Item, ItemClassification, Location, Region
from mod import requires as req
from data.worlds import LegoWorld
import data.worlds as worlds
import data.strings as txt
from mod.json_types import JsonObject
from . import categories, items, options

all_regions_dict: dict[str, Region] = {}

dino_island = all_regions_dict[worlds.dino_island.name] = Region(
  name=worlds.dino_island.name,
  requires=req.any(
    req.item_value(items.sandy_bay_race_value, 4),
    req.yaml_compare(options.save_mode, '>=', 2)
  )
)

mars = all_regions_dict[worlds.mars.name] = Region(
  name=worlds.mars.name,
  requires=req.any(
    req.all(
      req.item_value(items.gb_mars_value, 8),
      req.item_value(items.sandy_bay_race_value, 4)
    ),
    req.yaml_compare(options.save_mode, '>=', 2)
  )
)

arctic = all_regions_dict[worlds.arctic.name] = Region(
  name=worlds.arctic.name,
  requires=req.any(
    req.all(
      req.item_value(items.gb_arctic_value, 9),
      req.item_value(items.sandy_bay_race_value, 4)
    ),
    req.yaml_compare(options.save_mode, '>=', 2)
  )
)

xalax = all_regions_dict[worlds.xalax.name] = Region(
  name=worlds.xalax.name,
  requires=req.any(
    req.category(categories.boss_race_events, count=3),
    req.yaml_compare(options.save_mode, '=', 3)
  )
)

ephemeral = all_regions_dict[''] = Region(
  name=txt.Regions.EPHEMERAL
)

sandy_bay = all_regions_dict[worlds.sandy_bay.name] = Region(
  name=worlds.sandy_bay.name,
  starting=True,
  connects_to=[*all_regions_dict.values()]
)

def for_world(world: LegoWorld) -> Region:
  return all_regions_dict[world.name]

region_table: JsonObject = Region.to_json_output(all_regions_dict.values())

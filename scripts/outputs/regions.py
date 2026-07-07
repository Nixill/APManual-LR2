from mod.classes import Category, Item, ItemClassification, Location, Region
from mod import requires as req
from data.worlds import LegoWorld
import data.worlds as worlds
import data.strings as txt
from mod.json_types import JsonObject
from . import categories

all_regions_dict: dict[str, Region] = {}

dino_island = all_regions_dict[worlds.dino_island.name] = Region(
  name=worlds.dino_island.name,
  requires=req.custom_yaml_function(txt.Requirements.HAS_GOLDEN_BRICKS, '4')
)

mars = all_regions_dict[worlds.mars.name] = Region(
  name=worlds.mars.name,
  requires=req.custom_yaml_function(txt.Requirements.HAS_GOLDEN_BRICKS, '8')
)

arctic = all_regions_dict[worlds.arctic.name] = Region(
  name=worlds.arctic.name,
  requires=req.custom_yaml_function(txt.Requirements.HAS_GOLDEN_BRICKS, '9')
)

xalax = all_regions_dict[worlds.xalax.name] = Region(
  name=worlds.xalax.name,
  requires=req.custom_yaml_function(txt.Requirements.HAS_XALAX_ACCESS)
)

sandy_bay = all_regions_dict[worlds.sandy_bay.name] = Region(
  name=worlds.sandy_bay.name,
  starting=True,
  connects_to=[*all_regions_dict.values()]
)

def for_world(world: LegoWorld) -> Region:
  return all_regions_dict[world.name]

region_table: JsonObject = Region.to_json_output(all_regions_dict.values())

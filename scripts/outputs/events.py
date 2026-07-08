from data.worlds import LegoWorld, mid_worlds
from mod.classes import Event
import data.strings as txt
from . import categories

boss_race_events: dict[str, Event] = {
  world.name: Event(
    name=f'{world.name} boss accessible',
    copy_location=txt.Locations.BOSS_RACE.format(name=world.boss_race_name, i=1),
    category=[categories.boss_race_events]
  )
  for world in mid_worlds
}

all_events: list[Event] = [
  *boss_race_events.values()
]

event_table = Event.to_json_output(all_events)

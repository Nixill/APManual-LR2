import data.strings as txt
from mod.classes import Event
from mod.json_types import JsonObject
from . import categories

all_events: list[Event] = [
]

event_table: JsonObject = Event.to_json_output(all_events)

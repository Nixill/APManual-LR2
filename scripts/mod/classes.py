from dataclasses import dataclass
from enum import Enum, Flag, auto
from typing import Any, Iterable, Optional

from .json_types import JsonObject, JsonObjectProperty, JsonValue

USE_LOCAL_SCHEMA = True
LOCAL_SCHEMA_LINK = '../../schemas/Manual.{0}.schema.json'
GITHUB_SCHEMA_LINK = 'https://raw.githubusercontent.com/ManualForArchipelago/Manual/refs/heads/main/schemas/Manual.{0}.schema.json'

def get_schema(type: str):
  return (LOCAL_SCHEMA_LINK if USE_LOCAL_SCHEMA else GITHUB_SCHEMA_LINK).format(type)

def name_of(item: str | HasName):
  if isinstance(item, HasName):
    return item.name
  else:
    return item

class HasName:
  name: str

#region Category
class Category(HasName):
  options: list[str] = []
  hidden: bool = False
  comment: Optional[str | list[str]] = None
  extra_data: Optional[JsonObject] = None

  def __init__(
      self,
      name: str,
      *,
      options: Optional[list[str | Option]] = None,
      hidden: bool = False,
      comment: Optional[str | list[str]] = None,
      extra_data: Optional[JsonObject] = None):
    self.name = name
    if options: self.options = [name_of(option) for option in options]
    self.hidden = hidden
    self.comment = comment
    if extra_data: self.extra_data = dict(extra_data)

  def to_json_kvp(self) -> JsonObjectProperty:
    out = {}
    if self.options: out['yaml_option'] = self.options
    if self.hidden: out['hidden'] = True
    if self.extra_data: out['extra_data'] = self.extra_data
    if self.comment: out['_comment'] = self.comment
    return (self.name, out)

  def to_json(self) -> JsonObject:
    return self.to_json_kvp()[1]

  @staticmethod
  def to_json_output(categories: Iterable[Category]) -> JsonObject:
    return {
      '$schema': get_schema('categories'),
      **{cat.name: cat.to_json() for cat in categories}
    }
#endregion

#region Event
class Event(HasName):
  requires: Optional[str] = None
  category: list[str] = []
  region: Optional[str] = None
  copy_location: Optional[str] = None
  visible: bool = False
  sort_key: Optional[str] = None
  comment: Optional[str] = None
  extra_data: Optional[JsonObject] = None

  def __init__(
      self,
      name: str,
      *,
      requires: Optional[str] = None,
      category: list[Category | str] = [],
      region: Optional[Region | str] = None,
      copy_location: Optional[Location | str] = None,
      visible: bool = False,
      sort_key: Optional[str] = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    if ':' in name or '(' in name or ')' in name:
      raise ValueError('Event names cannot contain colons or parentheses.')
    self.name = name
    if requires: self.requires = requires
    if category: self.category = [name_of(cat) for cat in category]
    if region: self.region = name_of(region)
    if copy_location: self.copy_location = name_of(copy_location)
    self.visible = visible
    self.sort_key = sort_key
    self.extra_data = extra_data
    self.comment = comment

  def to_json(self) -> JsonObject:
    out: JsonObject = {
      'name': self.name
    }
    if self.requires: out['requires'] = self.requires
    if self.category: out['category'] = list(self.category)
    if self.region: out['region'] = self.region
    if self.copy_location: out['copy_location'] = self.copy_location
    if self.visible: out['visible'] = True
    if self.sort_key: out['sort-key'] = self.sort_key
    if self.extra_data: out['extra_data'] = dict(self.extra_data)
    if self.comment: out['_comment'] = self.comment
    return out

  @staticmethod
  def to_json_output(events: Iterable[Event]) -> JsonObject:
    return {
      '$schema': get_schema('events'),
      'data': [event.to_json() for event in events]
    }
#endregion

#region Game
class Game:
  game: str
  creator: str
  filler_item_name: str
  starting_items: Optional[list[StartingItem]] = None
  death_link: bool = False
  starting_index: int = 1
  unused_goals_are_locations: bool = False
  version: str = '0.0.0'
  extra_data: Optional[JsonObject] = None
  comment: Optional[str] = None

  def __init__(
      self,
      game: str,
      creator: str,
      filler_item_name: str,
      *,
      starting_items: Optional[list[StartingItem]] = None,
      death_link: bool = False,
      starting_index: int = 1,
      unused_goals_are_locations: bool = False,
      version: Optional[str] = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    self.game = game
    self.creator = creator
    self.filler_item_name = filler_item_name
    if starting_items: self.starting_items = list(starting_items)
    self.death_link = death_link
    self.starting_index = starting_index
    self.unused_goals_are_locations = unused_goals_are_locations
    if version: self.version = version
    if extra_data: self.extra_data = dict(extra_data)
    if comment: self.comment = comment

  def to_json(self) -> JsonObject:
    out: JsonObject = {
      'game': self.game,
      'creator': self.creator,
      'filler_item_name': self.filler_item_name
    }
    if self.starting_items: out['starting_items'] = [si.to_json() for si in self.starting_items]
    if self.death_link: out['death_link'] = True
    if self.starting_index > 1: out['starting_index'] = self.starting_index
    if self.unused_goals_are_locations: out['unused_goals_are_locations'] = True
    return out

  def to_json_output(self) -> JsonObject:
    return {
      '$schema': get_schema('game'),
      **self.to_json()
    }

class StartingItem:
  items: Optional[list[str]] = None
  item_categories: Optional[list[str]] = None
  random: Optional[int] = None
  if_previous_item: Optional[list[str]] = None
  yaml_option: Optional[list[str]] = None
  comment: Optional[str] = None

  def __init__(
      self,
      items: Optional[list[str | Item]] = None,
      *,
      item_categories: Optional[list[str | Category]] = None,
      random: Optional[int] = None,
      if_previous_item: Optional[list[str | Item]] = None,
      yaml_option: Optional[list[str | Option]] = None,
      comment: Optional[str] = None):
    if items: self.items = [name_of(item) for item in items]
    if item_categories: self.item_categories = [name_of(cat) for cat in item_categories]
    self.random = random
    if if_previous_item: self.if_previous_item = [name_of(prev) for prev in if_previous_item]
    if yaml_option: self.yaml_option = [name_of(option) for option in yaml_option]
    self.comment = comment

  def to_json(self) -> JsonObject:
    out: JsonObject = {}
    if self.items: out['items'] = list(self.items)
    if self.item_categories: out['item_categories'] = list(self.item_categories)
    if self.random: out['random'] = self.random
    if self.if_previous_item: out['if_previous_item'] = list(self.if_previous_item)
    if self.yaml_option: out['yaml_option'] = list(self.yaml_option)
    if self.comment: out['_comment'] = self.comment
    return out
#endregion

#region Item
class ItemClassification(Flag):
  TRAP = auto()
  FILLER = auto()
  USEFUL = auto()
  PROGRESSION = auto()
  PROGRESSION_SKIP_BALANCING = auto()
  def to_string(self) -> str:
    return (self.name or '').lower().replace('|', ' + ')

class Item(HasName):
  category: Optional[list[str]] = None
  item_class: ItemClassification = ItemClassification.FILLER
  count: int = 1
  classification_count: Optional[dict[ItemClassification, int]] = None
  early: bool = False
  local: bool = False
  sort_key: Optional[str] = None
  value: Optional[dict[str, int]] = None
  extra_data: Optional[JsonObject] = None
  comment: Optional[str] = None

  def __init__(
      self,
      name: str,
      item_class: Optional[ItemClassification] = None,
      count: Optional[int] = None,
      *,
      category: Optional[list[str | Category]] = None,
      classification_count: Optional[dict[ItemClassification, int]] = None,
      early: bool = False,
      local: bool = False,
      sort_key: Optional[str] = None,
      value: dict[str, int] | dict[Value, int] | None = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    if ':' in name or '(' in name or ')' in name:
      raise ValueError('Item names cannot contain colons or parentheses.')
    self.name = name
    if item_class: self.item_class = item_class
    if isinstance(count, int): self.count = count
    if category: self.category = [name_of(cat) for cat in category]
    if classification_count: self.classification_count = dict(classification_count)
    if early: self.early = True
    if local: self.local = True
    self.sort_key = sort_key
    if value: self.value = {name_of(key): val for key, val in value.items()}
    if extra_data: self.extra_data = dict(extra_data)
    self.comment = comment

  def to_json(self) -> JsonObject:
    out: JsonObject = {
      'name': self.name
    }
    if self.category: out['category'] = [name_of(cat) for cat in self.category]
    if self.classification_count:
      out['classification_count'] = {
        cls.to_string(): cnt
        for cls, cnt in self.classification_count.items()
      }
    else:
      if ItemClassification.TRAP in self.item_class: out['trap'] = True
      if ItemClassification.FILLER in self.item_class: out['filler'] = True
      if ItemClassification.USEFUL in self.item_class: out['useful'] = True
      if ItemClassification.PROGRESSION in self.item_class: out['progression'] = True
      if ItemClassification.PROGRESSION_SKIP_BALANCING in self.item_class: out['progression_skip_balancing'] = True
      out['count'] = self.count
    if self.early: out['early'] = True
    if self.local: out['local'] = True
    if self.sort_key: out['sort-key'] = self.sort_key
    if self.extra_data: out['extra_data'] = dict(self.extra_data)
    if self.comment: out['_comment'] = self.comment
    return out

  @staticmethod
  def to_json_output(items: Iterable[Item]) -> JsonObject:
    return {
      '$schema': get_schema('items'),
      'data': [item.to_json() for item in items]
    }
#endregion

#region Location
class Location(HasName):
  requires: str
  category: Optional[list[str]] = None
  victory: bool = False
  region: Optional[str] = None
  place_item: Optional[list[str]] = None
  place_item_category: Optional[list[str]] = None
  dont_place_item: Optional[list[str]] = None
  dont_place_item_category: Optional[list[str]] = None
  prehint: bool = False
  hint_entrance: Optional[str] = None
  sort_key: Optional[str] = None
  extra_data: Optional[JsonObject] = None
  comment: Optional[str] = None

  def __init__(
      self,
      name: str,
      requires: str,
      *,
      category: Optional[list[str | Category]] = None,
      victory: bool = False,
      region: Optional[str | Region] = None,
      place_item: Optional[Iterable[str | Item]] = None,
      place_item_category: Optional[Iterable[str | Category]] = None,
      dont_place_item: Optional[Iterable[str | Item]] = None,
      dont_place_item_category: Optional[Iterable[str | Category]] = None,
      prehint: bool = False,
      hint_entrance: Optional[str] = None,
      sort_key: Optional[str] = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    self.name = name
    self.requires = requires
    if category: self.category = [name_of(cat) for cat in category]
    if victory: self.victory = True
    if region: self.region = name_of(region)
    if place_item: self.place_item = [name_of(item) for item in place_item]
    if place_item_category: self.place_item_category = [name_of(cat) for cat in place_item_category]
    if dont_place_item: self.dont_place_item = [name_of(item) for item in dont_place_item]
    if dont_place_item_category: self.dont_place_item_category = [name_of(cat) for cat in dont_place_item_category]
    self.prehint = prehint
    self.hint_entrance = hint_entrance
    self.sort_key = sort_key
    if extra_data: self.extra_data = dict(extra_data)
    self.comment = comment

  def to_json(self) -> JsonObject:
    out: JsonObject = {
      'name': self.name
    }
    if self.requires: out['requires'] = self.requires
    if self.category: out['category'] = list(self.category)
    if self.victory: out['victory'] = True
    if self.place_item: out['place_item'] = list(self.place_item)
    if self.place_item_category: out['place_item_category'] = list(self.place_item_category)
    if self.dont_place_item: out['dont_place_item'] = list(self.dont_place_item)
    if self.dont_place_item_category: out['dont_place_item_category'] = list(self.dont_place_item_category)
    if self.prehint: out['prehint'] = True
    if self.hint_entrance: out['hint_entrance'] = self.hint_entrance
    if self.sort_key: out['sort-key'] = self.sort_key
    if self.extra_data: out['extra_data'] = dict(self.extra_data)
    if self.comment: out['_comment'] = self.comment
    return out

  @staticmethod
  def to_json_output(locations: Iterable[Location]) -> JsonObject:
    return {
      '$schema': get_schema('locations'),
      'data': [location.to_json() for location in locations]
    }
#endregion

#region Option
class OptionType(Enum):
  TOGGLE = 'Toggle'
  CHOICE = 'Choice'
  RANGE = 'Range'

@dataclass(frozen=True)
class OptionVisibility:
  template: bool = True
  simple_ui: bool = True
  complex_ui: bool = True
  spoiler: bool = True

  def to_json(self) -> list[str]:
    return [a for a in [
      'template' if self.template else None,
      'simple_ui' if self.simple_ui else None,
      'complex_ui' if self.complex_ui else None,
      'spoiler' if self.spoiler else None
    ] if a] or ['none']

class Option(HasName):
  type: OptionType
  display_name: Optional[str] = None
  description: Optional[list[str]] = None
  default: Optional[bool | int] = None
  hidden: bool = False
  visibility: Optional[OptionVisibility] = None
  group: Optional[str] = None
  extra_data: Optional[JsonObject] = None
  comment: Optional[str] = None

  def __init__(
      self,
      name: str,
      type: OptionType,
      *,
      display_name: Optional[str] = None,
      description: Optional[list[str]] = None,
      default: Optional[bool | int] = None,
      hidden: bool = False,
      visibility: Optional[OptionVisibility] = None,
      group: Optional[str] = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    self.name = name
    self.type = type
    if display_name: self.display_name = display_name
    if isinstance(description, list):
      self.description = list(description)
    elif isinstance(description, str):
      self.description = str.splitlines(description)
    self.default = default
    self.hidden = hidden
    self.visibility = visibility
    self.group = group
    self.extra_data = extra_data
    self.comment = comment

  def to_json(self) -> JsonObject:
    return self.to_json_kvp()[1]

  def to_json_kvp(self) -> JsonObjectProperty:
    out = {
      'type': self.type.value,
      'rich_text_doc': True
    }
    if self.display_name: out['display_name'] = self.display_name
    if self.description: out['description'] = self.description
    if self.default is not None: out['default'] = self.default
    if self.hidden: out['hidden'] = True
    if self.visibility: out['visibility'] = self.visibility.to_json()
    if self.group: out['group'] = self.group
    if self.extra_data: out['extra_data'] = self.extra_data
    if self.comment: out['_comment'] = self.comment
    return (self.name, out)

  @staticmethod
  def to_json_output(options: Iterable[Option]) -> JsonObject:
    core_options: JsonObject = {}
    user_options: JsonObject = {}
    for option in options:
      if isinstance(option, DeathLinkOption):
        core_options['death_link'] = option.to_json()
      elif isinstance(option, FillerTrapsOption):
        core_options['filler_traps'] = option.to_json()
      elif isinstance(option, GoalOption):
        core_options['goal'] = option.to_json()
      else:
        user_options[option.name] = option.to_json()

    return {
      '$schema': get_schema('options'),
      'core': core_options,
      'user': user_options
    }

class ToggleOption(Option):
  def __init__(
      self,
      name: str,
      *,
      display_name: Optional[str] = None,
      description: Optional[list[str]] = None,
      default: bool = False,
      hidden: bool = False,
      visibility: Optional[OptionVisibility] = None,
      group: Optional[str] = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    super().__init__(
      name=name,
      type=OptionType.TOGGLE,
      display_name=display_name,
      description=description,
      default=default,
      hidden=hidden,
      visibility=visibility,
      group=group,
      extra_data=extra_data,
      comment=comment)

  # since this doesn't add properties, it uses superclass
  # to_json functions unchanged

class DeathLinkOption(ToggleOption):
  def __init__(
      self,
      default: bool = False,
      *,
      description: Optional[list[str]] = None,
      display_name: Optional[str] = None,
      hidden: bool = False,
      visibility: Optional[OptionVisibility] = None,
      comment: Optional[str] = None):
    super().__init__(
      name='death_link',
      default=default,
      description=description,
      display_name=display_name,
      hidden=hidden,
      visibility=visibility,
      comment=comment)

  # since this doesn't add or remove properties, it uses
  # superclass to_json functions unchanged

class RangeOption(Option):
  range_start: int
  range_end: int
  values: Optional[dict[str, int]] = None

  def __init__(
      self,
      name: str,
      range_start: int,
      range_end: int,
      *,
      values: Optional[dict[str, int]] = None,
      display_name: Optional[str] = None,
      description: Optional[list[str]] = None,
      default: Optional[int] = None,
      hidden: bool = False,
      visibility: Optional[OptionVisibility] = None,
      group: Optional[str] = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    super().__init__(
      name=name,
      type=OptionType.RANGE,
      display_name=display_name,
      description=description,
      default=default,
      hidden=hidden,
      visibility=visibility,
      group=group,
      extra_data=extra_data,
      comment=comment)
    self.range_end = range_end
    self.range_start = range_start
    if values: self.values = dict(values)

  def to_json(self) -> JsonObject:
    return self.to_json_kvp()[1]

  def to_json_kvp(self) -> JsonObjectProperty:
    _, out = super().to_json_kvp()
    out['range_start'] = self.range_start
    out['range_end'] = self.range_end
    if self.values: out['values'] = dict(self.values)
    return (self.name, out)

class FillerTrapsOption(RangeOption):
  def __init__(
      self,
      values: Optional[dict[str, int]] = None,
      *,
      description: Optional[list[str]] = None,
      display_name: Optional[str] = None,
      hidden: bool = False,
      visibility: Optional[OptionVisibility] = None,
      comment: Optional[str] = None):
    super().__init__(
      name='filler_traps',
      range_start=0,
      range_end=100,
      values=values,
      description=description,
      display_name=display_name,
      hidden=hidden,
      visibility=visibility,
      extra_data=None,
      comment=comment)

  def to_json(self) -> JsonObject:
    return self.to_json_kvp()[1]

  def to_json_kvp(self) -> JsonObjectProperty:
    _, out = super().to_json_kvp()
    del out['range_start']
    del out['range_end']
    return (self.name, out)

class ChoiceOption(Option):
  values: dict[str, int]
  aliases: Optional[dict[str, int]] = None
  allow_custom_value: bool = False

  def __init__(
      self,
      name: str,
      values: dict[str, int],
      *,
      aliases: Optional[dict[str, int]] = None,
      allow_custom_value: bool = False,
      display_name: Optional[str] = None,
      description: Optional[list[str]] = None,
      default: Optional[int] = None,
      hidden: bool = False,
      visibility: Optional[OptionVisibility] = None,
      group: Optional[str] = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    super().__init__(
      name,
      OptionType.CHOICE,
      display_name=display_name,
      description=description,
      default=default,
      hidden=hidden,
      visibility=visibility,
      group=group,
      extra_data=extra_data,
      comment=comment)
    self.values = dict(values)
    if aliases: self.aliases = dict(aliases)
    self.allow_custom_value = allow_custom_value

  def to_json(self) -> JsonObject:
    return self.to_json_kvp()[1]

  def to_json_kvp(self) -> JsonObjectProperty:
    _, out = super().to_json_kvp()
    out['values'] = dict(self.values)
    if self.aliases: out['aliases'] = dict(self.aliases)
    if self.allow_custom_value: out['allow_custom_value'] = True
    return (self.name, out)

class GoalOption(ChoiceOption):
  def __init__(
      self,
      aliases: Optional[dict[str, int]] = None,
      *,
      display_name: Optional[str] = None,
      description: Optional[list[str]] = None,
      default: Optional[int] = None,
      hidden: bool = False,
      visibility: Optional[OptionVisibility] = None,
      comment: Optional[str] = None):
    super().__init__(
      name='goal',
      values={},
      aliases=aliases,
      allow_custom_value=False,
      display_name=display_name,
      description=description,
      default=default,
      hidden=hidden,
      visibility=visibility,
      comment=comment)

  def to_json(self) -> JsonObject:
    return self.to_json_kvp()[1]

  def to_json_kvp(self) -> JsonObjectProperty:
    _, out = super().to_json_kvp()
    del out['values']
    del out['allow_custom_value']
    del out['group']
    return (self.name, out)
#endregion

#region Region
class Region(HasName):
  starting: bool = False
  connects_to: Optional[list[str]] = None
  requires: Optional[str] = None
  entrance_requires: Optional[dict[str, str]] = None
  exit_requires: Optional[dict[str, str]] = None
  extra_data: Optional[JsonObject] = None
  comment: Optional[str] = None

  def __init__(
      self,
      name: str,
      requires: Optional[str] = None,
      *,
      starting: bool = False,
      connects_to: Optional[list[str | Region]] = None,
      entrance_requires: Optional[dict[str | Region, str]] = None,
      exit_requires: Optional[dict[str | Region, str]] = None,
      extra_data: Optional[JsonObject] = None,
      comment: Optional[str] = None):
    self.name = name
    self.requires = requires
    if connects_to: self.connects_to = [name_of(region) for region in connects_to]
    if starting: self.starting = True
    if entrance_requires:
      self.entrance_requires = {name_of(region): requires for region, requires in entrance_requires.items()}
    if exit_requires:
      self.exit_requires = {name_of(region): requires for region, requires in exit_requires.items()}
    if extra_data: self.extra_data = dict(extra_data)
    self.comment = comment

  def to_json_kvp(self) -> JsonObjectProperty:
    out = {}
    if self.requires: out['requires'] = self.requires
    if self.starting: out['starting'] = True
    if self.connects_to: out['connects_to'] = list(self.connects_to)
    if self.entrance_requires: out['entrance_requires'] = dict(self.entrance_requires)
    if self.exit_requires: out['exit_requires'] = dict(self.exit_requires)
    if self.extra_data: out['extra_data'] = dict(self.extra_data)
    if self.comment: out['_comment'] = self.comment
    return (self.name, out)

  def to_json(self) -> JsonObject:
    return self.to_json_kvp()[1]

  @staticmethod
  def to_json_output(regions: Iterable[Region]) -> JsonObject:
    return {
      '$schema': get_schema('regions'),
      **{region.name: region.to_json() for region in regions}
    }
#endregion

#region
class Value(HasName):
  def __init__(self, name: str):
    self.name = name
#endregion

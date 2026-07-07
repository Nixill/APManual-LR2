from enum import Enum
from typing import Optional

from .classes import Category, ChoiceOption, HasName, Option, RangeOption, ToggleOption, Value, name_of, Item, Event

def item(item: str | Item | Event, count: Optional[int] = None, *, percent: Optional[int] = None, all: bool = False, half: bool = False) -> str:
  if count: return f'|{name_of(item)}:{count}|'
  elif percent: return f'|{name_of(item)}:{percent}%|'
  elif all: return f'|{name_of(item)}:ALL|'
  elif half: return f'|{name_of(item)}:HALF|'
  else: return f'|{name_of(item)}|'

def category(cat: str | Category, count: Optional[int] = None, *, percent: Optional[int] = None, all: bool = False, half: bool = False) -> str:
  if count: return f'|@{name_of(cat)}:{count}|'
  elif percent: return f'|@{name_of(cat)}:{percent}%|'
  elif all: return f'|@{name_of(cat)}:ALL|'
  elif half: return f'|@{name_of(cat)}:HALF|'
  else: return f'|@{name_of(cat)}|'

def any(*conds: str) -> str:
  return f'({' or '.join(conds)})'

def all(*conds: str) -> str:
  return f'({' and '.join(conds)})'

def item_value(key: str | Value, count: int) -> str:
  return f'{{ItemValue({name_of(key)}:{count})}}'

def opt_one(item: Optional[str | Item | Event] = None, *, category: Optional[str | Category] = None) -> str:
  if item: return f'{{OptOne({name_of(item)})}}'
  elif category: return f'{{OptOne(@{name_of(category)})}}'
  else: raise ValueError('Need either item or category.')

def opt_all(requirement: str) -> str:
  return f'{{OptAll({requirement})}}'

def option_count(*, item: Optional[str | Item | Event] = None, option: str | Option, category: Optional[str | Category] = None) -> str:
  name = name_of(item) if item else f'@{name_of(category)}' if category else None
  if not name: raise ValueError('item or category is required!')
  return f'{{OptionCount({name}, {name_of(option)})}}'

def option_count_percent(*, item: Optional[str | Item | Event] = None, option: str | Option, category: Optional[str | Category] = None) -> str:
  name = name_of(item) if item else f'@{name_of(category)}' if category else None
  if not name: raise ValueError('item or category is required!')
  return f'{{OptionCountPercent({name}, {name_of(option)})}}'

def yaml_enabled(option: str | Option) -> str:
  return f'{{YamlEnabled({name_of(option)})}}'

def yaml_disabled(option: str | Option) -> str:
  return f'{{YamlDisabled({name_of(option)})}}'

class ComparatorSymbol(Enum):
  EQUAL = '='
  INEQUAL = '!='
  GREATER_EQUAL = '>='
  LESS_EQUAL = '<='
  GREATER = '>'
  LESS = '<'

ComparatorSymbol.EQUAL._add_value_alias_('==')

def yaml_compare(option: str | Option, symbol: ComparatorSymbol | str, value: str | int | bool):
  if isinstance(symbol, ComparatorSymbol):
    symbol = symbol.value
  elif symbol not in ComparatorSymbol:
    raise KeyError(f'{symbol} is not a valid comparator symbol!')

  if isinstance(option, str): return f'{{YamlCompare({option} {symbol} {value})}}' # no type checking

  # type checking!
  if isinstance(value, str):
    if isinstance(option, RangeOption):
      if not option.values:
        raise KeyError(f'Comparing string against yaml range option {option.name} without string values')
      elif value not in option.values:
        raise KeyError(f'Comparing yaml option {option.name} against nonexistent key {value}')
    elif symbol not in ['=', '==', '!=']:
      raise KeyError(f'Strings can only be compared for equality or inequality, except in Range options.')
    elif isinstance(option, ToggleOption):
      if value.lower() not in ['0', '1', 'true', 'false', 'on', 'off']:
        raise KeyError(f'ToggleOptions can only be compared to 0 / false / off or 1 / true / on.')
    elif isinstance(option, ChoiceOption):
      if value not in option.values and option.aliases and value not in option.aliases and not option.allow_custom_value:
        raise KeyError(f'Comparing yaml choice option {option.name} against key {value}')
  elif isinstance(value, int):
    if isinstance(option, ChoiceOption):
      if value not in option.values.values():
        raise KeyError(f'Comparing yaml choice option {option.name} against nonexistent choice value {value}')
    elif isinstance(option, ToggleOption):
      if symbol not in ['=', '==', '!=']:
        raise KeyError(f'ToggleOptions can only be compared for equality or inequality.')
      if value not in [0, 1]:
        raise KeyError(f'ToggleOptions can only be compared against an int that is 0 or 1.')
  elif isinstance(value, bool):
    if symbol not in ['=', '==', '!=']:
      raise KeyError(f'Bools can only be compared for equality or inequality.')
    elif not isinstance(option, ToggleOption):
      raise TypeError(f'Bools can only be compared against ToggleOptions.')

  return f'{{YamlCompare({option} {symbol} {value})}}' # completed type checking

def custom_yaml_function(function_name: str, *function_args: str | HasName):
  return f'{{{function_name}({','.join((name_of(arg) for arg in function_args))})}}'

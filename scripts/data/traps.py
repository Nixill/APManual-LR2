from dataclasses import dataclass

@dataclass(frozen=True)
class Trap:
  name: str
  default_weight: int
  uses_cheats: bool
  description: list[str]

item_embargo = Trap(
  'Item embargo', 50, False,
  ['You may not use items for the duration of a race.'])
freeze = Trap(
  'Freeze', 50, False,
  ['You must hold the brakes for 15 seconds at the start of a race.'])
destroy_car = Trap(
  'Destroy your car', 50, False,
  ['You must destroy your car at some point during a race.'])
no_pitstops = Trap(
  'No pitstops', 50, False,
  ['You must not use the pits at any point during a race.'])
no_shortcuts = Trap(
  'No shortcuts', 50, False,
  ['You must not take any shortcuts during a race.'])
drive_reverse = Trap(
  'Drive in reverse', 50, False,
  ['You must drive in reverse into lap 2 and maintain it for 30 seconds during a race.'])
top_camera = Trap(
  'Top-down camera', 50, True,
  ['You must use the top-down camera cheat for a race.', '', 'This is a cheat-based trap.'])
speed_boost = Trap(
  'Speed boost', 10, True,
  ['You must use the speed boost cheat for a race.', '', 'This is a cheat-based trap.'])
quit_adventure = Trap(
  'Quit adventure', 50, False,
  ['You must immediately quit to main menu without saving.'])

all_traps = [
  item_embargo,
  freeze,
  destroy_car,
  no_pitstops,
  no_shortcuts,
  drive_reverse,
  top_camera,
  speed_boost,
  quit_adventure
]

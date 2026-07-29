# Welcome! This script is designed to show you what traps you have
# pending and to select traps for you when too many await you to be
# active all at once.

from collections import Counter
import random

trap_inventory = Counter[str]()
trap_completion = Counter[str]()

def random_weight[T](weights: dict[T, int], randomizer: random.Random | None) -> T:
    total_weight = sum(weights.values())

    if total_weight <= 0:
        raise ValueError('dict object is empty or has total weight <= 0')

    selection = (randomizer or random).randint(0, total_weight - 1)

    for item, weight in weights.items():
        if weight > selection:
            return item
        else:
            selection -= weight

    raise IndexError('I don\'t know how you got here.')

while True:
  print(f'You have {sum(trap_inventory.values())} traps waiting.')
  print(f'You may enter the following commands:')
  print(f'- \'list\': List all traps.')
  print(f'- \'add (name) [number]\': Add traps to your pending inventory.')
  print(f'- \'set (name) (number)\': Set your current trap count.')
  print(f'- \'roll\': Roll a set of up to three traps for a race.')

  line = input('> ')
  print()

  words = line.split()

  cmd = words[0].lower()

  try:
    if cmd == 'add':
      if len(words) >= 3 and words[-1].isnumeric():
        amount = int(words[-1])
        name = ' '.join(words[1:-1])
      elif len(words) >= 2:
        amount = 1
        name = ' '.join(words[1:])
      else: raise IndexError("Usage: 'add (name) [number]'")

      name = name.title()

      trap_inventory[name] += amount

      print(f'Added {name} ×{amount} to the trap inventory! ({trap_inventory[name]} pending)')
    elif cmd == 'set':
      if len(words) >= 3 and words[-1].isnumeric():
        amount = int(words[-1])
        name = ' '.join(words[1:-1])
      else: raise IndexError("Usage: 'set (name) (number)'")

      name = name.title()

      trap_inventory[name] = max(amount - trap_completion[name], 0)

      print(f'Set {name} to {trap_inventory[name] + trap_completion[name]} instances '\
            f'({trap_inventory[name]} pending, {trap_completion[name]} completed)')
    elif cmd == 'list':
      for k, v in trap_inventory.items():
        print(f'{k}: {v} pending, {trap_completion[k]} completed')
    elif cmd == 'roll':
      trap_bag = {k: v for k, v in trap_inventory.items() if v >= 0}
      if len(trap_bag) == 0:
        print('You have no traps pending, good racing!')
        selection = []
      if len(trap_bag) < 3:
        selection = list(trap_bag.keys())
      else:
        selection: list[str] = []

        for i in range(0, 3):
          selection.append(random_weight(trap_bag, None))
          del trap_bag[selection[i]]

      if selection:
        print('You have rolled the following traps:')
        for trap in selection:
          trap_inventory[trap] -= 1
          trap_completion[trap] += 1
          print(f'- {trap}')
    elif cmd == 'clear':
      if len(words) >= 3 and words[-1].isnumeric():
        amount = int(words[-1])
        name = ' '.join(words[1:-1])
      elif len(words) >= 2:
        amount = 1
        name = ' '.join(words[1:])
      else: raise IndexError("Usage: 'clear (name) [number]'")

      name = name.title()
      amount = min(amount, trap_inventory[name])

      trap_inventory[name] -= amount
      trap_completion[name] += amount

      print(f'Cleared {name} ×{amount} from the trap inventory! ({trap_inventory[name]} pending, {trap_completion[name]} completed)')
  except IndexError as e:
    print(e.__notes__)
  except KeyboardInterrupt:
    break

  print()

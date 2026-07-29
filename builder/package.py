import json

from typing import Iterable
from zipfile import ZipFile
from os import scandir
from datetime import datetime

from outputs.game import game, game_table
from outputs.categories import category_table
from outputs.items import item_table
from outputs.regions import region_table
from outputs.locations import location_table
from outputs.options import option_table
from outputs.events import event_table
from mod.json_types import JsonObject

manual_name = f'Manual_{game.game}_{game.creator}'

# Use the build log to generate a version number and build number
with open(f'output/{manual_name}.build.log', 'rt') as file:
  game_table['build'] = build_number = len(file.readlines()) + 1

# Build the JSON files from the data in these folders first
for filename, contents in [
  ('game', game_table),
  ('items', item_table),
  ('categories', category_table),
  ('regions', region_table),
  ('locations', location_table),
  ('options', option_table),
  ('events', event_table),
]:
  with open(f'src/data/{filename}.json', 'wt') as file:
    json.dump(contents, file, indent='  ')
    print(f'Wrote json file: {filename}.json')

print('make_json.py done!')
print()

# Now package everything!
def recursive_listdir(path: str = '.', files_only: bool = True, exclude_prefix: bool = True) -> Iterable[str]:
  for entry in scandir(path):
    if entry.is_file():
      if exclude_prefix: yield entry.path.removeprefix(path).removeprefix('/').removeprefix('\\')
      else: yield entry.path
    elif entry.is_dir():
      if not files_only:
        if exclude_prefix: yield entry.path.removeprefix(path).removeprefix('/').removeprefix('\\')
        else: yield entry.path
      for file in recursive_listdir(entry.path, files_only, False):
        if exclude_prefix: yield file.removeprefix(path).removeprefix('/').removeprefix('\\')
        else: yield file

with ZipFile(f'output/{manual_name}.apworld', 'w') as apworld:
  for path in recursive_listdir('src'):
    path = path.replace('\\', '/')
    origpath = f'src/{path}'
    arcpath = f'{manual_name}/{path}'
    apworld.write(origpath, arcpath)
    print(f'Wrote to archive: {path}')

print('package.py done!')

# And append to the log
with open(f'output/{manual_name}.build.log', '+at') as file:
  file.write(f'Build {build_number} - {datetime.now()}\n')

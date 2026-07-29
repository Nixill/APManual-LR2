from mod.classes import Game, StartingItem
from outputs import items
import data.worlds as worlds

game = Game(
  game='LEGORacers2',
  creator='Nixill',
  filler_item_name='Nothing',
  death_link=True,
  starting_items=[StartingItem([items.exploration_keys_dict[worlds.sandy_bay.name]])],
)

game_table = game.to_json_output()

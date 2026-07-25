from mod.classes import Game, StartingItem
from . import items

game = Game(
  game='game',
  creator='creator',
  filler_item_name='Nothing',
  # This defaults to True because it's always optional by the player.
  # Turn it off if Death Link makes no sense for your game.
  death_link=True,
  starting_items=[],
)

game_table = game.to_json_output()

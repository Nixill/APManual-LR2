from mod.classes import Game

game = Game(
  game='LEGORacers2',
  creator='Nixill',
  filler_item_name='Cheese Wedge Brick',
  death_link=True
)

game_table = game.to_json_output()

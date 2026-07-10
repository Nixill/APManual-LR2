from dataclasses import dataclass

@dataclass(frozen=True)
class LegoWorld:
  name: str
  race_names: list[str]
  boss_race_name: str | None
  golden_brick_names: tuple[str, str, str]
  npc_names: list[str]
  bonus_npc_names: list[str]
  world_index: int
  race_npc_names: list[str] | None = None
  boss_npc_name: str | None = None

sandy_bay = LegoWorld(
  name='Sandy Bay',
  race_names=['Dig-a-Brick', 'Express Delivery', 'Hot Stuff', "Bobby's Beat"],
  boss_race_name=None,
  golden_brick_names=('Beachside', 'Cliffside', 'Mountain'),
  npc_names=[
    '(player)',
    'Ben',
    'Doctor Dave',
    'Fisherman',
    'Foreman Stu',
    'Gillian',
    'Jan',
    'Jay',
    'Jimmy',
    'Laura',
    'Nurse Nikki',
    'Pauline',
    'Rachel',
    'Sparky',
    'Steve',
    'Suzie',
    'Tony the Coastguard',
    'Workman Jon',
    'Workman Rob',
  ],
  bonus_npc_names=['Captain Geoff'],
  race_npc_names=['Workman Fred', 'Mike the Postman', 'Fireman Gavin', 'PC Bobby'],
  world_index=1
)

dino_island = LegoWorld(
  name='Dino Island',
  race_names=['Tribal Trouble', 'Dino Dodgems', 'The Lost Race World', 'Cretaceous Canyon'],
  boss_race_name="Sam Sanister's Slammer",
  boss_npc_name='Sam Sanister',
  golden_brick_names=('Plateau', 'Oceanside', 'Jungle'),
  npc_names=['Achu', 'Alexandria Sanister', 'Bungo', 'Mike', 'Morat', 'Slyboots'],
  bonus_npc_names=['Johnny Thunder', 'Pippin'],
  world_index=2
)

mars = LegoWorld(
  name='Mars',
  race_names=['The Phobos Anomaly', 'Red Run', 'Deimos Derby', 'Contact'],
  boss_race_name="Riegel's Racetrack",
  boss_npc_name='Riegel',
  golden_brick_names=('Powerstore', 'Gold Mine', 'Alien Base'),
  npc_names=['Altair', 'Antares', 'BB', 'Doc (Mars)', 'Scientist', 'Vega'],
  bonus_npc_names=[],
  world_index=3
)

arctic = LegoWorld(
  name='Arctic',
  race_names=['Winter Wonderland', 'Ice Canyons', 'Slip Sliding', 'Chill Thrill'],
  boss_race_name="The Berg's Royal Rumble",
  boss_npc_name='The Berg',
  golden_brick_names=('Crash Site', 'Trapped Ship', 'Base Camp'),
  npc_names=['Captain Ross', 'Chilly', 'Cosmo', 'Crystal', 'Doc (Arctic)', 'Frosty'],
  bonus_npc_names=[],
  world_index=4
)

xalax = LegoWorld(
  name='Xalax',
  race_names=['Wheeled Warriors', "Smash 'n' Bash", 'Vertigo', 'Beyond the Dome'],
  boss_race_name="The Grand Finale",
  golden_brick_names=('Tubeside', 'Jump Ramp', 'Dormant Volcano'),
  npc_names=[],
  bonus_npc_names=['Warrior'],
  world_index=5
)

all_worlds = [sandy_bay, dino_island, mars, arctic, xalax]
'''All five LEGO worlds.'''

world_dict = {world.name: world for world in all_worlds}
'''Dict of world name to world.'''

boss_worlds = [dino_island, mars, arctic, xalax]
'''The four LEGO worlds that have a boss.'''

mid_worlds = [dino_island, mars, arctic]
'''The three LEGO worlds accessible via Golden Bricks.'''

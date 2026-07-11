# Options for LEGO Racers 2 Archipelago
## `save_mode`
This option lets you define how you'll play the Archipelago regarding saved game progress. You may choose from the following values:
- **New game**: You start the run without using any existing saves. Select "New Game" from the Adventure menu and then follow the prompts.
- **New game with cheats**: As above, but at the start of the run you use the "Unlock Arctic" cheat code (←←→→←←→→↑←→) to unlock Dino Island, Mars, and Arctic.
  - Note that this is accomplished by simply marking the races of Sandy Bay and Arctic, plus "Tribal Trouble" from Dino Island, as having already been completed. The player is still expected to do those races for checks, as well as clearing the Arctic races before The Berg and Tribal Trouble (in addition to the other Dino Island races) before Sam Sanister. However, clearing Sandy Bay's races before performing checks outside of Sandy Bay is not required or expected.
- **Finished save**: You start the run with a save that has access to every race in every world. This save must not have completed any bonus games or picked up any golden bricks from on the ground. Such a save is available in the `saves` folder of this repository.

You will also be granted an item at the start of the run that states which mode is in use. Check the `[0.0] Run Settings` section of your inventory. This is in case you have Archipelago select save mode randomly.

## `boss_keys_available`
This is the number of boss keys that are generated in the multiworld, from 1 to 10 per boss (Sam Sanister, Riegel, and The Berg).

Note that locations must outnumber non-filler items by at least 5. If the player's settings cause this condition to be violated, `boss_keys_available` and `xalax_keys_available` will be decreased and `boss_check_count` increased until the condition is met.

## `boss_keys_needed`
This is the percentage of needed boss keys in order to partake in the boss race in question.

It is rounded down, with a minimum of 1, except that exactly truncated percentage values will round up instead. (For example, 33% of 6 keys is 2 rather than rounding down to 1.) This also means that there will always be at least 1 spare key unless the number of available keys is exactly 1 or this setting is exactly 100.

## `xalax_keys_available` and `xalax_keys_needed`
These options have the same effect as `boss_keys_available` and `boss_keys_needed`, except that they control access to The Grand Finale.

## `boss_check_count`
This option is the number of checks clearing a boss race grants the player.

Note that locations must outnumber non-filler items by at least 5. If the player's settings cause this condition to be violated, `boss_check_count` will be increased and `boss_keys_available` and `xalax_keys_available` decreased until the condition is met.

## `filler_weight_`(name)
These options control the relative distribution of the Filler and Trap items.

The chance for any particular filler to be generated is dependent on the total of the weights. Under default settings, every trap (and the Cheese Wedge Brick filler) has a 12.5% chance (50 out of 400) of being selected as a filler item, except for the two traps that use cheats, which are disabled (0 out of 400) by default.

## `car_bonus_weight_`(name)
These options control both the relative distribution weight *and* the total number of each car bonus available.

Exactly 10 car bonuses will always be selected. Please observe the following notes:
- If the total of the car bonus weights is **exactly 10**, then that exactly defines the list and counts of car bonuses that will be given.
- If the total of the car bonus weights **exceeds 10**, then those will be put in a list and 10 of them will be randomly selected.
- If the total of the car bonus weights is **under 10**, then all of the selected bonuses will be guaranteed, and the remainder selected at random from the unpicked options. (For example, 9 Power 0 Grip 0 Shield means that you are guaranteed 9 Power, while the tenth car bonus has a 1/21 chance of being Power and a 10/21 chance each of being Grip or Shield.)

In a future version of this Archipelago Randomizer, there will be an option to run with fewer than 10 car bonuses, simply skipping some bonus games.

## `enable_npc_checks`
Whether talking to NPCs should constitue a check for each unique NPC.

*(This option could conceivably be called something like "talksanity", but the author of this apworld chooses not to follow such a naming convention.)*

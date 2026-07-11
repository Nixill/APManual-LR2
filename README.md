# Manual for Archipelago - LEGO Racers 2 (Nixill)
This is a **remake** of the LEGO Racers 2 AP (which is on the `racers-2-original` branch)!

## Setup
You need the following software:
- A legally acquired copy of LEGO Racers 2 in your computer's CD Drive
- The [LEGO Racers 2 APWorld](https://github.com/Nixill/APManuals/releases?q=LEGO+Racers+2&expanded=true)

It is assumed you are familiar with [setting up Archipelago](https://archipelago.gg/tutorial/Archipelago/setup_en) and [connecting the Manual Client](https://github.com/ManualForArchipelago/Manual/blob/main/docs/play/connect-client.md). If not, use those links for more information.

### Save Modes
The YAML has an option for "save mode", which has three choices. Where you need to start your archipelago experience depends on which mode you're using. If you select random, check your inventory - you will receive an item matching your save mode.
- **If you are using the "New Game" save mode,** which is the **default,** then open LEGO Racers 2 and start a new game. It is recommended your starting point for the AP be the last confirmation before car selection.
- **If you are using the "New Game With Cheats" save mode,** then the same applies. However, once you are in-game, pause and press the following keys on the pause menu: Left Left Right Right Left Left Right Right Up Right Left. It is recommended that your starting point for the AP be just after entering this cheat code.
- **If you are using the "Finished Save" save mode,** then you will need to have a saved game with all races accessible (which means that every race has been beaten except for The Grand Finale, which is optional), but no bonus games have been played nor have any on-the-ground golden bricks been picked up. Such a save is included in the release if you would like it. It is recommended that your starting point for the AP be somewhere in Sandy Bay.

## Restrictions on Play
LEGO Racers 2's normal rules apply, except:
- You may not play a race until you have received that race's Race Key.
- You may not collect Golden Bricks from the ground of a world until you have received that world's Exploration Key.
- You may not play a bonus game until you have received that world's Bonus Game Key (once for the easy, twice for the hard) *and* its Exploration Key.
- Upon winning a bonus game, you must select the Upgrade that unlocked that bonus game as the reward for completing it. (If you have multiple Upgrades pending, you may apply them at any order; you simply may not have more of any upgrade in-game than you have received from Archipelago.)

At the start of the run, you have only the Sandy Bay Exploration Key, and you can grab its three Golden Bricks and its numerous NPC checks, if applicable.

You must also watch the "Traps" section of your inventory. Upon receiving a trap, you must follow the associated instructions on the [traps page](docs/traps.md).

## Performing checks
To perform checks, you take the following actions:
- You perform a Bonus Game Unlock check immediately upon receiving any "Upgrade" item.
- You perform a Race check by winning the named race.
- You perform *all* Boss checks simultaneously by beating that boss in a race *once*.
  - Note: For a "new game" save mode, you must win all prior races in that world first. This applies even to the Arctic in the "New Game with Cheats" mode, despite the cheat automatically unlocking that boss race.
- You perform a Golden Brick check by collecting that Golden Brick.
  - Which golden brick goes to which name is explained [here](docs/golden-bricks.md).
- You perform a Bonus Game Completion check by winning that minigame.
- You perform an NPC check by completing a conversation in which the named NPC talks.

Note that you do not perform ANY checks if you have opted into the DeathLink system, and you have received a death without acknowledging it. (See the [DeathLink](#death-link) section for more info.)

## The Goal
The goal of this Archipelago is the same as the base game: Roll credits by beating Rocket Racer in a race on his own track.

Other goals are planned, but not yet implemented.

# The other stuff
## Options
The YAML options for this Archipelago are explained in detail [here](docs/options.md), but in short, are as follows:
- **Progression Balancing** and **Accessibility**: Default Archipelago options.
- **Death Link**: Whether or not you want to send and receive death links; see next section for details.
- **Save Mode**: Defines whether you want to use a pre-finished save or new game.
- **Boss Keys Available** and **Xalax Keys Available**: The number of keys you want to generate for each boss race.
- **Boss Keys Needed** and **Xalax Keys Needed**: The percentage of generated keys that are needed to access that race.
- **Boss Check Count**: The number of checks clearing a boss race should grant.
- **Weight of (trap name)**: The weight for generating that trap as a filler item.
- **Weight of (car bonus name)**: The weight for generating that car bonus as one of the ten bonuses in the run.
- **Enable NPC Checks**: Whether or not to include the 44 or 47 "talk to NPC" checks.

## Death Link
This Archipelago features Death Link support as follows:

**Send a death** (click the button so that it turns green and says "Sent!") when:
- You lose a race or minigame
- You reset a race or minigame (except because of an incoming death)
- You leave a race or minigame (except because of a Quit Adventure trap)
- LEGO Racers 2 crashes
Once the death is sent, click the button again so that it turns grey and says "Primed".

When you **receive a death** (the button is red and has a player's name on it): Immediately pause the game and select whichever Restart or Quit option is in the menu. If it's "Quit Adventure", you do not get to save first. (Once you have acknowledged a death, click the button to reset it to "primed".)

## Cheats
This Archipelago optionally makes use of some cheat codes. Default settings avoid them, but the player may choose to use them in settings. The cheat codes relevant to the Archipelago run are listed below. Cheats are entered in the main menu or the pause menu by pressing the arrow keys shown. A cheat code is accepted when you hear a laugh in the menu.

Super Speed and Top-Down Camera can be disabled by re-entering the cheat code.

A change to the Super Speed state takes effect only after a loading screen (restart doesn't count).

| Effect                               | Code                                                                                           |
| :----------------------------------- | :--------------------------------------------------------------------------------------------- |
| Unlock Dino Island, Mars, and Arctic | Left Left Right Right Left Left Right Right Up Left Right                                      |
| Super Speed                          | Left Right Up Down Right Left Up Down Left Right Up Down Right Left Up Down Left Right Up Down |
| Top-Down Camera                      | Left Up Up Up Right Up Up Up Left Up Up Up Right Up Up Up                                      |

# Disclaimer
This repository is not affiliated with Manual. I am not one of its core developers, simply an APWorld dev using it.

This project is also not affiliated with or endorsed by The LEGO Group.

Also, I'll leave Manual's own disclaimers here:

Manual is a fan project for use with the Archipelago multiworld project. 

Manual is not affiliated with or endorsed by the Archipelago project in any way.

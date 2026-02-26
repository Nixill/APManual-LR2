// A small script to make the items.json and locations.json files for the AP.

// NOTE: This script expects to be run from the *repository root* level!
// If running directly from its folder, uncomment the first non-using line.

using System.Text.Json;
using System.Text.Json.Nodes;
using System.Text.Json.Serialization;

// Directory.SetCurrentDirectory("..");

LegoWorld SandyBay = new LegoWorld(
  WorldName: "Sandy Bay",
  RaceNames: ["Dig-a-Brick", "Express Delivery", "Hot Stuff", "Bobby's Beat"],
  BossRaceName: null,
  GoldenBrickNames: ["Beachside", "Cliffside", "Mountain"],
  NPCNames: [
    "(player)",
    "Ben",
    "Captain Geoff",
    "Doctor Dave",
    "Fireman Gavin",
    "Fisherman",
    "Foreman Stu",
    "Gillian",
    "Jan",
    "Jay",
    "Jimmy",
    "Laura",
    "Mike the Postman",
    "Nurse Nikki",
    "Pauline",
    "PC Bobby",
    "Rachel",
    "Sparky",
    "Steve",
    "Suzie",
    "Tony the Coastguard",
    "Workman Fred",
    "Workman Jon",
    "Workman Rob"
  ],
  WorldIndex: 1,
  IsStartingWorld: true
);

LegoWorld DinoIsland = new LegoWorld(
  WorldName: "Dino Island",
  RaceNames: [
    "Tribal Trouble",
    "Dino Dodgems",
    "The Lost Race World",
    "Cretaceous Canyon"
  ],
  BossRaceName: "Sam Sanister's Slammer",
  GoldenBrickNames: [
    "Plateau",
    "Oceanside",
    "Jungle"
  ],
  NPCNames: [
    "Achu",
    "Alexandria Sanister",
    "Bungo",
    "Johnny Thunder",
    "Mike",
    "Morat",
    "Pippin",
    "Slyboots"
  ],
  WorldIndex: 2
);

LegoWorld Mars = new LegoWorld(
  WorldName: "Mars",
  RaceNames: [
    "The Phobos Anomaly",
    "Red Run",
    "Deimos Derby",
    "Contact"
  ],
  BossRaceName: "Riegel's Racetrak",
  GoldenBrickNames: [
    "Powerstore",
    "Gold Mine",
    "Alien Base"
  ],
  NPCNames: [
    "Altair",
    "Antares",
    "BB",
    "Doc (Mars)",
    "Scientist",
    "Vega"
  ],
  WorldIndex: 3
);

LegoWorld Arctic = new LegoWorld(
  WorldName: "Arctic",
  RaceNames: [
    "Winter Wonderland",
    "Ice Canyons",
    "Slip Sliding",
    "Chill Thrill"
  ],
  BossRaceName: "The Berg's Royal Rumble",
  GoldenBrickNames: [
    "Crash Site",
    "Trapped Ship",
    "Base Camp"
  ], NPCNames: [
    "Captain Ross",
    "Chilly",
    "Cosmo",
    "Crystal",
    "Doc (Arctic)",
    "Frosty"
  ],
  WorldIndex: 4
);

LegoWorld Xalax = new LegoWorld(
  WorldName: "Xalax",
  RaceNames: [
    "Wheeled Warriors",
    "Smash 'n' Bash",
    "Vertigo",
    "Beyond the Dome"
  ],
  BossRaceName: "The Grand Finale",
  GoldenBrickNames: [
    "Tubeside",
    "Jump Ramp",
    "Dormant Volcano"
  ],
  NPCNames: [
    "Warrior"
  ],
  WorldIndex: 5,
  IsFinalWorld: true
);

JsonSerializerOptions options = new JsonSerializerOptions
{
  DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
  WriteIndented = true,
  IndentCharacter = ' ',
  IndentSize = 4,
  NewLine = "\n"
};

// Note that these file paths are relative to the *root of this repository* (the parent directory to this file's location).
File.WriteAllText("Manual_LEGO Racers 2_Nixill/data/items.json", RemoveNullObj(new JsonObject
{
  ["$schema"] = "../../schemas/Manual.items.schema.json",
  ["data"] = new JsonArray([
    .. SandyBay.GetItems(),
    .. DinoIsland.GetItems(),
    .. Mars.GetItems(),
    .. Arctic.GetItems(),
    .. Xalax.GetItems(),
    .. GetTraps(),
    GetCheeseWedge()
  ])
}).ToJsonString(options));

File.WriteAllText("Manual_LEGO Racers 2_Nixill/data/locations.json", RemoveNullObj(new JsonObject
{
  ["schema"] = "../../schemas/Manual.locations.schema.json",
  ["data"] = new JsonArray([
    .. SandyBay.GetLocations(),
    .. DinoIsland.GetLocations(),
    .. Mars.GetLocations(),
    .. Arctic.GetLocations(),
    .. Xalax.GetLocations(),
    .. GetVictoryLocations()
  ])
}).ToJsonString(options));

IEnumerable<JsonObject> GetTraps() =>
[
  GetTrap("Item Embargo"),
  GetTrap("Freeze"),
  GetTrap("Destroy your Car"),
  GetTrap("Hold Talk"),
  GetTrap("No Shortcuts"),
  GetTrap("No Pitstops"),
  GetTrap("Drive in Reverse")
];

JsonObject GetTrap(string name) => new JsonObject
{
  ["name"] = $"TRAP - {name}",
  ["trap"] = true,
  ["count"] = 300
};

JsonObject GetCheeseWedge() => new JsonObject
{
  ["name"] = "Cheese Wedge",
  ["filler"] = true,
  ["count"] = 300
};

JsonObject RemoveNullObj(JsonObject input)
{
  var kvps = input.ToArray();
  foreach (var kvp in kvps)
  {
    if (kvp.Value is null) input.Remove(kvp.Key);
    else if (kvp.Value is JsonArray arr) RemoveNullArr(arr);
    else if (kvp.Value is JsonObject obj) RemoveNullObj(obj);
  }
  return input;
}

JsonArray RemoveNullArr(JsonArray input)
{
  for (int i = 0; i < input.Count; i++)
  {
    if (input[i] is null)
    {
      input.RemoveAt(i);
      i--;
    }
    else if (input[i] is JsonArray arr) RemoveNullArr(arr);
    else if (input[i] is JsonObject obj) RemoveNullObj(obj);
  }
  return input;
}

IEnumerable<JsonObject> GetVictoryLocations() =>
[
  new() {
    ["name"] = "The Grand Finale (Victory)",
    ["victory"] = true,
    ["requires"] = "{OptionCount(Xalax Boss Key, xalax_keys_needed)}"
  },
  new() {
    ["name"] = "All Bosses Defeated (Victory)",
    ["victory"] = true,
    ["requires"] = "{OptionCount(Xalax Boss Key, xalax_keys_needed)}"
      + string.Join("", Enumerable.Select(["Dino Island", "Mars", "Arctic"],
        s => $" and {{OptionCount({s} Boss Key, boss_keys_needed)}}"))
  },
  new() {
    ["name"] = "All Races Won (Victory)",
    ["victory"] = true,
    ["requires"] = "{OptionCount(Xalax Boss Key, xalax_keys_needed)}"
      + string.Join("", Enumerable.Select(["Dino Island", "Mars", "Arctic"],
        s => $" and {{OptionCount({s} Boss Key, boss_keys_needed)}}"))
      + string.Join("", Enumerable.SelectMany([DinoIsland, Mars, Arctic, Xalax],
        w => w.RaceNames).Select(s => $" and |{s} Race Key|"))
  },
  new() {
    ["name"] = "100% Completion (Victory)",
    ["victory"] = true,
    ["requires"] = "{OptionCount(Xalax Boss Key, xalax_keys_needed)} and |Xalax Exploration Key|"
      + string.Join("", Enumerable.Select(["Dino Island", "Mars", "Arctic"],
        s => $" and {{OptionCount({s} Boss Key, boss_keys_needed)}} and |{s} Exploration Key| and |{s} Hard Bonus Game Key|"))
      + string.Join("", Enumerable.SelectMany([DinoIsland, Mars, Arctic, Xalax],
        w => w.RaceNames).Select(s => $" and |{s} Race Key|"))
      + string.Join("", Enumerable.Select(["Sandy Bay", "Xalax"], s => $" and |{s} Hard Bonus Game Key|"))
  }
];

record class LegoWorld(string WorldName, string[] RaceNames, string? BossRaceName, string[] GoldenBrickNames, string[] NPCNames, int WorldIndex, bool IsStartingWorld = false, bool IsFinalWorld = false)
{
  public IEnumerable<JsonObject> GetItems()
  {
    if (!IsStartingWorld)
    {
      foreach (string race in RaceNames)
        yield return new JsonObject
        {
          ["name"] = $"{race} Race Key",
          ["progression"] = true,
          ["category"] = new JsonArray([WorldName, "Race Keys"])
        };
      yield return new JsonObject
      {
        ["name"] = $"{WorldName} Boss Key",
        ["classification_count"] = new JsonObject
        {
          ["progression"] = 5,
          ["useful"] = 5
        },
        ["category"] = new JsonArray([WorldName, "Boss Keys"])
      };
      yield return new JsonObject
      {
        ["name"] = $"{WorldName} Exploration Key",
        ["progression"] = true,
        ["category"] = new JsonArray([WorldName, "Exploration and Minigames"])
      };
    }
    yield return new JsonObject
    {
      ["name"] = $"{WorldName} Hard Bonus Game Key",
      ["classification_count"] = new JsonObject
      {
        ["progression"] = 1,
        ["useful"] = 1
      },
      ["category"] = new JsonArray([WorldName, "Exploration and Minigames"])
    };
  }

  public IEnumerable<JsonObject> GetLocations()
  {
    foreach ((int i, string race) in RaceNames.Index())
    {
      yield return new JsonObject
      {
        ["name"] = $"Race {i + 1}: {race}",
        ["region"] = WorldName,
        ["sort-key"] = $"{WorldIndex}-1-{i + 1}",
        ["requires"] = IsStartingWorld ? null : $"|{race} Race Key|",
        ["category"] = new JsonArray([WorldName])
      };
    }

    if (!IsStartingWorld)
    {
      foreach ((int i, string str) in Enumerable.Index(["", "Second", "Third", "Fourth", "Fifth"]))
      {
        List<JsonNode> cats = [];
        if (IsFinalWorld) cats.Add($"{WorldName} Boss Checks");
        if (i > 0) cats.Add($"{str} Boss Checks");
        yield return new JsonObject
        {
          ["name"] = $"Boss: {BossRaceName} (Check {i + 1})",
          ["requires"] = $"{{OptionCount({WorldName} Boss Key, {(IsFinalWorld ? "xalax" : "boss")}_keys_needed)}}",
          ["category"] = new JsonArray([WorldName, .. cats]),
          ["region"] = WorldName,
          ["sort-key"] = $"{WorldIndex}-2-{i + 1}"
        };
      }
    }

    yield return new JsonObject
    {
      ["name"] = $"Bonus Game: {WorldName} Easy",
      ["category"] = new JsonArray([WorldName, "Minigames"]),
      ["region"] = WorldName,
      ["sort-key"] = $"{WorldIndex}-3-1",
      ["requires"] = IsStartingWorld ? null : $"|{WorldName} Exploration Key|"
    };

    yield return new JsonObject
    {
      ["name"] = $"Bonus Game: {WorldName} Hard",
      ["category"] = new JsonArray([WorldName, "Minigames"]),
      ["requires"] = $"|{WorldName} Hard Bonus Game Key|{(IsStartingWorld ? "" : $" and |{WorldName} Exploration Key|")}",
      ["region"] = WorldName,
      ["sort-key"] = $"{WorldIndex}-3-2"
    };

    foreach ((int i, string brick) in GoldenBrickNames.Index())
    {
      yield return new JsonObject
      {
        ["name"] = $"Golden Brick: {brick}",
        ["requires"] = IsStartingWorld ? null : $"|{WorldName} Exploration Key|",
        ["region"] = WorldName,
        ["sort-key"] = $"{WorldIndex}-3-{i + 3}",
        ["category"] = new JsonArray([WorldName])
      };
    }

    foreach ((int i, string chr) in NPCNames.Index())
    {
      yield return new JsonObject
      {
        ["name"] = $"NPC: {chr}",
        ["category"] = new JsonArray([WorldName, "Talksanity"]),
        ["sort-key"] = $"{WorldIndex}-4-{i + 1}",
        ["requires"] = IsStartingWorld ? null : $"|{WorldName} Exploration Key|"
      };
    }
  }
}

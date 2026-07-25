JsonValue = bool | int | float | str | list['JsonValue'] | dict[str, 'JsonValue'] | None
JsonObject = dict[str, JsonValue]
JsonArray = list[JsonValue]
JsonProperty = tuple[str, JsonValue]
JsonObjectProperty = tuple[str, JsonObject]

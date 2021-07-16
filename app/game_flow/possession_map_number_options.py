import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    [
        Output("possession-map-number-dropdown", "options"),
        Output("possession-map-number-dropdown", "value"),
    ],
    [
        Input("game-flow-substitutions-graph", "clickData"),
        Input("game-flow-game-dropdown", "value"),
        Input("game-flow-home-away-dropdown", "value"),
    ],
    [
        State("possession-map-number-dropdown", "options"),
        State("possession-map-number-dropdown", "value"),
    ],
)
def possession_map_number_options(clickData, game_url, home_away, options, value):
    """Update the possession options based on a click on the game flow graph."""
    # Get game info
    g = audl.Game(game_url)
    events = g.get_events(home=bool(home_away), qc=False)

    if clickData is None:
        t = 0
    else:
        t = clickData["points"][0]["x"]

    # Get the point number associated with that game segment
    points = events.query(f"s_total=={t}")["point_number"].unique()

    # If the game segment doesn't exist for this game (old click data), use 0
    if len(points) > 0:
        point = points[0]
    else:
        point = events.query(f"s_total==0")["point_number"].iloc[0]

    # Get possessions associated with that point
    possessions = events.loc[
        (events["point_number"] == point) & (events["offensive_possession"]),
        "possession_number",
    ].unique()

    # Get the last play description for each possession
    final_play_in_possession = (
        events.loc[
            (events["point_number"] == point)
            & (events["offensive_possession"])
            & (events["play_description"] != ""),
        ]
        .groupby(["possession_number"])
        .tail(1)
        .set_index("possession_number")["play_description"]
        .str.replace("<br>", " ")
        .to_dict()
    )

    # Get all possessions
    if len(possessions) > 0:
        options = [
            {
                "label": final_play_in_possession.get(
                    possession_number, f"Possession {int(possession_number)}"
                ),
                "value": possession_number,
            }
            for possession_number in possessions
        ]
        value = options[0]["value"]
    # If no possessions, return message and blank map
    else:
        return [{"label": "No offensive possessions on this point", "value": -1}], -1

    return (options, value)

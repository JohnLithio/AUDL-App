import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    [
        Output("game-flow-game-dropdown", "options"),
        Output("game-flow-game-dropdown", "value"),
    ],
    [Input("game-flow-team-dropdown", "value"),],
    [State("game-flow-game-dropdown", "value"),],
)
def game_flow_game_dropdown(team, game):
    """Update the game options based on the selected team for the game flow graph."""
    # Get game info
    game_info = audl.Season().get_game_info()

    if team == "any":
        game_options = GAME_OPTIONS
    else:
        game_options = [
            {
                "label": f"{row['away_team']} at {row['home_team']}, {row['game_date']}",
                "value": row["url"],
            }
            for _, row in game_info.iterrows()
            if row["events_exist"]
            and ((row["away_team"] == team) or (row["home_team"] == team))
        ]

    if game not in [x["value"] for x in game_options]:
        game = game_options[0]["value"]

    return game_options, game

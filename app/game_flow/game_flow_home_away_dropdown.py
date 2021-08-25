import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    [
        Output("game-flow-home-away-dropdown", "options"),
        Output("game-flow-home-away-dropdown", "value"),
    ],
    [Input("game-flow-game-dropdown", "value"),],
    [State("game-flow-team-dropdown", "value"),],
)
def game_flow_home_away_dropdown(game, team):
    """Update the home/away team options based on the selected game for the game flow graph."""
    # Get game info
    game_info = audl.Season().get_game_info()
    selected_game_info = game_info.loc[game_info["url"] == game].iloc[0]
    home_team = selected_game_info["home_team"]
    away_team = selected_game_info["away_team"]

    home_away_options = [
        {"label": home_team, "value": 1},
        {"label": away_team, "value": 0},
    ]

    if team == "any":
        home_away = 1
    elif team == home_team:
        home_away = 1
    elif team == away_team:
        home_away = 0
    else:
        home_away = 1

    return home_away_options, home_away

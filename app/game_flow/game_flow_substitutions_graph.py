import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app, dir_path


@app.callback(
    Output("game-flow-substitutions-graph", "figure"),
    [
        Input("game-flow-substitutions-color-dropdown", "value"),
        Input("game-flow-game-dropdown", "value"),
        Input("game-flow-home-away-dropdown", "value"),
    ],
)
def game_flow_substitutions_graph(color, game_url, home_away):
    """Update the game flow substitutions graph."""
    g = audl.Game(game_url)
    fig = g.visual_game_flow(color=color, home=bool(home_away), qc=False)

    return fig

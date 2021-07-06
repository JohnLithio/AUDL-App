import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app, dir_path


@app.callback(
    Output("possession-map-graph", "figure"),
    [
        Input("game-flow-game-dropdown", "value"),
        Input("game-flow-home-away-dropdown", "value"),
    ],
)
def possession_map_graph(game_url, home_away):
    """Update the possession map graph."""
    g = audl.Game(game_url)
    fig = g.visual_possession_map(possession_number=1, home=bool(home_away))

    return fig

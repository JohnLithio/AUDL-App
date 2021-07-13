import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app, dir_path


@app.callback(
    Output("game-flow-score-graph", "figure"),
    [Input("game-flow-game-dropdown", "value"),],
)
def game_flow_score_graph(game_url):
    """Update the game flow score graph."""
    g = audl.Game(game_url)
    fig = g.visual_game_score(qc=False)

    return fig

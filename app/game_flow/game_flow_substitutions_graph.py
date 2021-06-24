import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app, dir_path


@app.callback(
    Output("game-flow-substitutions-graph", "figure"),
    [Input("game-flow-substitutions-color-dropdown", "value"),],
)
def game_flow_substitutions_graph(color):
    """Update the game flow substitutions graph."""
    s = audl.Season()
    g = audl.Game(s.get_game_urls()[0])
    fig = g.visual_game_flow(color=color, home=True, qc=False)

    return fig

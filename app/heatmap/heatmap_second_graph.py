import audl_advanced_stats as audl
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    Output("heatmap-second-graph", "figure"),
    [Input("heatmap-opoint-dropdown", "value"),],
)
def heatmap_second_graph(o_point):
    """Update the second heatmap graph."""
    s = audl.Season()

    if o_point == "all":
        o_point = None

    fighm, fighx, fighy = s.visual_field_heatmap_vertical(
        outcome_measure="throw_outcome",
        outcome="Completion",
        metric="pct",
        o_point=o_point,
        throw=True,
        #     team_ids=[14]
        # Square where the throw came from if throw=False
        # Square where the throw went if throw=True
        # x_cut=0,
        #     y_cut=[10, 11],
    )

    return s.visual_field_heatmap_subplots_vertical(
        fighm=fighm, fighx=fighy, fighy=fighx
    )

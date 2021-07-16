import audl_advanced_stats as audl
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    Output("heatmap-metric-dropdown", "options"),
    [Input("heatmap-outcome-dropdown", "value"),],
)
def heatmap_metric_options(outcome):
    """Update the metric options based on the outcome chosen."""

    return [
        {"label": f"Num. of {outcome}s", "value": "count"},
        {"label": f"{outcome} Pct", "value": "pct"},
        {"label": "Yards", "value": "yards_raw"},
        {"label": "Downfield Yards", "value": "yyards_raw"},
        {"label": "Sideways Yards", "value": "xyards"},
    ]

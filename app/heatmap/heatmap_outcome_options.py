import audl_advanced_stats as audl
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    [
        Output("heatmap-outcome-dropdown", "options"),
        Output("heatmap-outcome-dropdown", "value"),
    ],
    [Input("heatmap-outcome-measure-dropdown", "value"),],
    [State("heatmap-outcome-dropdown", "value"),],
)
def heatmap_outcome_options(outcome_measure, outcome):
    """Update the metric options based on the outcome chosen."""
    if outcome_measure == "possession_outcome_general":
        options = [
            {"label": "Score", "value": "Score"},
            {"label": "Turnover", "value": "Turnover"},
        ]
    else:
        options = [
            {"label": "Completion", "value": "Completion"},
            {"label": "Turnover", "value": "Turnover"},
        ]
    if outcome != "Turnover":
        outcome = options[0]["value"]

    return (options, outcome)

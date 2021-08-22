import audl_advanced_stats as audl
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    Output("heatmap-z-slider", "disabled"),
    [Input("heatmap-z-switch", "value"), Input("heatmap-metric-dropdown", "value"),],
)
def heatmap_z_slider_enable(switch, metric):
    """Enable or disable the slider based on switch."""
    if (switch == ["auto"]) or (metric != "pct"):
        return True
    else:
        return None

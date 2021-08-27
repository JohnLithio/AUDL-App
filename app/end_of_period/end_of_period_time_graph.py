import audl_advanced_stats as audl
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    Output("end-of-period-time-graph", "figure"),
    [
        Input("end-of-period-team-dropdown", "value"),
        Input("end-of-period-team-radio", "value"),
        Input("end-of-period-period-dropdown", "value"),
    ],
)
def end_of_period_time_graph(
    teams, team_radio, periods,
):
    """Update the end of period time graph."""
    s = audl.Season()

    if teams == []:
        teams = None
    if team_radio == "offense":
        team_ids = {"team_ids": teams}
    elif team_radio == "defense":
        team_ids = {"opposing_team_ids": teams}
    if periods == []:
        periods = [1, 2, 3]

    fig = s.visual_end_of_period(periods=periods, **team_ids,)

    return fig

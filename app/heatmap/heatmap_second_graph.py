import audl_advanced_stats as audl
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    Output("heatmap-second-graph", "figure"),
    [
        Input("heatmap-opoint-dropdown", "value"),
        Input("heatmap-outcome-measure-dropdown", "value"),
        Input("heatmap-outcome-dropdown", "value"),
        Input("heatmap-metric-dropdown", "value"),
        Input("heatmap-throw-dropdown", "value"),
        Input("heatmap-team-radio", "value"),
        Input("heatmap-team-dropdown", "value"),
        Input("heatmap-player-dropdown", "value"),
        Input("heatmap-yards-slider", "value"),
        Input("heatmap-xyards-slider", "value"),
        Input("heatmap-yyards-slider", "value"),
        Input("heatmap-z-slider", "disabled"),
        Input("heatmap-z-slider", "value"),
        Input("heatmap-first-graph", "clickData"),
    ],
)
def heatmap_second_graph(
    o_point,
    outcome_measure,
    outcome,
    metric,
    throw,
    team_radio,
    teams,
    players,
    yards,
    xyards,
    yyards,
    slider_disabled,
    zminmax,
    clickData1,
):
    """Update the second heatmap graph."""
    if clickData1 is None:
        x_cut = 2
        y_cut = 3
    else:
        x_cut = clickData1["points"][0]["x"]
        y_cut = clickData1["points"][0]["y"]

    s = audl.Season()

    if o_point == "all":
        o_point = None
    if teams == []:
        teams = None
    if players == []:
        players = None
    if team_radio == "offense":
        team_ids = {"team_ids": teams}
    elif team_radio == "defense":
        team_ids = {"opposing_team_ids": teams}
    if slider_disabled is None:
        zmin = zminmax[0]
        zmax = zminmax[1]
    elif slider_disabled:
        zmin = None
        zmax = None

    fighm, fighx, fighy = s.visual_field_heatmap_vertical(
        outcome_measure=outcome_measure,
        outcome=outcome,
        metric=metric,
        o_point=o_point,
        throw=not throw,
        player_ids=players,
        yards_min=yards[0],
        yards_max=yards[1],
        xyards_min=xyards[0],
        xyards_max=xyards[1],
        yyards_min=yyards[0],
        yyards_max=yyards[1],
        zmin=zmin,
        zmax=zmax,
        # Square where the throw came from if throw=False
        # Square where the throw went if throw=True
        x_cut=x_cut,
        y_cut=y_cut,
        second_graph=True,
        **team_ids,
    )

    fig = s.visual_field_heatmap_subplots_vertical(
        fighm=fighm, fighx=fighy, fighy=fighx
    )

    # Draw square where click occurred
    # Assumes a 5x12 grid
    y0 = audl.HEATMAP_RATIO_V_Y * y_cut / 12
    y1 = audl.HEATMAP_RATIO_V_Y * (y_cut + 1) / 12
    x0 = audl.HEATMAP_RATIO_V_X * x_cut / 5
    x1 = audl.HEATMAP_RATIO_V_X * (x_cut + 1) / 5

    fig.add_shape(
        xref="paper",
        yref="paper",
        type="rect",
        y0=y0,
        y1=y1,
        x0=x0,
        x1=x1,
        line=dict(color="black", width=0),
        fillcolor="gray",
        opacity=0.5,
    )

    return fig

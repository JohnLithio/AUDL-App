import audl_advanced_stats as audl
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    [Output("heatmap-first-graph", "figure"), Output("heatmap-click-store", "data")],
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
        Input("heatmap-second-graph", "clickData"),
    ],
    [State("heatmap-click-store", "data"),],
)
def heatmap_first_graph(
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
    clickData2,
    clickstore,
):
    """Update the first heatmap graph."""
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
    elif slider_disabled[0]:
        zmin = None
        zmax = None

    fighm, fighx, fighy = s.visual_field_heatmap_vertical(
        outcome_measure=outcome_measure,
        outcome=outcome,
        metric=metric,
        o_point=o_point,
        throw=throw,
        player_ids=players,
        yards_min=yards[0],
        yards_max=yards[1],
        xyards_min=xyards[0],
        xyards_max=xyards[1],
        yyards_min=yyards[0],
        yyards_max=yyards[1],
        zmin=zmin,
        zmax=zmax,
        **team_ids,
    )

    fig = s.visual_field_heatmap_subplots_vertical(
        fighm=fighm, fighx=fighy, fighy=fighx
    )

    if clickData1 is None:
        x_cut = None
        y_cut = None
    else:
        x_cut = clickData1["points"][0]["x"]
        y_cut = clickData1["points"][0]["y"]
    if clickData2 is None:
        x_cut_remove = None
        y_cut_remove = None
    else:
        x_cut_remove = clickData2["points"][0]["x"]
        y_cut_remove = clickData2["points"][0]["y"]

    # Remove square if it was clicked
    # When this condition is "or", square removed on any click
    if (
        (x_cut_remove == clickstore["x_cut"]) and (y_cut_remove == clickstore["y_cut"])
    ) or ((x_cut == clickstore["x_old"]) and (y_cut == clickstore["y_old"])):
        return fig, {"x_cut": -1, "y_cut": -1, "x_old": x_cut, "y_old": y_cut}
    elif x_cut is not None:
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
        clickstore = {"x_cut": x_cut, "y_cut": y_cut, "x_old": x_cut, "y_old": y_cut}

    return fig, clickstore

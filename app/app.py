"""This is the structure for a Dash app to explore AUDL stats.

Author: John Lithio
"""

import base64
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash_table import DataTable
from os.path import join
from .server import app
from .constants import *
from .game_flow import *
from .heatmap import *
from .stats import *

app.title = APP_NAME
image_filename = join(__file__, r"../info-button.png")
encoded_image = base64.b64encode(open(image_filename, "rb").read())

### GAME FLOW
## GAME FLOW TOOLTIPS
elem_game_tooltip = dbc.Tooltip(
    GAME_TOOLTIP,
    innerClassName="tooltip-custom",
    target="game-flow-game-label",
    placement="top-start",
    hide_arrow=True,
)

elem_home_away_tooltip = dbc.Tooltip(
    HOME_AWAY_TOOLTIP,
    innerClassName="tooltip-custom",
    target="game-flow-home-away-label",
    placement="top-start",
    hide_arrow=True,
)

elem_substitutions_color_tooltip = dbc.Tooltip(
    SUBSTITUTIONS_COLOR_TOOLTIP,
    innerClassName="tooltip-custom",
    target="game-flow-substitutions-color-label",
    placement="top-start",
    hide_arrow=True,
)

elem_possession_number_tooltip = dbc.Tooltip(
    POSSESSION_NUMBER_TOOLTIP,
    innerClassName="tooltip-custom",
    target="possession-map-number-label",
    placement="top-start",
    hide_arrow=True,
)


## GAME FLOW ELEMENTS
# Game selection
elem_game_dropdown = dbc.Col(
    [
        html.Label("Game", id="game-flow-game-label"),
        dcc.Dropdown(
            id="game-flow-game-dropdown",
            options=GAME_OPTIONS,
            value=GAME_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    className="col-sm-12 col-md-12 col-lg-4 col-xl-4 col-12",
)

# Home/Away selection
elem_home_away_dropdown = dbc.Col(
    [
        html.Label("Team", id="game-flow-home-away-label"),
        dcc.Dropdown(
            id="game-flow-home-away-dropdown",
            options=HOME_AWAY_OPTIONS,
            value=HOME_AWAY_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    className="col-sm-12 col-md-6 col-lg-4 col-xl-4 col-12",
)

# Game flow substitutions graph color selection
elem_game_flow_substitutions_color_dropdown = dbc.Col(
    [
        html.Label("Color", id="game-flow-substitutions-color-label"),
        dcc.Dropdown(
            id="game-flow-substitutions-color-dropdown",
            options=GAME_FLOW_COLOR_OPTIONS,
            value=GAME_FLOW_COLOR_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    className="col-sm-12 col-md-6 col-lg-4 col-xl-4 col-12",
)

# Possession number selection for possession map
elem_possession_number_dropdown = dbc.Col(
    [
        html.Label("Possessions", id="possession-map-number-label"),
        dcc.Dropdown(
            id="possession-map-number-dropdown",
            options=POSSESSION_NUMBER_OPTIONS,
            value=POSSESSION_NUMBER_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Data store to remember which spot of heatmap was clicked previously
elem_heatmap_click_store = dbc.Col(
    dcc.Store(
        id="heatmap-click-store",
        data={"x_cut": -1, "y_cut": -1, "x_old": -1, "y_old": -1},
        storage_type="session",
    )
)

# Data store to indicate if 2nd heatmap is filtered
elem_heatmap_filtered_store = dbc.Col(
    dcc.Store(
        id="heatmap-filtered-store", data={"filtered": False,}, storage_type="session",
    )
)

# Game flow score graph
elem_game_flow_score_graph = dbc.Col(
    [
        dcc.Graph(
            id="game-flow-score-graph",
            config={
                "toImageButtonOptions": {"format": "png", "filename": "audl_subs",},
                "displaylogo": False,
                "displayModeBar": False,
            },
        ),
    ],
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
    align="center",
)

# Game flow substitution graph
elem_game_flow_substitutions_graph = dbc.Col(
    [
        dcc.Graph(
            id="game-flow-substitutions-graph",
            config={
                "toImageButtonOptions": {"format": "png", "filename": "audl_subs",},
                "displaylogo": False,
                "displayModeBar": False,
            },
        ),
    ],
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
    align="center",
)

# Possession map graph
elem_possession_map_graph = dbc.Col(
    [
        dcc.Graph(
            id="possession-map-graph",
            config={
                "toImageButtonOptions": {
                    "format": "png",
                    "filename": "possession_map",
                },
                "displaylogo": False,
                "displayModeBar": False,
            },
        ),
    ],
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

### HEATMAP
## HEATMAP TOOLTIPS
elem_heatmap_outcome_measure_tooltip = dbc.Tooltip(
    OUTCOME_MEASURE_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-outcome-measure-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_outcome_tooltip = dbc.Tooltip(
    OUTCOME_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-outcome-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_metric_tooltip = dbc.Tooltip(
    METRIC_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-metric-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_throw_tooltip = dbc.Tooltip(
    THROW_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-throw-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_opoint_tooltip = dbc.Tooltip(
    OPOINT_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-opoint-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_team_tooltip = dbc.Tooltip(
    TEAM_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-team-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_player_tooltip = dbc.Tooltip(
    PLAYER_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-player-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_yards_tooltip = dbc.Tooltip(
    YARDS_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-yards-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_yyards_tooltip = dbc.Tooltip(
    YYARDS_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-yyards-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_xyards_tooltip = dbc.Tooltip(
    XYARDS_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-xyards-label",
    placement="top-start",
    hide_arrow=True,
)

elem_heatmap_z_tooltip = dbc.Tooltip(
    Z_TOOLTIP,
    innerClassName="tooltip-custom",
    target="heatmap-z-switch",
    placement="top-start",
    hide_arrow=True,
)

## HEATMAP ELEMENTS
# Outcome measure dropdown selection for heatmap
elem_heatmap_outcome_measure_dropdown = dbc.Col(
    [
        html.Label("Outcome Type", id="heatmap-outcome-measure-label"),
        dcc.Dropdown(
            id="heatmap-outcome-measure-dropdown",
            options=HEATMAP_OUTCOME_MEASURE_OPTIONS,
            value=HEATMAP_OUTCOME_MEASURE_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-4 col-xl-4 col-12",
)

# Outcome dropdown selection for heatmap
elem_heatmap_outcome_dropdown = dbc.Col(
    [
        html.Label("Outcome", id="heatmap-outcome-label"),
        dcc.Dropdown(
            id="heatmap-outcome-dropdown",
            options=HEATMAP_OUTCOME_OPTIONS,
            value=HEATMAP_OUTCOME_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-4 col-xl-4 col-12",
)

# Metric dropdown selection for heatmap
elem_heatmap_metric_dropdown = dbc.Col(
    [
        html.Label("Metric", id="heatmap-metric-label"),
        dcc.Dropdown(
            id="heatmap-metric-dropdown",
            options=HEATMAP_METRIC_OPTIONS,
            value=HEATMAP_METRIC_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-4 col-xl-4 col-12",
)

# Throw/Receive dropdown selection for heatmap
elem_heatmap_throw_dropdown = dbc.Col(
    [
        html.Label("Location", id="heatmap-throw-label"),
        dcc.Dropdown(
            id="heatmap-throw-dropdown",
            options=HEATMAP_THROW_OPTIONS,
            value=HEATMAP_THROW_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-5 col-xl-5 col-12",
)

# O-point dropdown selection for heatmap
elem_heatmap_opoint_dropdown = dbc.Col(
    [
        html.Label("Receiving Team", id="heatmap-opoint-label"),
        dcc.Dropdown(
            id="heatmap-opoint-dropdown",
            options=HEATMAP_OPOINT_OPTIONS,
            value=HEATMAP_OPOINT_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-6 col-xl-6 col-12",
)

# Empty column for padding
elem_empty = dbc.Col(className="col-xl-4 col-0",)

# Team dropdown selection for heatmap
elem_heatmap_team_dropdown = dbc.Col(
    [
        html.Label("Teams", id="heatmap-team-label"),
        dcc.Dropdown(
            id="heatmap-team-dropdown",
            options=HEATMAP_TEAM_OPTIONS,
            value=[],
            multi=True,
            clearable=True,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-8 col-xl-8 col-12",
)

# Selection for offense or defensive team
elem_heatmap_team_radio = dbc.Col(
    [
        dbc.RadioItems(
            id="heatmap-team-radio",
            options=[
                {"label": "Offense", "value": "offense"},
                {"label": "Defense", "value": "defense"},
            ],
            value="offense",
            inline=True,
        ),
    ],
    style={"margin": "20px 0px 0px 0px", "padding": "20px 20px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-4 col-xl-4 col-12",
)

# Player dropdown selection for heatmap
elem_heatmap_player_dropdown = dbc.Col(
    [
        html.Label("Players", id="heatmap-player-label"),
        dcc.Dropdown(
            id="heatmap-player-dropdown",
            options=HEATMAP_PLAYER_OPTIONS,
            value=[],
            multi=True,
            clearable=True,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Min and max yards label
elem_heatmap_yards_slider_label = dbc.Col(
    html.Label("Total Yards", id="heatmap-yards-label"),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-4 col-12",
)

# Min and max yards
elem_heatmap_yards_slider = dbc.Col(
    dcc.RangeSlider(
        id="heatmap-yards-slider",
        min=0,
        max=130,
        step=None,
        marks={int(x): str(x) for x in np.arange(0, 140, 10)},
        value=[0, 130],
    ),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-8 col-12",
)

# Min and max y yards label
elem_heatmap_yyards_slider_label = dbc.Col(
    html.Label("Downfield Yards", id="heatmap-yyards-label"),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-4 col-12",
)

# Min and max y yards
elem_heatmap_yyards_slider = dbc.Col(
    dcc.RangeSlider(
        id="heatmap-yyards-slider",
        min=-120,
        max=120,
        step=None,
        marks=HEATMAP_YYARDS_MARKS,
        value=[-120, 120],
    ),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-8 col-12",
)

# Min and max x yards label
elem_heatmap_xyards_slider_label = dbc.Col(
    html.Label("Sideways Yards", id="heatmap-xyards-label"),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-4 col-12",
)

# Min and max x yards
elem_heatmap_xyards_slider = dbc.Col(
    dcc.RangeSlider(
        id="heatmap-xyards-slider",
        min=-30,
        max=30,
        step=None,
        marks={int(x): str(x) for x in np.arange(-30, 40, 10)},
        value=[-30, 30],
    ),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-8 col-12",
)

# Switch to enable/disable manual color slider
elem_heatmap_z_switch = dbc.Col(
    dbc.Checklist(
        id="heatmap-z-switch",
        options=[{"label": "Auto Color Scale", "value": "auto"}],
        value=["auto"],
        switch=True,
    ),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-4 col-12",
)

# Min and max % for color slider
elem_heatmap_z_slider = dbc.Col(
    dcc.RangeSlider(
        id="heatmap-z-slider",
        min=0,
        max=1,
        step=None,
        marks=HEATMAP_Z_MARKS,
        value=[0, 1],
    ),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-12 col-lg-12 col-xl-8 col-12",
)

# Heatmap description
elem_heatmap_description = dbc.Col(
    html.P(id="heatmap-description", children="Test text",),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# First heatmap graph
elem_heatmap_first_graph = dbc.Col(
    [
        dcc.Graph(
            id="heatmap-first-graph",
            config={"displaylogo": False, "displayModeBar": False,},
            style={"aspect-ratio": "1 / 2", "max-height": "750px", "margin": "0 auto"},
        ),
    ],
    className="col-sm-12 col-md-6 col-lg-6 col-xl-6 col-12",
)

# Second heatmap graph
elem_heatmap_second_graph = dbc.Col(
    [
        dcc.Graph(
            id="heatmap-second-graph",
            config={"displaylogo": False, "displayModeBar": False,},
            style={"aspect-ratio": "1 / 2", "max-height": "750px", "margin": "0 auto"},
        ),
    ],
    className="col-sm-12 col-md-6 col-lg-6 col-xl-6 col-12",
)

### PLAYER STATS BY GAME
# TODO: Clear filter queries when changing table view
# Player dropdown selection for heatmap
player_stats_by_game_dropdown = dbc.Col(
    [
        dcc.Dropdown(
            id="player-stats-by-game-dropdown",
            options=PLAYER_STATS_BY_GAME_OPTIONS,
            value=PLAYER_STATS_BY_GAME_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-4 col-lg-3 col-xl-3 col-12",
)

throw_types_tooltip = dbc.Tooltip(
    THROW_TYPES_TOOLTIP,
    innerClassName="tooltip-custom",
    target="throw-types-info",
    placement="top-start",
    hide_arrow=True,
)

# Throw type info
throw_types_info = dbc.Col(
    html.P(
        "Throw Types?",
        id="throw-types-info",
        style={"float": "right", "text-align": "right"},
    ),
    style={"margin": "20px 0px 0px 0px",},
    className="col-sm-12 col-md-2 col-lg-1 col-xl-1 col-12",
)

player_stats_by_game_info_tooltip = dbc.Tooltip(
    PLAYER_STATS_BY_GAME_INFO_TOOLTIP,
    innerClassName="tooltip-custom",
    target="player-stats-by-game-info",
    placement="top-start",
    hide_arrow=True,
)

# Info icon
player_stats_by_game_info = dbc.Col(
    dbc.Row(
        [
            html.P(
                "Throw Types?",
                id="throw-types-info",
                style={"float": "right", "text-align": "right"},
            ),
            html.Img(
                id="player-stats-by-game-info",
                src="data:image/png;base64,{}".format(encoded_image.decode()),
                style={"width": "25px", "height": "25px", "float": "right"},
            ),
        ]
    ),
    style={"margin": "20px 0px 0px 0px",},
    className="col-sm-12 col-md-2 col-lg-1 col-xl-1 col-12",
)

# Empty column for padding
player_stats_by_game_empty = dbc.Col(
    className="col-sm-0 col-md-6 col-lg-8 col-xl-8 col-0",
)

# Player stats by game table
player_stats_by_game_table = dbc.Col(
    [
        DataTable(
            id="player-stats-by-game-table",
            merge_duplicate_headers=True,
            sort_action="native",
            filter_action="native",
            sort_as_null=["N/A"],
            style_cell_conditional=[
                {"if": {"column_id": "name"}, "textAlign": "left",},
                {"if": {"column_id": "team"}, "textAlign": "left",},
                {"if": {"column_id": "opponent"}, "textAlign": "left",},
                {"if": {"column_id": "game_date"}, "textAlign": "left",},
            ],
            style_cell={
                "background-color": "rgb(255, 255, 255)",
                "color": "rgb(0, 51, 102)",
                "font-family": "TW Cen MT",
                "border": "0px",
                "textAlign": "right",
            },
            style_header={
                "textAlign": "center",
                "background-color": "rgb(0, 51, 102)",
                "color": "rgb(235, 235, 235)",
                "border": "0px",
                "whiteSpace": "normal",
                "height": "auto",
            },
            style_filter={
                "background-color": "rgb(220, 220, 220)",
                "border-width": "0px",
                "border-color": "rgb(0, 51, 102)",
            },
            style_data_conditional=[
                {
                    "if": {"state": "selected"},  # 'active' | 'selected'
                    "backgroundColor": "rgba(230, 157, 0, 0.5)",
                    "border": "0px",
                }
            ],
            tooltip_header=PLAYER_STATS_HEADER_TOOLTIPS,
            tooltip_duration=None,
            page_size=25,
        )
    ],
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

### PLAYER STATS BY SEASON
# Player dropdown selection for heatmap
player_stats_by_season_dropdown = dbc.Col(
    [
        dcc.Dropdown(
            id="player-stats-by-season-dropdown",
            options=PLAYER_STATS_BY_SEASON_OPTIONS,
            value=PLAYER_STATS_BY_SEASON_OPTIONS[0]["value"],
            multi=False,
            clearable=False,
            optionHeight=OPTION_HEIGHT,
        ),
    ],
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-4 col-lg-3 col-xl-3 col-12",
)

throw_types_tooltip2 = dbc.Tooltip(
    THROW_TYPES_TOOLTIP,
    innerClassName="tooltip-custom",
    target="throw-types-info2",
    placement="top-start",
    hide_arrow=True,
)

# Throw type info
throw_types_info2 = dbc.Col(
    html.P(
        "Throw Types?",
        id="throw-types-info2",
        style={"float": "right", "text-align": "right"},
    ),
    style={"margin": "20px 0px 0px 0px",},
    className="col-sm-12 col-md-2 col-lg-1 col-xl-1 col-12",
)

player_stats_by_season_info_tooltip = dbc.Tooltip(
    PLAYER_STATS_BY_SEASON_INFO_TOOLTIP,
    innerClassName="tooltip-custom",
    target="player-stats-by-season-info",
    placement="top-start",
    hide_arrow=True,
)

# Info icon
player_stats_by_season_info = dbc.Col(
    dbc.Row(
        [
            html.P(
                "Throw Types?",
                id="throw-types-info2",
                style={"float": "right", "text-align": "right"},
            ),
            html.Img(
                id="player-stats-by-season-info",
                src="data:image/png;base64,{}".format(encoded_image.decode()),
                style={"width": "25px", "height": "25px", "float": "right"},
            ),
        ]
    ),
    style={"margin": "20px 0px 0px 0px",},
    className="col-sm-12 col-md-2 col-lg-1 col-xl-1 col-12",
)

# Empty column for padding
player_stats_by_season_empty = dbc.Col(
    className="col-sm-0 col-md-2 col-lg-5 col-xl-5 col-0",
)

# Switch to enable per-game totals instead of season totals
player_stats_by_season_per_game_switch = dbc.Col(
    dbc.Checklist(
        id="player-stats-by-season-per-game-switch",
        options=[{"label": "Per-Game", "value": "per_game"}],
        value=["per_game"],
        switch=True,
    ),
    style={"margin": "20px 0px 0px 0px"},
    className="col-sm-12 col-md-4 col-lg-3 col-xl-3 col-12",
)

# Player stats by season table
player_stats_by_season_table = dbc.Col(
    [
        DataTable(
            id="player-stats-by-season-table",
            merge_duplicate_headers=True,
            sort_action="native",
            filter_action="native",
            sort_as_null=["N/A"],
            style_cell_conditional=[
                {"if": {"column_id": "name"}, "textAlign": "left",},
                {"if": {"column_id": "team"}, "textAlign": "left",},
            ],
            style_cell={
                "background-color": "rgb(255, 255, 255)",
                "color": "rgb(0, 51, 102)",
                "font-family": "TW Cen MT",
                "border": "0px",
                "textAlign": "right",
            },
            style_header={
                "textAlign": "center",
                "background-color": "rgb(0, 51, 102)",
                "color": "rgb(235, 235, 235)",
                "border": "0px",
                "whiteSpace": "normal",
                "height": "auto",
            },
            style_filter={
                "background-color": "rgb(220, 220, 220)",
                "border-width": "0px",
                "border-color": "rgb(0, 51, 102)",
            },
            style_data_conditional=[
                {
                    "if": {"state": "selected"},  # 'active' | 'selected'
                    "backgroundColor": "rgba(230, 157, 0, 0.5)",
                    "border": "0px",
                }
            ],
            tooltip_header=PLAYER_STATS_HEADER_TOOLTIPS,
            tooltip_duration=None,
            page_size=25,
        )
    ],
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

## APP STRUCTURE
app.layout = dbc.Container(
    [
        dbc.Tabs(
            children=[
                dbc.Tab(
                    label="Game Flow",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                elem_game_dropdown,
                                                elem_home_away_dropdown,
                                                elem_game_flow_substitutions_color_dropdown,
                                                # Tooltips
                                                elem_game_tooltip,
                                                elem_home_away_tooltip,
                                                elem_substitutions_color_tooltip,
                                            ],
                                            justify="center",
                                            align="center",
                                            style={"padding": "20px 0px 20px 0px"},
                                        ),
                                        dbc.Row(
                                            [elem_game_flow_score_graph,],
                                            justify="center",
                                            align="center",
                                            style={
                                                "margin-bottom": 0,
                                                "padding-bottom": 0,
                                            },
                                        ),
                                        dbc.Row(
                                            [elem_game_flow_substitutions_graph,],
                                            justify="center",
                                            align="center",
                                            style={"margin-top": 0, "padding-top": 0},
                                        ),
                                    ],
                                    className="col-sm-12 col-md-12 col-lg-8 col-xl-8 col-12",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Row(
                                            [
                                                elem_possession_number_dropdown,
                                                elem_possession_number_tooltip,
                                            ],
                                            align="center",
                                            justify="center",
                                            style={"padding": "20px 0px 20px 0px"},
                                        ),
                                        dbc.Row(
                                            [elem_possession_map_graph,],
                                            justify="center",
                                            align="center",
                                        ),
                                    ],
                                    className="col-sm-12 col-md-12 col-lg-4 col-xl-4 col-12",
                                ),
                            ]
                        ),
                    ],
                ),
                dbc.Tab(
                    label="Heat Maps",
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Row(
                                        [
                                            # Visible elements
                                            elem_heatmap_outcome_measure_dropdown,
                                            elem_heatmap_outcome_dropdown,
                                            elem_heatmap_metric_dropdown,
                                            elem_heatmap_throw_dropdown,
                                            elem_heatmap_opoint_dropdown,
                                            elem_heatmap_team_dropdown,
                                            elem_heatmap_team_radio,
                                            elem_heatmap_player_dropdown,
                                            elem_heatmap_yards_slider_label,
                                            elem_heatmap_yards_slider,
                                            elem_heatmap_xyards_slider_label,
                                            elem_heatmap_xyards_slider,
                                            elem_heatmap_yyards_slider_label,
                                            elem_heatmap_yyards_slider,
                                            elem_heatmap_z_switch,
                                            elem_heatmap_z_slider,
                                            # Data Stores
                                            elem_heatmap_click_store,
                                            elem_heatmap_filtered_store,
                                            # Tooltips
                                            elem_heatmap_outcome_measure_tooltip,
                                            elem_heatmap_outcome_tooltip,
                                            elem_heatmap_metric_tooltip,
                                            elem_heatmap_throw_tooltip,
                                            elem_heatmap_opoint_tooltip,
                                            elem_heatmap_team_tooltip,
                                            elem_heatmap_player_tooltip,
                                            elem_heatmap_yards_tooltip,
                                            elem_heatmap_yyards_tooltip,
                                            elem_heatmap_xyards_tooltip,
                                            elem_heatmap_z_tooltip,
                                        ],
                                        align="center",
                                    ),
                                    className="col-sm-12 col-md-12 col-lg-4 col-xl-4 col-12",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Row([elem_heatmap_description]),
                                        dbc.Row(
                                            [
                                                elem_heatmap_first_graph,
                                                elem_heatmap_second_graph,
                                            ],
                                        ),
                                    ],
                                    className="col-sm-12 col-md-12 col-lg-8 col-xl-8 col-12",
                                ),
                            ],
                            style={
                                "padding": "0px 0px 0px 0px",
                                "margin": "0px 0px 0px 0px",
                            },
                            align="start",
                        ),
                    ],
                ),
                dbc.Tab(
                    label="Player Game Stats",
                    children=[
                        dbc.Row(
                            children=[
                                player_stats_by_game_dropdown,
                                player_stats_by_game_empty,
                                player_stats_by_game_info,
                                player_stats_by_game_table,
                                # Tooltips
                                throw_types_tooltip,
                                player_stats_by_game_info_tooltip,
                            ]
                        ),
                    ],
                ),
                dbc.Tab(
                    label="Player Season Stats",
                    children=[
                        dbc.Row(
                            children=[
                                player_stats_by_season_dropdown,
                                player_stats_by_season_per_game_switch,
                                player_stats_by_season_empty,
                                player_stats_by_season_info,
                                player_stats_by_season_table,
                                # Tooltips
                                throw_types_tooltip2,
                                player_stats_by_season_info_tooltip,
                            ]
                        ),
                    ],
                ),
            ]
        )
    ],
    fluid=True,
)

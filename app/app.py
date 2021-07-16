"""This is the structure for a Dash app to explore AUDL stats.

Author: John Lithio
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash_table import DataTable
from .server import app
from .constants import *
from .game_flow import *
from .heatmap import *

app.title = APP_NAME

## ELEMENTS
# Game flow substitutions graph color selection
elem_game_flow_substitutions_color_dropdown = dbc.Col(
    dcc.Dropdown(
        id="game-flow-substitutions-color-dropdown",
        options=GAME_FLOW_COLOR_OPTIONS,
        value=GAME_FLOW_COLOR_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    )
)

# Game selection
elem_game_dropdown = dbc.Col(
    dcc.Dropdown(
        id="game-flow-game-dropdown",
        options=GAME_OPTIONS,
        value=GAME_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    )
)

# Home/Away selection
elem_home_away_dropdown = dbc.Col(
    dcc.Dropdown(
        id="game-flow-home-away-dropdown",
        options=HOME_AWAY_OPTIONS,
        value=HOME_AWAY_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    )
)

# Possession number selection for possession map
elem_possession_number_dropdown = dbc.Col(
    dcc.Dropdown(
        id="possession-map-number-dropdown",
        options=POSSESSION_NUMBER_OPTIONS,
        value=POSSESSION_NUMBER_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    ),
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

# O-point dropdown selection for heatmap
elem_heatmap_opoint_dropdown = dbc.Col(
    dcc.Dropdown(
        id="heatmap-opoint-dropdown",
        options=HEATMAP_OPOINT_OPTIONS,
        value=HEATMAP_OPOINT_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Outcome measure dropdown selection for heatmap
elem_heatmap_outcome_measure_dropdown = dbc.Col(
    dcc.Dropdown(
        id="heatmap-outcome-measure-dropdown",
        options=HEATMAP_OUTCOME_MEASURE_OPTIONS,
        value=HEATMAP_OUTCOME_MEASURE_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    ),
    className="col-sm-12 col-md-12 col-lg-412 col-xl-12 col-12",
)

# Outcome dropdown selection for heatmap
elem_heatmap_outcome_dropdown = dbc.Col(
    dcc.Dropdown(
        id="heatmap-outcome-dropdown",
        options=HEATMAP_OUTCOME_OPTIONS,
        value=HEATMAP_OUTCOME_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    ),
    className="col-sm-12 col-md-12 col-lg-412 col-xl-12 col-12",
)

# Metric dropdown selection for heatmap
elem_heatmap_metric_dropdown = dbc.Col(
    dcc.Dropdown(
        id="heatmap-metric-dropdown",
        options=HEATMAP_METRIC_OPTIONS,
        value=HEATMAP_METRIC_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Throw/Receive dropdown selection for heatmap
elem_heatmap_throw_dropdown = dbc.Col(
    dcc.Dropdown(
        id="heatmap-throw-dropdown",
        options=HEATMAP_THROW_OPTIONS,
        value=HEATMAP_THROW_OPTIONS[0]["value"],
        multi=False,
        clearable=False,
        optionHeight=OPTION_HEIGHT,
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# TODO: Labels for inputs
# outcome_measure, outcome, metric,
# thrower, o_point
# teams, offense_defense
# players,
# Throw filters
# Scale switch, color scale
# TODO: Explanation for inputs and graphs

# Selection for offense or defensive team
elem_heatmap_team_radio = dbc.Col(
    dbc.RadioItems(
        id="heatmap-team-radio",
        options=[
            {"label": "Offense", "value": "offense"},
            {"label": "Defense", "value": "defense"},
        ],
        value="offense",
        inline=True,
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Team dropdown selection for heatmap
elem_heatmap_team_dropdown = dbc.Col(
    dcc.Dropdown(
        id="heatmap-team-dropdown",
        options=HEATMAP_TEAM_OPTIONS,
        value=[],
        multi=True,
        clearable=True,
        optionHeight=OPTION_HEIGHT,
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Player dropdown selection for heatmap
elem_heatmap_player_dropdown = dbc.Col(
    dcc.Dropdown(
        id="heatmap-player-dropdown",
        options=HEATMAP_PLAYER_OPTIONS,
        value=[],
        multi=True,
        clearable=True,
        optionHeight=OPTION_HEIGHT,
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
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
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Min and max y yards
elem_heatmap_yyards_slider = dbc.Col(
    dcc.RangeSlider(
        id="heatmap-yyards-slider",
        min=-120,
        max=120,
        step=None,
        marks={int(x): str(x) for x in np.arange(-120, 130, 10)},
        value=[-120, 120],
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Min and x max yards
elem_heatmap_xyards_slider = dbc.Col(
    dcc.RangeSlider(
        id="heatmap-xyards-slider",
        min=-30,
        max=30,
        step=None,
        marks={int(x): str(x) for x in np.arange(-30, 40, 10)},
        value=[-30, 30],
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Switch to enable/disable manual color slider
elem_heatmap_z_switch = dbc.Col(
    dbc.Checklist(
        id="heatmap-z-switch",
        options=[{"label": "Auto Color Scale", "value": "auto"}],
        value=["auto"],
        switch=True,
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Min and max % for color slider
elem_heatmap_z_slider = dbc.Col(
    dcc.RangeSlider(
        id="heatmap-z-slider",
        min=0,
        max=1,
        step=None,
        marks={float(x): f"{x:.0%}" for x in np.arange(0, 1.1, 0.1)},
        value=[0, 1],
    ),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
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

# Heatmap description
elem_heatmap_description = dbc.Col(
    html.P(id="heatmap-description", children="Test text",),
    className="col-sm-12 col-md-12 col-lg-12 col-xl-12 col-12",
)

# Heatmap graph 1 description
elem_heatmap_description_graph1 = html.P(
    id="heatmap-description-graph1", children="Test text",
)

# Heatmap graph 2 description
elem_heatmap_description_graph2 = html.P(
    id="heatmap-description-graph2", children="Test text",
)

# First heatmap graph
elem_heatmap_first_graph = dbc.Col(
    [
        dcc.Graph(
            id="heatmap-first-graph",
            config={"displaylogo": False, "displayModeBar": False,},
            style={"aspect-ratio": "1 / 2", "max-height": "750px"},
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
            style={"aspect-ratio": "1 / 2", "max-height": "750px"},
        ),
    ],
    className="col-sm-12 col-md-6 col-lg-6 col-xl-6 col-12",
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
                                            ],
                                            justify="center",
                                            align="center",
                                            style={"padding": "10px 0px 10px 0px"},
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
                                            [elem_possession_number_dropdown,],
                                            align="center",
                                            justify="center",
                                            style={"padding": "10px 0px 10px 0px"},
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
                                    [
                                        elem_heatmap_click_store,
                                        elem_heatmap_filtered_store,
                                        elem_heatmap_opoint_dropdown,
                                        elem_heatmap_outcome_measure_dropdown,
                                        elem_heatmap_outcome_dropdown,
                                        elem_heatmap_metric_dropdown,
                                        elem_heatmap_throw_dropdown,
                                        elem_heatmap_team_radio,
                                        elem_heatmap_team_dropdown,
                                        elem_heatmap_player_dropdown,
                                        elem_heatmap_yards_slider,
                                        elem_heatmap_xyards_slider,
                                        elem_heatmap_yyards_slider,
                                        elem_heatmap_z_switch,
                                        elem_heatmap_z_slider,
                                    ],
                                    className="col-sm-12 col-md-12 col-lg-4 col-xl-4 col-12",
                                ),
                                dbc.Col(
                                    [
                                        dbc.Row([elem_heatmap_description]),
                                        dbc.Row(
                                            [
                                                elem_heatmap_first_graph,
                                                elem_heatmap_second_graph,
                                            ]
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
            ]
        )
    ],
    fluid=True,
)

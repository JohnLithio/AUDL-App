"""This is the structure for a Dash app to explore AUDL stats.

Author: John Lithio
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_table import DataTable
from .server import app
from .constants import *
from .game_flow import *

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
                )
            ]
        )
    ],
    fluid=True,
)

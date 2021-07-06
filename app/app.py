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
# TODO: Filter this to not show games that are yet to happen
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

# Game flow substitution graph
elem_game_flow_substitutions_graph = dbc.Col(
    [
        dcc.Graph(
            id="game-flow-substitutions-graph",
            config={
                "toImageButtonOptions": {"format": "png", "filename": "audl_subs",},
                "displaylogo": False,
            },
        ),
    ],
    className="col-sm-12 col-md-12 col-lg-6 col-xl-6 col-12",
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
            },
        ),
    ],
    className="col-sm-12 col-md-12 col-lg-6 col-xl-6 col-12",
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
                            [elem_game_dropdown, elem_home_away_dropdown,],
                            justify="start",
                            align="start",
                        ),
                        dbc.Row(
                            elem_game_flow_substitutions_color_dropdown,
                            justify="start",
                            align="start",
                        ),
                        dbc.Row(
                            [
                                elem_game_flow_substitutions_graph,
                                elem_possession_map_graph,
                            ],
                            justify="start",
                            align="start",
                        ),
                    ],
                )
            ]
        )
    ]
)

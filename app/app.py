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
    className="col-sm-12 col-md-6 col-lg-6 col-xl-12 col-12",
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
                            elem_game_flow_substitutions_color_dropdown,
                            justify="start",
                            align="start",
                        ),
                        dbc.Row(
                            elem_game_flow_substitutions_graph,
                            justify="start",
                            align="start",
                        ),
                    ],
                )
            ]
        )
    ]
)

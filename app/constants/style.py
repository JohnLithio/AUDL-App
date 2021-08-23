"""Aesthetic settings, as well as label ordering and data types."""

import plotly.io as pio
from dash_table import FormatTemplate
from dash_table.Format import Format, Scheme
from .options import *

# App info
VERSION = "0.1.0"
APP_NAME = "AUDL Stats Explorer"

# Theme/style settings
COLORS = [
    "#56B4E9",
    "#E69F00",
    "#009E73",
    "#F0E442",
    "#CC79A7",
    "#6B6A6A",
    "#0072B2",
    "#D55E00",
]

OPTION_HEIGHT = 50
GRAPH_TITLE_FONT_SIZE = 24
AXIS_TITLE_FONT_SIZE = 20
TICK_FONT_SIZE = 16

TEMPLATE = pio.templates["plotly_white"]
TEMPLATE.layout["colorway"] = tuple(COLORS)
TEMPLATE.layout["font"] = {
    "family": "TW Cen MT",
    "color": "#003366",
}

# Datatable formatting
percentage_no_decimal = FormatTemplate.percentage(0)
number_no_decimal = Format(precision=0)


def stat_table_format(col, per_game):
    if "_pct" in col:
        return FormatTemplate.percentage(0)
    elif (
        ("_percompletion" in col)
        or ("_perreception" in col)
        or ("_perthrowaway" in col)
        or ("_perthrowattempt" in col)
        or ("_percatchattempt" in col)
        or ("_pp" in col)
        or ("_ratio_" in col)
    ) and ("yards" not in col):
        return Format(precision=2, scheme=Scheme.fixed)
    elif (
        ("_percompletion" in col)
        or ("_perreception" in col)
        or ("_perthrowaway" in col)
        or ("_perthrowattempt" in col)
        or ("_percatchattempt" in col)
        or ("_pp" in col)
        or ("_ratio_" in col)
    ) and ("yards" in col):
        return Format(precision=1, scheme=Scheme.fixed)
    elif per_game:
        return Format(precision=1, scheme=Scheme.fixed)
    else:
        return Format(precision=0, scheme=Scheme.fixed)


def stat_table_type(col):
    if (col in PLAYER_GAME_STATS_INFO_COLS) or (col in PLAYER_SEASON_STATS_INFO_COLS):
        return "text"
    else:
        return "numeric"

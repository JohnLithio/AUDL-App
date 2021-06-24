"""Aesthetic settings, as well as label ordering and data types."""

import plotly.io as pio

# App info
VERSION = "0.0.1"
APP_NAME = "AUDL Stats"

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
NUM_ROWS_ASSESSMENTS = 30

TEMPLATE = pio.templates["plotly_white"]
TEMPLATE.layout["colorway"] = tuple(COLORS)
TEMPLATE.layout["font"] = {
    "family": "TW Cen MT",
    "color": "#003366",
}

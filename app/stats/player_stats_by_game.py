import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    [
        Output("player-stats-by-game-table", "data"),
        Output("player-stats-by-game-table", "columns"),
    ],
    [
        Input("player-stats-by-game-dropdown", "value"),
        Input("player-stats-by-game-playoffs-dropdown", "value"),
    ],
)
def player_stats_by_game(stat_group, playoffs):
    """Display player stats by game."""
    if playoffs == "all":
        playoffs = [True, False]

    df = (
        audl.Season()
        .get_player_stats_by_game(keep_all_years=True)
        .query(f"playoffs=={playoffs}")[
            PLAYER_GAME_STATS_INFO_COLS + PLAYER_STATS_OPTIONS_COLUMNS[stat_group]
        ]
    )
    columns = [
        {
            "name": PLAYER_STATS_COLS_DISPLAY[i],
            "id": i,
            "format": stat_table_format(i, False),
            "type": stat_table_type(i),
        }
        for i in df.columns
    ]

    return df.to_dict("records"), columns

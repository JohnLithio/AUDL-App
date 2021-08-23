import audl_advanced_stats as audl
import pandas as pd
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


def get_per_game_averages(df):
    for col in list(df):
        if (
            ("_pct" not in col)
            and ("_percompletion" not in col)
            and ("_perreception" not in col)
            and ("_perthrowaway" not in col)
            and ("_perthrowattempt" not in col)
            and ("_percatchattempt" not in col)
            and ("_pp" not in col)
            and ("_ratio_" not in col)
            and (col not in PLAYER_SEASON_STATS_INFO_COLS)
        ):
            df[col] = df[col] / df["games"]

    return df


@app.callback(
    [
        Output("player-stats-by-season-table", "data"),
        Output("player-stats-by-season-table", "columns"),
    ],
    [
        Input("player-stats-by-season-dropdown", "value"),
        Input("player-stats-by-season-per-game-switch", "value"),
    ],
)
def player_stats_by_season(stat_group, per_game_switch):
    """Display player stats by season."""
    per_game = per_game_switch == ["per_game"]
    df_list = []
    for season in SEASONS:
        df_list.append(
            audl.Season(year=season).get_player_stats_by_season()[
                PLAYER_SEASON_STATS_INFO_COLS + PLAYER_STATS_OPTIONS_COLUMNS[stat_group]
            ]
        )
    df = pd.concat(df_list, ignore_index=True)

    if per_game:
        df = get_per_game_averages(df)

    columns = [
        {
            "name": PLAYER_STATS_COLS_DISPLAY[i],
            "id": i,
            "format": stat_table_format(i, per_game),
            "type": stat_table_type(i),
        }
        for i in df.columns
    ]

    return df.to_dict("records"), columns

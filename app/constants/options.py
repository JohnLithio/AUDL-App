import audl_advanced_stats as audl
from datetime import datetime, timedelta

# All available AUDL season with the requisite stats
SEASONS = [
    2021,
]

# # Get all seasons of games
# games_dict = dict()
# for season in SEASONS:
#     games_dict[season] = audl.Season(year=season).get_game_info(override=False)

# GAME_FLOW_COLOR_OPTIONS = [
#     {"label": "Receiving Team", "value": "o_point"},
#     {"label": "Point Outcome", "value": "point_outcome"},
#     {"label": "Point Hold", "value": "point_hold"},
#     {"label": "Total Turnovers", "value": "num_turnovers"},
# ]

# GAME_OPTIONS = [
#     {
#         "label": f"{row['away_team']} at {row['home_team']}, {row['game_date']}",
#         "value": row["url"],
#     }
#     for _, row in games_dict[SEASONS[-1]].iterrows()
#     if (datetime.strptime(row["game_date"], "%Y-%m-%d") + timedelta(days=1))
#     < datetime.now()
# ]

HOME_AWAY_OPTIONS = [
    {"label": "Home Team", "value": 1},
    {"label": "Away Team", "value": 0},
]

POSSESSION_NUMBER_OPTIONS = [
    {"label": "Possession 1", "value": 1},
]

HEATMAP_OPOINT_OPTIONS = [
    {"label": "All Points", "value": "all"},
    {"label": "O-Points", "value": True},
    {"label": "D-Points", "value": False},
]

HEATMAP_METRIC_OPTIONS = [
    {"label": "Num. of Completions", "value": "count"},
    {"label": "Completion Pct", "value": "pct"},
    {"label": "Yards", "value": "yards_raw"},
    {"label": "Downfield Yards", "value": "yyards_raw"},
    {"label": "Sideways Yards", "value": "xyards"},
]

HEATMAP_OUTCOME_MEASURE_OPTIONS = [
    {"label": "Throw Outcome", "value": "throw_outcome"},
    {"label": "Possession Outcome", "value": "possession_outcome_general"},
]

HEATMAP_OUTCOME_OPTIONS = [
    {"label": "Completion", "value": "Completion"},
    {"label": "Turnover", "value": "Turnover"},
]

HEATMAP_THROW_OPTIONS = [
    {"label": "Thrower", "value": True},
    {"label": "Receiver", "value": False},
]

# HEATMAP_TEAM_OPTIONS = [
#     {"label": row["team_name"], "value": row["team_id"]}
#     for i, row in audl.Season().get_teams().iterrows()
# ]

# HEATMAP_PLAYER_OPTIONS = [
#     {"label": row["player_name"], "value": row["player_id"]}
#     for i, row in audl.Season().get_players().iterrows()
# ]

HEATMAP_YYARDS_MARKS = {
    -120: "120",
    -110: "",
    -100: "100",
    -90: "",
    -80: "-80",
    -70: "",
    -60: "-60",
    -50: "",
    -40: "-40",
    -30: "",
    -20: "-20",
    -10: "",
    0: "0",
    10: "",
    20: "20",
    30: "",
    40: "40",
    50: "",
    60: "60",
    70: "",
    80: "80",
    90: "",
    100: "100",
    110: "",
    120: "120",
}

HEATMAP_Z_MARKS = {
    0: "0%",
    0.05: "",
    0.1: "",
    0.15: "",
    0.2: "20%",
    0.25: "",
    0.3: "",
    0.35: "",
    0.4: "40%",
    0.45: "",
    0.5: "",
    0.55: "",
    0.6: "60%",
    0.65: "",
    0.7: "",
    0.75: "",
    0.8: "80%",
    0.85: "",
    0.9: "",
    0.95: "",
    1: "100%",
}

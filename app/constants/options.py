import audl_advanced_stats as audl

# All available AUDL season with the requisite stats
SEASONS = [
    2021,
]

# Get all seasons of games
games_dict = dict()
for season in SEASONS:
    games_dict[season] = audl.Season(year=season).get_games(override=False)

GAME_FLOW_COLOR_OPTIONS = [
    {"label": "Point Outcome", "value": "point_outcome"},
    {"label": "Point Hold", "value": "point_hold"},
    {"label": "Receiving Team", "value": "o_point"},
    {"label": "Total Turnovers", "value": "num_turnovers"},
]

GAME_OPTIONS = [
    {
        "label": f"{row['away_team']} at {row['home_team']}, {row['game_date']}",
        "value": row["url"],
    }
    for _, row in games_dict[SEASONS[-1]].iterrows()
]

HOME_AWAY_OPTIONS = [
    {"label": "Home Team", "value": 1},
    {"label": "Away Team", "value": 0},
]


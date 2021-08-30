import audl_advanced_stats as audl
from datetime import datetime, timedelta

# All available AUDL season with the requisite stats
SEASONS = [
    2021,
]

# Get all seasons of games
games_dict = dict()
for season in SEASONS:
    games_dict[season] = audl.Season(year=season).get_game_info(override=False)

GAME_FLOW_TEAM_OPTIONS = [{"label": "Any Team", "value": "any"}] + [
    {"label": row["team_name"], "value": row["team_abbrev"]}
    for i, row in audl.Season().get_teams().iterrows()
]

GAME_FLOW_COLOR_OPTIONS = [
    {"label": "Receiving Team", "value": "o_point"},
    {"label": "Point Outcome", "value": "point_outcome"},
    {"label": "Point Hold", "value": "point_hold"},
    {"label": "Total Turnovers", "value": "num_turnovers"},
]

GAME_OPTIONS = [
    {
        "label": f"{row['away_team']} at {row['home_team']}, {row['game_date']}",
        "value": row["url"],
    }
    for _, row in games_dict[SEASONS[-1]].iterrows()
    if row["events_exist"]
]

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

HEATMAP_TEAM_OPTIONS = [
    {"label": row["team_name"], "value": row["team_id"]}
    for i, row in audl.Season().get_teams().iterrows()
]

HEATMAP_PLAYER_OPTIONS = [
    {"label": row["player_name"], "value": row["player_id"]}
    for i, row in audl.Season().get_players().iterrows()
]

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

PLAYER_STATS_PLAYOFFS_OPTIONS = [
    {"label": "Regular Season", "value": False},
    {"label": "Playoffs", "value": True},
    {"label": "Reg. Season & Playoffs", "value": "all"},
]

PLAYER_STATS_BY_GAME_OPTIONS = [
    {"label": "General", "value": "general"},
    {"label": "Plus/Minus Overview", "value": "plus_minus_overview"},
    {"label": "Playing Time", "value": "playing_time"},
    {"label": "Usage", "value": "usage"},
    {"label": "Throw Types", "value": "throw_types"},
    {"label": "Reception Types", "value": "reception_types"},
    {"label": "Yardage Overview", "value": "yardage_overview"},
    {"label": "Yardage (Centering Passes)", "value": "yardage_overview_centering"},
    {"label": "Team Success", "value": "team_success"},
    {"label": "Per Possession", "value": "per_possession"},
    {"label": "Per Touch", "value": "per_touch"},
]

PLAYER_STATS_BY_SEASON_OPTIONS = [
    {
        "label": "General",
        "value": "general",
    },  # Add per-game toggle and column for games
    {
        "label": "Plus/Minus Overview",
        "value": "plus_minus_overview",
    },  # Add per-game toggle and column for games
    {
        "label": "Playing Time",
        "value": "playing_time",
    },  # Add per-game toggle and column for games
    {"label": "Usage", "value": "usage"},  # Add per-game toggle and column for games
    {
        "label": "Throw Types",
        "value": "throw_types",
    },  # Add per-game toggle and column for games
    {
        "label": "Reception Types",
        "value": "reception_types",
    },  # Add per-game toggle and column for games
    {
        "label": "Yardage Overview",
        "value": "yardage_overview",
    },  # Add per-game toggle and column for games
    {
        "label": "Yardage (Centering Passes)",
        "value": "yardage_overview_centering",
    },  # Add per-game toggle and column for games
    {
        "label": "Team Success",
        "value": "team_success",
    },  # Add per-game toggle and column for games
    {
        "label": "Per Possession",
        "value": "per_possession",
    },  # Add per-game toggle and column for games
    {
        "label": "Per Touch",
        "value": "per_touch",
    },  # Add per-game toggle and column for games
]

PLAYER_STATS_COLS_DISPLAY = {
    "name": "Player",
    "team": "Team",
    "opponent": "Opp.",
    "game_date": "Date",
    "year": "Year",
    "games": "Games",
    "total_points": "Pts Played",
    "o_points": "O Pts",
    "d_points": "D Pts",
    "minutes_played": "Min.",
    "plus_minus": "+/-",
    "completions": "CMP",
    "receptions": "REC",
    "goals": "GLS",
    "assists": "AST",
    "turnovers": "TO",
    "blocks": "BLK",
    "throwaways": "T",
    "drops": "D",
    "stalls": "S",
    "goals_pp": "GLS PP",
    "assists_pp": "AST PP",
    "throwaways_pp": "T PP",
    "drops_pp": "D PP",
    "stalls_pp": "S PP",
    "blocks_pp": "BLK PP",
    "yyards_throwing_total": "Yds Thr Y",
    "yyards_receiving_total": "Yds Rec Y",
    "yyards_total": "Tot Yds Y",
    "total_possessions": "Poss Played",
    "o_possessions": "O Poss",
    "d_possessions": "D Poss",
    "throw_attempts": "THR Att",
    "attempts_dish": "DSH Att",
    "attempts_dump": "DMP Att",
    "attempts_huck": "HCK Att",
    "attempts_swing": "SWG Att",
    "attempts_throw": "OTH Att",
    "completions_dish": "DSH CMP",
    "completions_dump": "DMP CMP",
    "completions_huck": "HCK CMP",
    "completions_swing": "SWG CMP",
    "completions_throw": "OTH CMP",
    "completion_dish_pct": "DSH CMP%",
    "completion_dump_pct": "DMP CMP%",
    "completion_huck_pct": "HCK CMP%",
    "completion_swing_pct": "SWG CMP%",
    "completion_throw_pct": "OTH CMP%",
    "receptions_dish": "DSH REC",
    "receptions_dump": "DMP REC",
    "receptions_huck": "HCK REC",
    "receptions_swing": "SWG REC",
    "receptions_throw": "OTH REC",
    "receptions_dish_pct": "DSH %",
    "receptions_dump_pct": "DMP %",
    "receptions_huck_pct": "HCK %",
    "receptions_swing_pct": "SWG %",
    "receptions_throw_pct": "OTH %",
    "attempts_dish_pct": "DSH %",
    "attempts_dump_pct": "DMP %",
    "attempts_huck_pct": "HCK %",
    "attempts_swing_pct": "SWG %",
    "attempts_throw_pct": "OTH %",
    "xyards_throwing_total": "Yds Thr X",
    "yards_throwing_total": "Yds Thr X&Y",
    "xyards_receiving_total": "Yds Rec X",
    "yards_receiving_total": "Yds Rec X&Y",
    "xyards_total": "Tot Yds X",
    "yards_total": "Tot Yds X&Y",
    "xyards_throwaway": "T Yds X",
    "yyards_throwaway": "T Yds Y",
    "yards_throwaway": "T Yds X&Y",
    "completions_team_pct": "CMP USG",
    "throwaways_team_pct": "T USG",
    "assists_team_pct": "AST USG",
    "goals_team_pct": "GLS USG",
    "blocks_team_pct": "BLK USG",
    "points_team_pct": "PTS USG",
    "o_points_team_pct": "O-PTS USG",
    "d_points_team_pct": "D-PTS USG",
    "possessions_team_pct": "POS USG",
    "o_possessions_team_pct": "O-POS USG",
    "d_possessions_team_pct": "D-POS USG",
    "xyards_total_pct": "Tot Yds X USG",
    "yyards_total_pct": "Tot Yds Y USG",
    "yards_total_pct": "Tot Yds X&Y USG",
    "xyards_throwing_total_pct": "Thr Yds X USG",
    "yyards_throwing_total_pct": "Thr Yds Y USG",
    "yards_throwing_total_pct": "Thr Yds X&Y USG",
    "xyards_receiving_total_pct": "Rec Yds X USG",
    "yyards_receiving_total_pct": "Rec Yds Y USG",
    "yards_receiving_total_pct": "Rec Yds X&Y USG",
    "o_point_scores": "O Pt Scores",
    "o_point_score_pct": "O Pt Score%",
    "o_point_noturns": "O Pt No Turns",
    "o_point_noturn_pct": "O Pt No Turn%",
    "d_point_scores": "D Pt Scores",
    "d_point_score_pct": "D Pt Score%",
    "d_point_turns": "D Pt Turns",
    "d_point_turn_pct": "D Pt Turn%",
    "o_possession_scores": "O Poss Scores",
    "o_possession_score_pct": "O Poss Score%",
    "d_possession_scores_allowed": "D Poss Scores Alwd",
    "d_possession_score_allowed_pct": "D Poss Scores Alwd%",
    "xyards_throwing_center": "Yds Thr X Ctr",
    "yyards_throwing_center": "Yds Thr Y Ctr",
    "yards_throwing_center": "Yds Thr X&Y Ctr",
    "xyards_receiving_center": "Yds Rec X Ctr",
    "yyards_receiving_center": "Yds Rec Y Ctr",
    "yards_receiving_center": "Yds Rec X&Y Ctr",
    "xyards_center": "Tot Yds X Ctr",
    "yyards_center": "Tot Yds Y Ctr",
    "yards_center": "Tot Yds X&Y Ctr",
    "xyards_throwing": "Yds Thr X No Ctr",
    "yyards_throwing": "Yds Thr Y No Ctr",
    "yards_throwing": "Yds Thr X&Y No Ctr",
    "xyards_receiving": "Yds Rec X No Ctr",
    "yyards_receiving": "Yds Rec Y No Ctr",
    "yards_receiving": "Yds Rec X&Y No Ctr",
    "xyards": "Tot Yds X No Ctr",
    "yyards": "Tot Yds Y No Ctr",
    "yards": "Tot Yds X&Y No Ctr",
    "completion_pct": "CMP%",
    "reception_pct": "REC%",
    "turnovers_pp": "TO PP",
    "xyards_throwing_pp": "Yds Thr X PP",
    "yyards_throwing_pp": "Yds Thr Y PP",
    "yards_throwing_pp": "Yds Thr X&Y PP",
    "xyards_receiving_pp": "Yds Rec X PP",
    "yyards_receiving_pp": "Yds Rec Y PP",
    "yards_receiving_pp": "Yds Rec X&Y PP",
    "xyards_pp": "Tot Yds X PP",
    "yyards_pp": "Tot Yds Y PP",
    "yards_pp": "Tot Yds X&Y PP",
    "catch_attempts": "REC Att",
    "assists_perthrowattempt": "Ast/THR",
    "goals_percatchattempt": "Gls/REC",
    "xyards_throwing_percompletion": "Yds Thr X/CMP",
    "yyards_throwing_percompletion": "Yds Thr Y/CMP",
    "yards_throwing_percompletion": "Yds Thr X&Y/CMP",
    "xyards_receiving_perreception": "Yds Rec X/REC",
    "yyards_receiving_perreception": "Yds Rec Y/REC",
    "yards_receiving_perreception": "Yds Rec X&Y/REC",
    "xyards_throwing_perthrowaway": "Yds Thr X/T",
    "yyards_throwing_perthrowaway": "Yds Thr Y/T",
    "yards_throwing_perthrowaway": "Yds Thr X&Y/T",
    "yx_ratio_throwing": "Y:X Thr Yds Ratio",
    "yx_ratio_receiving": "Y:X Rec Yds Ratio",
}

PLAYER_GAME_STATS_INFO_COLS = [
    "name",
    "team",
    "opponent",
    "year",
    "game_date",
]

PLAYER_SEASON_STATS_INFO_COLS = [
    "name",
    "team",
    "year",
    "games",
]

PLAYER_STATS_OPTIONS_COLUMNS = {
    "general": [
        "total_points",
        "o_points",
        "d_points",
        "minutes_played",
        "plus_minus",
        "completions",
        "completion_pct",
        "receptions",
        "reception_pct",
        "goals",
        "assists",
        "turnovers",
        "blocks",
        "yyards_throwing_total",
        "yyards_receiving_total",
        "yyards_total",
    ],
    "plus_minus_overview": [
        "plus_minus",
        "goals",
        "assists",
        "throwaways",
        "drops",
        "stalls",
        "blocks",
        "o_possessions",
        "d_possessions",
        "goals_pp",
        "assists_pp",
        "throwaways_pp",
        "drops_pp",
        "stalls_pp",
        "blocks_pp",
    ],
    "playing_time": [
        "total_points",
        "points_team_pct",
        "o_points",
        "o_points_team_pct",
        "d_points",
        "d_points_team_pct",
        "total_possessions",
        "possessions_team_pct",
        "o_possessions",
        "o_possessions_team_pct",
        "d_possessions",
        "d_possessions_team_pct",
        "minutes_played",
    ],
    "usage": [
        "total_points",
        "o_points",
        "d_points",
        "total_possessions",
        "o_possessions",
        "d_possessions",
        "completions_team_pct",
        "throwaways_team_pct",
        "assists_team_pct",
        "goals_team_pct",
        "blocks_team_pct",
        "xyards_throwing_total_pct",
        "yyards_throwing_total_pct",
        "yards_throwing_total_pct",
        "xyards_receiving_total_pct",
        "yyards_receiving_total_pct",
        "yards_receiving_total_pct",
        "xyards_total_pct",
        "yyards_total_pct",
        "yards_total_pct",
    ],
    "throw_types": [
        "completions",
        "throw_attempts",
        "completions_dump",
        "attempts_dump",
        "completion_dump_pct",
        "attempts_dump_pct",
        "completions_dish",
        "attempts_dish",
        "completion_dish_pct",
        "attempts_dish_pct",
        "completions_swing",
        "attempts_swing",
        "completion_swing_pct",
        "attempts_swing_pct",
        "completions_huck",
        "attempts_huck",
        "completion_huck_pct",
        "attempts_huck_pct",
        "completions_throw",
        "attempts_throw",
        "completion_throw_pct",
        "attempts_throw_pct",
    ],
    "reception_types": [
        "receptions",
        "receptions_dump",
        "receptions_dump_pct",
        "receptions_dish",
        "receptions_dish_pct",
        "receptions_swing",
        "receptions_swing_pct",
        "receptions_huck",
        "receptions_huck_pct",
        "receptions_throw",
        "receptions_throw_pct",
    ],
    "yardage_overview": [
        "xyards_throwing_total",
        "yyards_throwing_total",
        "yards_throwing_total",
        "xyards_receiving_total",
        "yyards_receiving_total",
        "yards_receiving_total",
        "xyards_total",
        "yyards_total",
        "yards_total",
        "xyards_throwaway",
        "yyards_throwaway",
        "yards_throwaway",
        "yx_ratio_throwing",
        "yx_ratio_receiving",
    ],
    "yardage_overview_centering": [
        "xyards_throwing_center",
        "yyards_throwing_center",
        "yards_throwing_center",
        "xyards_receiving_center",
        "yyards_receiving_center",
        "yards_receiving_center",
        "xyards_center",
        "yyards_center",
        "yards_center",
        "xyards_throwing",
        "yyards_throwing",
        "yards_throwing",
        "xyards_receiving",
        "yyards_receiving",
        "yards_receiving",
        "xyards",
        "yyards",
        "yards",
    ],
    "team_success": [
        "total_points",
        "o_points",
        "o_point_scores",
        "o_point_score_pct",
        "o_point_noturns",
        "o_point_noturn_pct",
        "d_points",
        "d_point_scores",
        "d_point_score_pct",
        "d_point_turns",
        "d_point_turn_pct",
        "total_possessions",
        "o_possessions",
        "o_possession_scores",
        "o_possession_score_pct",
        "d_possessions",
        "d_possession_scores_allowed",
        "d_possession_score_allowed_pct",
    ],
    "per_possession": [
        "o_possessions",
        "d_possessions",
        "goals_pp",
        "assists_pp",
        "throwaways_pp",
        "drops_pp",
        "turnovers_pp",
        "stalls_pp",
        "blocks_pp",
        "xyards_throwing_pp",
        "yyards_throwing_pp",
        "yards_throwing_pp",
        "xyards_receiving_pp",
        "yyards_receiving_pp",
        "yards_receiving_pp",
        "xyards_pp",
        "yyards_pp",
        "yards_pp",
    ],
    "per_touch": [
        "completions",
        "throwaways",
        "catch_attempts",
        "assists_perthrowattempt",
        "goals_percatchattempt",
        "xyards_throwing_percompletion",
        "yyards_throwing_percompletion",
        "yards_throwing_percompletion",
        "xyards_receiving_perreception",
        "yyards_receiving_perreception",
        "yards_receiving_perreception",
        "xyards_throwing_perthrowaway",
        "yyards_throwing_perthrowaway",
        "yards_throwing_perthrowaway",
    ],
}

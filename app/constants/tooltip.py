"""Content of tooltips to be displayed when hovering on app elements."""

import base64
import dash_core_components as dcc
import dash_html_components as html
from os.path import join

# GAME FLOW TOOLTIPS
GAME_FLOW_TEAM_TOOLTIP = (
    "Select a team to filter the games dropdown to only their games."
)

GAME_TOOLTIP = (
    "Select the game you want to see by scrolling or searching.\n"
    "For each game, you will get a graph of the score throughout the game and\n"
    "a graph of substitution patterns.\n"
    "On the substitution graph, timeouts and injuries are marked with dashed lines.\n"
    "Players are grouped by how often they played together. Typically, o-line will be on top, followed by d-line players.\n"
    "You can click on any of the segments to see the possessions within that point."
)

HOME_AWAY_TOOLTIP = "Select whether you want to see the substitution patterns for the home or away team."

SUBSTITUTIONS_COLOR_TOOLTIP = "Select which factor to color the substitutions chart by."

POSSESSION_NUMBER_TOOLTIP = (
    "Some points have multiple possessions (when turnovers happen),\n"
    "in which case you can select the possession you want here.\n"
    "Click on a segment in the substitution chart to see the possessions for that point."
)

## HEATMAP TOOLTIPS
OUTCOME_MEASURE_TOOLTIP = (
    "Throw Outcome - Was the throw completed or not?\n"
    "Possession Outcome - How did the possession end, regardless of whether this throw was completed or not?"
)

OUTCOME_TOOLTIP = "The outcome of the throw or possession."

METRIC_TOOLTIP = "The value represented by the colors on the heat maps."

THROW_TOOLTIP = (
    "Thrower - Show locations based on where the throw originated.\n"
    "Receiver - Show locations based on where the throw ended up."
)

OPOINT_TOOLTIP = (
    "Filter results to only show results based on which team received the pull.\n"
    "For example, O-Points will only show results when teams received the pull,\n"
    "which will most often be each team's o-line.\n"
    "On the other hand, D-Points will only show results when teams pulled,\n"
    "which will most often be each team's d-line following a forced turnover."
)

TEAM_TOOLTIP = (
    "Filter by team to only see their possessions.\n"
    "When Offense is selected, you will see how the selected team(s) did when they had the disc.\n"
    "When Defense is selected, you will see how opposing teams did with the disc against the selected team(s)."
)

YEAR_TOOLTIP = "Filter by year to only see possessions from specific seasons."

PLAYER_TOOLTIP = (
    "Filter by player to only see their possessions.\n"
    "Note that if Receiver is selected for Location, the only turnovers you see will be drops.\n"
    "This is because throwaways do not record the intended receiver."
)

YARDS_TOOLTIP = "Filter by the total distance of the throw in any direction."

YYARDS_TOOLTIP = "Filter by the vertical distance of the throw."

XYARDS_TOOLTIP = "Filter by the horizontal distance of the throw."

Z_TOOLTIP = (
    "When this is turned on, the heatmap will set the coloring automatically.\n"
    "If you have selected a percentage for the metric, you can set the color range manually by disabling this switch.\n"
    "This can make it easier to compare heatmaps across different inputs since the color ranges will be the same."
)

PLAYER_STATS_BY_GAME_INFO_TOOLTIP = dcc.Markdown(
    "Use the dropdown selection to see different stats for each player.\n"
    "You can filter columns by typing in the row beneath the column headers. For example:\n"
    "* Typing `>=10` in the Pts Played column will filter the table to only players with at least 10 points played.\n"
    "* Typing `>2021-06-04` in the Date column will filter the table to only games played after 6/4/2021.\n"
    "* Typing `<0.9` in the CMP% column will filter the table to only players with a completion percentage below 90%.\n"
    "* Typing `NY` in the Team column will filter the table to only NY players. Note that this is case-sensitive.\n"
    "You will likely need to manually clear your filters before selecting a different stat page from the dropdown."
)

PLAYER_STATS_BY_SEASON_INFO_TOOLTIP = dcc.Markdown(
    "Use the dropdown selection to see different stats for each player.\n"
    "Use the Per-Game switch to toggle between seeing season totals and per-game averages for each player.\n"
    "You can filter columns by typing in the row beneath the column headers. For example:\n"
    "* Typing `>=10` in the Pts Played column will filter the table to only players with at least 10 points played.\n"
    "* Typing `<0.9` in the CMP% column will filter the table to only players with a completion percentage below 90%.\n"
    "* Typing `NY` in the Team column will filter the table to only NY players. Note that this is case-sensitive.\n"
    "You will likely need to manually clear your filters before selecting a different stat page from the dropdown."
)

PLAYER_STATS_HEADER_TOOLTIPS = {
    "opponent": "Opponent",
    "games": "Games played",
    "total_points": "# of pts where player was on at the start of the point",
    "o_points": "# of pts where player was on the field to receive the pull",
    "d_points": "# of pts where player was on defense at the time of the pull",
    "minutes_played": "Minutes played. Some of this data is missing.",
    "plus_minus": "GLS+AST+BLK-Turnovers",
    "completions": "Completions",
    "receptions": "Receptions",
    "goals": "Goals",
    "assists": "Assists",
    "turnovers": "Turnovers",
    "blocks": "Blocks",
    "throwaways": "Throwaways",
    "drops": "Drops",
    "stalls": "Stalls",
    "goals_pp": "Goals per possession",
    "assists_pp": "Assists per possession",
    "throwaways_pp": "Throwaways per possession",
    "drops_pp": "Drops per possession",
    "stalls_pp": "Stalls per possession",
    "blocks_pp": "Blocks per possession",
    "yyards_throwing_total": "Downfield throwing yards. Can be positive or negative.",
    "yyards_receiving_total": "Downfield receiving yards. Can be positive or negative.",
    "yyards_total": "Downfield throwing and receiving yards. Can be positive or negative.",
    "total_possessions": "# of possessions where player was on at the end of the possession",
    "o_possessions": "# of o-possessions where player was on at the end of the possession",
    "d_possessions": "# of d-possessions where player was on at the end of the possession",
    "throw_attempts": "Throw attempts: completions+throwaways+stalls",
    "attempts_dish": "Dish throw attempts",
    "attempts_dump": "Dump throw attempts",
    "attempts_huck": "Huck throw attempts",
    "attempts_swing": "Swing throw attempts",
    "attempts_throw": "Other types of throw attempts",
    "completions_dish": "Dish throw completions",
    "completions_dump": "Dump throw completions",
    "completions_huck": "Huck throw completions",
    "completions_swing": "Swing throw completions",
    "completions_throw": "Other types of throw completions",
    "completion_dish_pct": "Dish throw completion %",
    "completion_dump_pct": "Dump throw completion %",
    "completion_huck_pct": "Huck throw completion %",
    "completion_swing_pct": "Swing throw completion %",
    "completion_throw_pct": "Other types of throw completion %",
    "receptions_dish": "Dish receptions",
    "receptions_dump": "Dump receptions",
    "receptions_huck": "Huck receptions",
    "receptions_swing": "Swing receptions",
    "receptions_throw": "Other types of receptions",
    "receptions_dish_pct": r"% of receptions that are dishes",
    "receptions_dump_pct": r"% of receptions that are dumps",
    "receptions_huck_pct": r"% of receptions that are hucks",
    "receptions_swing_pct": r"% of receptions that are swings",
    "receptions_throw_pct": r"% of receptions that are other types of throws",
    "attempts_dish_pct": r"% of throw attempts that are dishes",
    "attempts_dump_pct": r"% of throw attempts that are dumps",
    "attempts_huck_pct": r"% of throw attempts that are hucks",
    "attempts_swing_pct": r"% of throw attempts that are swings",
    "attempts_throw_pct": r"% of throw attempts that are other types of throws",
    "xyards_throwing_total": "Sideways throwing yards. All throws count as positive yardage.",
    "yards_throwing_total": "Throwing yards in any direction. All throws count as positive yardage.",
    "xyards_receiving_total": "Sideways receiving yards. All receptions count as positive yardage.",
    "yards_receiving_total": "Receiving yards in any direction. All receptions count as positive yardage.",
    "xyards_total": "Sideways throwing and receiving yards. All count as positive yardage.",
    "yards_total": "Throwing and receiving yards in any direction. All receptions count as positive yardage.",
    "xyards_throwaway": "Sideways yards on throwaways",
    "yyards_throwaway": "Downfield yards on throwaways",
    "yards_throwaway": "Yards in any direction on throwaways",
    "throws_team_pct": r"% of team's throws player accounts for while on the field",
    "completions_team_pct": r"% of team's completions player accounts for while on the field",
    "throwaways_team_pct": r"% of team's throwaways player accounts for while on the field",
    "assists_team_pct": r"% of team's assists player accounts for while on the field",
    "goals_team_pct": r"% of team's goals player accounts for while on the field",
    "blocks_team_pct": r"% of team's blocks player accounts for while on the field",
    "xyards_total_pct": r"% of team's sideways throwing and receiving yards player accounts for while on the field",
    "yyards_total_pct": r"% of team's downfield throwing and receiving yards player accounts for while on the field",
    "yards_total_pct": r"% of team's throwing and receiving yards in any direction player accounts for while on the field",
    "xyards_throwing_total_pct": r"% of team's sideways throwing yards player accounts for while on the field",
    "yyards_throwing_total_pct": r"% of team's downfield throwing yards player accounts for while on the field",
    "yards_throwing_total_pct": r"% of team's throwing yards in any direction player accounts for while on the field",
    "xyards_receiving_total_pct": r"% of team's sideways receiving yards player accounts for while on the field",
    "yyards_receiving_total_pct": r"% of team's downfield receiving yards player accounts for while on the field",
    "yards_receiving_total_pct": r"% of team's receiving yards in any direction player accounts for while on the field",
    "points_team_pct": r"% of team's points player was on the field at the start of the point in games where the player was rostered",
    "o_points_team_pct": r"% of team's o-points player was on the field at the start of the point in games where the player was rostered",
    "d_points_team_pct": r"% of team's d-points player was on the field at the start of the point in games where the player was rostered",
    "possessions_team_pct": r"% of team's possessions player was on the field at the end of the possession in games where the player was rostered",
    "o_possessions_team_pct": r"% of team's o-possessions player was on the field at the end of the possession in games where the player was rostered",
    "d_possessions_team_pct": r"% of team's d-possessions player was on the field at the end of the possession in games where the player was rostered",
    "o_point_scores": "# of points player's team scored when player was on the field to start the o-point",
    "o_point_score_pct": r"% of points player's team scored when player was on the field to start the o-point",
    "o_point_noturns": "# of points player's team had 0 turnovers when player was on the field to start the o-point",
    "o_point_noturn_pct": r"% of points player's team had 0 turnovers when player was on the field to start the o-point",
    "d_point_scores": "# of points player's team scored when player was on the field to start the d-point",
    "d_point_score_pct": r"% of points player's team scored when player was on the field to start the d-point",
    "d_point_turns": "# of points opposing team turned it over at least once when player was on the field to start the d-point",
    "d_point_turn_pct": r"% of points opposing team turned it over at least once when player was on the field to start the d-point",
    "o_possession_scores": "# of scores on o-possessions when player was on the field to end the possession",
    "o_possession_score_pct": r"% of o-possessions ending in a score when player was on the field to end the possession",
    "d_possession_scores_allowed": "# of scores by opponent on d-possessions when player was on the field to end the possession",
    "d_possession_score_allowed_pct": r"% of d-possessions ending in opponent score when player was on the field to end the possession",
    "xyards_throwing_center": "Sideways throwing yards on centering passes (first throw after in-bounds pull for positive yards towards center of field)",
    "yyards_throwing_center": "Downfield throwing yards on centering passes (first throw after in-bounds pull for positive yards towards center of field)",
    "yards_throwing_center": "Throwing yards in any direction on centering passes (first throw after in-bounds pull for positive yards towards center of field)",
    "xyards_receiving_center": "Sideways receiving yards on centering passes (first throw after in-bounds pull for positive yards towards center of field)",
    "yyards_receiving_center": "Downfield receiving yards on centering passes (first throw after in-bounds pull for positive yards towards center of field)",
    "yards_receiving_center": "Receiving yards in any direction on centering passes (first throw after in-bounds pull for positive yards towards center of field)",
    "xyards_center": "Sideways throwing and receiving yards on centering passes",
    "yyards_center": "Downfield throwing and receiving yards on centering passes",
    "yards_center": "Throwing and receiving yards in any direction on centering passes",
    "xyards_throwing": "Sideways throwing yards on non-centering passes",
    "yyards_throwing": "Downfield throwing yards on non-centering passes",
    "yards_throwing": "Throwing yards in any direction on non-centering passes",
    "xyards_receiving": "Sideways receiving yards on non-centering passes",
    "yyards_receiving": "Downfield receiving yards on non-centering passes",
    "yards_receiving": "Receiving yards in any direction on non-centering passes",
    "xyards": "Sideways throwing and receiving yards on non-centering passes",
    "yyards": "Downfield throwing and receiving yards on non-centering passes",
    "yards": "Throwing and receiving yards in any direction on non-centering passes",
    "completion_pct": "Completions/(completions+throwaways+stalls)",
    "reception_pct": "Receptions/(receptions+drops)",
    "completions_pp": "Completions per possession",
    "throws_pp": "Throw attempts per possession",
    "turnovers_pp": "Turnovers per possession",
    "xyards_throwing_pp": "Sideways throwing yards per possession",
    "yyards_throwing_pp": "Downfield throwing yards per possession",
    "yards_throwing_pp": "Throwing yards in any direction per possession",
    "xyards_receiving_pp": "Sideways receiving yards per possession",
    "yyards_receiving_pp": "Downfield receiving yards per possession",
    "yards_receiving_pp": "Receiving yards in any direction per possession",
    "xyards_pp": "Sideways throwing and receiving yards per possession",
    "yyards_pp": "Downfield throwing and receiving yards per possession",
    "yards_pp": "Throwing and receiving yards in any direction per possession",
    "catch_attempts": "Reception attempts (receptions+drops)",
    "assists_perthrowattempt": "Assists per throw attempt",
    "goals_percatchattempt": "Goals per reception attempt",
    "xyards_throwing_percompletion": "Sideways throwing yards per completion",
    "yyards_throwing_percompletion": "Downfield throwing yards per completion",
    "yards_throwing_percompletion": "Throwing yards in any direction per completion",
    "xyards_receiving_perreception": "Sideways receiving yards per completion",
    "yyards_receiving_perreception": "Downfield receiving yards per completion",
    "yards_receiving_perreception": "Receiving yards in any direction per completion",
    "xyards_throwing_perthrowaway": "Sideways yards per throwaway",
    "yyards_throwing_perthrowaway": "Downfield per throwaway",
    "yards_throwing_perthrowaway": "Yards in any direction per throwaway",
    "yx_ratio_throwing": "Ratio of downfield to sideways throwing yards",
    "yx_ratio_receiving": "Ratio of downfield to sideways receiving yards",
}

## END OF PERIOD PROBABILITY TOOLTIPS
TIME_AT_MIDFIELD_TOOLTIP = (
    "The amount of time left in the period when the disc crosses midfield.\n"
    "The difference between this and the time to start trying to score is\n"
    "how long the clock will need to be run without trying to score."
)

TIME_TO_SCORE_TOOLTIP = "The amount of time left in the period at which the offense will start trying to score."

P_TURN_OPPONENT_SCORE_UNDER_TOOLTIP = (
    "The probability the other team will score after a turnover from\n"
    "farther than midfield with less than x seconds left.\n"
    "This represents the other team scoring after the offense turns it over\n"
    "while trying to score after successfully running clock."
)

P_TURN_OPPONENT_SCORE_OVER_TOOLTIP = (
    "The probability the other team will score after a turnover from\n"
    "farther than midfield with more than x seconds left.\n"
    "This represents the other team scoring after the offense turns it over\n"
    "while trying to run clock OR the other team scoring after the offense turns it over\n"
    "while trying to score while not trying to run clock."
)

P_SCORE_OPPONENT_SCORE_UNDER_TOOLTIP = (
    "The probability the other team will score after the offense scores\n"
    "with less than x seconds left."
)

P_SCORE_OPPONENT_SCORE_OVER_TOOLTIP = (
    "The probability the other team will score after the offense scores\n"
    "with more than x seconds left."
)

P_SCORE_RUN_CLOCK_TOOLTIP = (
    "The probability the offense will score given that they have successfully\n"
    "run the clock down to x seconds.\n"
    "You should NOT account for the possibility of turning the disc over while\n"
    "running clock here. That is handled with the prob. of completion while running\n"
    "clock and the time per pass while running clock."
)

P_SCORE_NO_RUN_CLOCK_TOOLTIP = (
    "The probability the offense will score when they are not using the strategy\n"
    "of running the clock down.\n"
    "Note that you can simulate a wide open look to the endzone w/ greater than x\n"
    "seconds left by changing this probability to 99 or 100."
)

P_COMPLETION_TOOLTIP = (
    "The probability of completing each pass while running clock.\n"
    "This is combined with time per pass to estimate how likely the offense is\n"
    "to retain possession while running clock."
)

TIME_PER_PASS_TOOLTIP = (
    "The amount of time each pass takes while running clock.\n"
    "This is used to estimate the number of passes needed to run the clock\n"
    "down to the desired time. The number of passes is then combined with the\n"
    "probability of completion to estimate how likely the offense is to retain\n"
    "possession while running clock."
)

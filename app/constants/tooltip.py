"""Content of tooltips to be displayed when hovering on app elements."""

# GAME FLOW TOOLTIPS
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

import audl_advanced_stats as audl
import dash_html_components as html
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    Output("heatmap-description", "children"),
    [
        Input("heatmap-outcome-measure-dropdown", "value"),
        Input("heatmap-outcome-dropdown", "value"),
        Input("heatmap-metric-dropdown", "value"),
        Input("heatmap-opoint-dropdown", "value"),
        Input("heatmap-throw-dropdown", "value"),
        Input("heatmap-team-radio", "value"),
        Input("heatmap-team-dropdown", "value"),
        Input("heatmap-player-dropdown", "value"),
        Input("heatmap-yards-slider", "value"),
        Input("heatmap-xyards-slider", "value"),
        Input("heatmap-yyards-slider", "value"),
        Input("heatmap-filtered-store", "data"),
    ],
)
def heatmap_description(
    outcome_measure,
    outcome,
    metric,
    o_point,
    throw,
    team_radio,
    teams,
    players,
    yards,
    xyards,
    yyards,
    filtered,
):
    """Create a figure description based on inputs."""

    outcome_str = outcome

    metric_dict = {
        "pct": "percentage",
        "count": "locations",
        "yards_raw": "avg. total yards",
        "yyards_raw": "avg. downfield yards",
        "xyards": "avg. sideways yards",
    }
    metric_str = metric_dict[metric]

    outcome_measure_dict = {
        "possession_outcome_general": "possession",
        "throw_outcome": "throw",
    }
    outcome_measure_str = outcome_measure_dict[outcome_measure]

    if throw:
        throw_str1 = "Throws"
    else:
        throw_str1 = "Receptions"

    o_point_dict = {
        "all": "O and D Points",
        True: "O Points",
        False: "D Points",
    }
    o_point_str = o_point_dict[o_point]

    if teams == []:
        teams_str = "all teams"
    else:
        teams_dict = (
            audl.Season().get_teams().set_index("team_id")["team_name"].to_dict()
        )
        teams_str = ", ".join([teams_dict[team] for team in teams])

    team_radio_str = team_radio

    if players == []:
        players_str = "All Players"
    else:
        players_dict = (
            audl.Season()
            .get_players()
            .set_index("player_id")["player_name"]
            .str.extract("(.*),", expand=False)
            .to_dict()
        )
        players_str = ", ".join([players_dict[player] for player in players])

    yards_base_str = f"{throw_str1.lower()} of "
    yards_str = yards_base_str
    if (yards == [0, 130]) and (yyards == [-120, 120]) and (xyards == [-30, 30]):
        yards_str += "any distance"
    else:
        if yards != [0, 130]:
            yards_str += f"{int(yards[0])} to {int(yards[1])} total yards"
        if xyards != [-30, 30]:
            if yards_str != yards_base_str:
                yards_str += ", "
            yards_str += f"{int(xyards[0])} to {int(xyards[1])} sideways yards"
        if yyards != [-120, 120]:
            if yards_str != yards_base_str:
                yards_str += ", "
            yards_str += f"{int(yyards[0])} to {int(yyards[1])} downfield yards"

    if filtered["filtered"]:
        if throw:
            throw_str2 = f"The second heat map shows all receptions from throws that started in the highlighted box. Click on the box in the second map to remove this filter."
        else:
            throw_str2 = f"The second heat map shows the starting points of all throws that ended in the highlighted box on this heat map. Click on the box in the second map to remove this filter."
    else:
        if throw:
            throw_str2 = f"The second heat map is currently showing receptions. Click anywhere on the first map to show only receptions on throws from that area."
        else:
            throw_str2 = f"The second heat map is currently showing throws. Click anywhere on the first map to show only throws that ended in that area."

    if outcome_measure == "throw_outcome":
        description = [
            html.H2(
                f"{outcome_str.title()} {metric_str.title()}",
                style={"text-align": "center"},
            ),
            f"Based on location of {throw_str1.lower()}",
            html.Br(),
            f"{o_point_str} with {teams_str} on {team_radio_str}. Showing {yards_str}.",
            html.Br(),
            f"Players: {players_str}",
            html.Br(),
            throw_str2,
        ]
    else:
        description = [
            html.H2(
                f"{metric_str.title()} of Touches Leading to a {outcome_str.title()}",
                style={"text-align": "center"},
            ),
            f"Based on possessions ending in a {outcome_str.lower()} and location of {throw_str1.lower()}",
            html.Br(),
            f"{o_point_str} with {teams_str} on {team_radio_str}. Showing {yards_str}.",
            html.Br(),
            f"Players: {players_str}",
            html.Br(),
            throw_str2,
        ]

    return description

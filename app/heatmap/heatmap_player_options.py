import audl_advanced_stats as audl
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    [
        Output("heatmap-player-dropdown", "options"),
        Output("heatmap-player-dropdown", "value"),
    ],
    [Input("heatmap-team-dropdown", "value"), Input("heatmap-team-radio", "value"),],
    [State("heatmap-player-dropdown", "value"),],
)
def heatmap_player_options(teams, team_radio, selected_players):
    """Update the player options based on the teams chosen."""
    # No teams selected, keep current player selection
    if teams == []:
        return HEATMAP_PLAYER_OPTIONS, selected_players
    if team_radio == "defense":
        opposing_players = (
            audl.Season()
            .get_games(small_file=True, build_new_file=False, qc=False)
            .query(f"opponent_team_id=={teams}")
            .drop_duplicates(["r", "r_after"])
        )
        playerlist = list(
            set(
                opposing_players["r"].dropna().unique().tolist()
                + opposing_players["r_after"].dropna().unique().tolist()
            )
        )
        players_df = audl.Season().get_players().query(f"player_id=={playerlist}")
    else:
        # All players on selected teams
        players_df = audl.Season().get_players().query(f"team_id=={teams}")

    options = [
        {"label": row["player_name"], "value": row["player_id"]}
        for i, row in players_df.iterrows()
    ]
    # Only keep players from previous selection who are on selected teams
    selected_players = players_df.query(f"player_id=={selected_players}")[
        "player_id"
    ].values.tolist()

    return options, selected_players

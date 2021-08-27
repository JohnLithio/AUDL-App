import audl_advanced_stats as audl
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output, State
from ..constants import *
from ..server import app


@app.callback(
    [
        Output("end-of-period-description", "children"),
        Output("end-of-period-turn-opponent-score-under-label", "children"),
        Output("end-of-period-turn-opponent-score-over-label", "children"),
        Output("end-of-period-score-opponent-score-under-label", "children"),
        Output("end-of-period-score-opponent-score-over-label", "children"),
    ],
    [
        Input("end-of-period-time-to-score", "value"),
        Input("end-of-period-time-at-midfield", "value"),
        Input("end-of-period-turn-opponent-score-under", "value"),
        Input("end-of-period-turn-opponent-score-over", "value"),
        Input("end-of-period-score-opponent-score-under", "value"),
        Input("end-of-period-score-opponent-score-over", "value"),
        Input("end-of-period-score-run-clock", "value"),
        Input("end-of-period-score-no-run-clock", "value"),
        Input("end-of-period-completion", "value"),
        Input("end-of-period-time-per-pass", "value"),
    ],
)
def end_of_period_probabilities(
    time_to_score,
    time_at_midfield,
    p_turn_opponent_score_under,
    p_turn_opponent_score_over,
    p_score_opponent_score_under,
    p_score_opponent_score_over,
    p_score_run_clock,
    p_score_no_run_clock,
    p_completion,
    time_per_pass,
):
    """Calculate the expected points based on input probabilties."""
    # Set labels
    p_turn_opponent_score_under_label = (
        f"Prob. opp. score after turn, <{time_to_score}s"
    )
    p_turn_opponent_score_over_label = f"Prob. opp. score after turn, >{time_to_score}s"
    p_score_opponent_score_under_label = (
        f"Prob. opp. score after score, <{time_to_score}s"
    )
    p_score_opponent_score_over_label = (
        f"Prob. opp. score after score, >{time_to_score}s"
    )

    # Convert to probabilities
    p_turn_opponent_score_under = p_turn_opponent_score_under / 100
    p_turn_opponent_score_over = p_turn_opponent_score_over / 100
    p_score_opponent_score_under = p_score_opponent_score_under / 100
    p_score_opponent_score_over = p_score_opponent_score_over / 100
    p_score_run_clock = p_score_run_clock / 100
    p_score_no_run_clock = p_score_no_run_clock / 100
    p_completion = p_completion / 100

    #### CALCULATIONS
    ### RUNNING CLOCK
    # Probability of maintaing possession while running clock
    time_run_clock = time_at_midfield - time_to_score
    num_passes = time_run_clock / time_per_pass
    p_poss_run_clock = p_completion ** (num_passes)

    ## They score 1 more than us
    # We score 0, they score 1
    p_turn_after_run_clock_score = (
        p_turn_opponent_score_under * (1 - p_score_run_clock) * p_poss_run_clock
    )
    p_turn_while_run_clock_score = p_turn_opponent_score_over * (1 - p_poss_run_clock)
    p_minus1_run_clock = p_turn_after_run_clock_score + p_turn_while_run_clock_score

    ## They score the same as us
    # We score 0, they score 0
    p_turn_after_run_clock_no_score = (
        (1 - p_turn_opponent_score_under) * (1 - p_score_run_clock) * p_poss_run_clock
    )
    p_turn_while_run_clock_no_score = (1 - p_turn_opponent_score_over) * (
        1 - p_poss_run_clock
    )

    # We score 1, they score 1
    p_score_after_run_clock_score = (
        p_score_opponent_score_under * p_score_run_clock * p_poss_run_clock
    )
    p_even_run_clock = (
        p_turn_after_run_clock_no_score
        + p_turn_while_run_clock_no_score
        + p_score_after_run_clock_score
    )

    ## We score 1 more than them
    # We score 1, they score 0
    p_score_after_run_clock_no_score = (
        (1 - p_score_opponent_score_under) * p_score_run_clock * p_poss_run_clock
    )
    p_plus1_run_clock = p_score_after_run_clock_no_score

    assert (
        np.round(p_minus1_run_clock + p_even_run_clock + p_plus1_run_clock, 3) == 1.000
    )

    expected_margin_run_clock = p_plus1_run_clock - p_minus1_run_clock

    run_clock_str = [
        html.H3("Intentionally Running Clock"),
        f"Probability of losing (0-1): {p_minus1_run_clock:.1%}",
        html.Br(),
        f"Probability of tying (0-0 or 1-1): {p_even_run_clock:.1%}",
        html.Br(),
        f"Probability of winning (1-0): {p_plus1_run_clock:.1%}",
        html.Br(),
        f"Expected Margin: {expected_margin_run_clock:+.2f} points",
    ]

    ### NOT RUNNING CLOCK
    ## They score 1 more than us
    # We score 0, they score 1
    p_minus1_no_run_clock = p_turn_opponent_score_over * (1 - p_score_no_run_clock)

    ## They score the same as us
    # We score 0, they score 0
    p_turn_no_run_clock_no_score = (1 - p_score_no_run_clock) * (
        1 - p_turn_opponent_score_over
    )

    # We score 1, they score 1
    p_score_no_run_clock_score = p_score_no_run_clock * p_score_opponent_score_over
    p_even_no_run_clock = p_turn_no_run_clock_no_score + p_score_no_run_clock_score

    ## We score 1 more than them
    # We score 1, they score 0
    p_plus1_no_run_clock = p_score_no_run_clock * (1 - p_score_opponent_score_over)

    assert (
        np.round(p_minus1_no_run_clock + p_even_no_run_clock + p_plus1_no_run_clock, 3)
        == 1.000
    )

    expected_margin_no_run_clock = p_plus1_no_run_clock - p_minus1_no_run_clock

    no_run_clock_str = [
        html.H3(f"Not Running Clock (Score w/ >{time_to_score} seconds)"),
        f"Probability of losing (0-1): {p_minus1_no_run_clock:.1%}",
        html.Br(),
        f"Probability of tying (0-0 or 1-1): {p_even_no_run_clock:.1%}",
        html.Br(),
        f"Probability of winning (1-0): {p_plus1_no_run_clock:.1%}",
        html.Br(),
        f"Expected Margin: {expected_margin_no_run_clock:+.2f} points",
    ]

    # Combine results from running clock and not running clock
    diff_expected_margin = expected_margin_run_clock - expected_margin_no_run_clock
    if diff_expected_margin > 0:
        diff_str = f"{diff_expected_margin:.2f} points better than"
    elif diff_expected_margin == 0:
        diff_str = f"as good as"
    else:
        diff_str = f"{np.abs(diff_expected_margin):.2f} points worse than"

    diff_expected_margin_str = [
        dcc.Markdown(
            f"**With these inputs, we'd expect intentionally running clock to be {diff_str} not running clock**"
        ),
    ]

    full_str = (
        no_run_clock_str
        + [html.Br()]
        + run_clock_str
        + [html.Br()]
        + [html.Br()]
        + diff_expected_margin_str
    )

    return (
        full_str,
        p_turn_opponent_score_under_label,
        p_turn_opponent_score_over_label,
        p_score_opponent_score_under_label,
        p_score_opponent_score_over_label,
    )

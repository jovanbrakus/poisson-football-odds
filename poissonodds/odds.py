# Simple odds prediction model using Poisson distribution
import itertools

import pandas as pd
from scipy.stats import poisson

# Consider only scores up to 6:6 with significant probabilities
HOME_WIN_SCORES = set(res for res in itertools.product(range(7), range(7)) if res[0] > res[1])
AWAY_WIN_SCORES = set(res for res in itertools.product(range(7), range(7)) if res[0] < res[1])
DRAW_SCORES = set(res for res in itertools.product(range(7), range(7)) if res[0] == res[1])

ODDS_COLUMNS = ['HomeTeam', 'AwayTeam', 'HomeWin', 'AwayWin', 'Draw']


def get_odds_for_results(home_ft_mean, away_ft_mean, scores):
    odds = 0
    for (home_goals, away_goals) in scores:
        score_odds = poisson.pmf(home_goals, home_ft_mean) * poisson.pmf(away_goals, away_ft_mean)
        odds += score_odds
    return odds


def match_odds_poisson(data, home_team, away_team):
    home_ft_mean = data.groupby('HomeTeam').mean().loc[home_team].loc['FTHG']
    away_ft_mean = data.groupby('AwayTeam').mean().loc[away_team].loc['FTAG']

    odds_home_win = get_odds_for_results(home_ft_mean, away_ft_mean, HOME_WIN_SCORES)
    odds_away_win = get_odds_for_results(home_ft_mean, away_ft_mean, AWAY_WIN_SCORES)
    odds_draw = get_odds_for_results(home_ft_mean, away_ft_mean, DRAW_SCORES)

    odds = pd.DataFrame(data=[[home_team, away_team, odds_home_win, odds_away_win, odds_draw]], columns=ODDS_COLUMNS)
    return odds


def complete_odds(data):
    home_teams = set(data.HomeTeam.unique())
    away_teams = set(data.HomeTeam.unique())
    teams = home_teams.union(away_teams)

    match_odds = list()

    for home_team in teams:
        for away_team in teams:
            if home_team == away_team:
                continue
            match_odds.append(match_odds_poisson(data, home_team, away_team))

    odds = pd.concat(match_odds).reset_index(drop=True)
    return odds







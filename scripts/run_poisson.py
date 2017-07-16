import logging

from poissonodds.loader import fetch_season_data, ENGLAND_PREMIER_LEAGUE, SEASON_2016_2017
from poissonodds.odds import match_odds_poisson, complete_odds

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)

if __name__ == '__main__':
    season_data = fetch_season_data(SEASON_2016_2017, ENGLAND_PREMIER_LEAGUE)
    match_odds = match_odds_poisson(season_data, 'Arsenal', 'Liverpool')
    print match_odds
    complete_odds = complete_odds(season_data)
    print complete_odds

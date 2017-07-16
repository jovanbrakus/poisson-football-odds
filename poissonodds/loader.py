# football-data.co.uk loader

import StringIO

import requests
import pandas as pd

FOOTBALL_DATA_URL = 'http://www.football-data.co.uk/mmz4281/{0}/{1}.csv'

SEASON_2015_2016 = '1516'
SEASON_2016_2017 = '1617'

ITALY_SERIE_A = 'I1'
ITALY_SERIE_B = 'I2'
ENGLAND_PREMIER_LEAGUE = 'E0'
ENGLAND_CHAMPIONSHIP = 'E1'


def fetch_season_data(season, competition):
    url = FOOTBALL_DATA_URL.format(season, competition)
    csv_string = requests.get(url).content
    season_data = pd.read_csv(StringIO.StringIO(csv_string.decode('utf-8')))
    return season_data

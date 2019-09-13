import pandas as pd
import requests

#nba stats data retrieval

def GetSeason(year, less=True):
  '''
  Scrapes a season of NBA Game Statistics from stats.nba.com

  Parameters
  ---------------
  year - {int} - year corresponding to the season of data to be retrieved

  less - {boolean} - optional boolean, if true returns a DataFrame with some of the more exotic columns dropped

  Returns
  ---------------
  A Pandas Dataframe with the game statistics for the season provided with year.
  '''
    import requests

    cookies = {
        'nbaMembershipRedirectInfo': '%7B%22externalUrl%22%3A%22https%3A//www.nba.com/leaguepass/pricing%22%2C%22externalCancelUrl%22%3A%22https%3A//www.nba.com/leaguepass/%22%2C%22currentMessage%22%3A%22membership.redirect.external%22%7D',
        's_ppvl': '%5B%5BB%5D%5D',
        's_ppv': 'nba%253Aleaguepass%2C32%2C32%2C920%2C1886%2C920%2C1920%2C1080%2C1%2CP',
        's_cc': 'true',
        's_tps': '76650',
        's_pvs': '76296',
        'check': 'true',
        'AMCVS_248F210755B762187F000101%40AdobeOrg': '1',
        's_ecid': 'MCMID%7C02488456132187434068685646980771421773',
        'AMCVS_7FF852E2556756057F000101%40AdobeOrg': '1',
        's_sq': '%5B%5BB%5D%5D',
        '_ga': 'GA1.2.998942045.1568145342',
        '_gid': 'GA1.2.608653446.1568145342',
        'ug': '5d77ffbd044d430a3f804a0015f02fc0',
        'ugs': '1',
        'AMCV_7FF852E2556756057F000101%40AdobeOrg': '1687686476%7CMCIDTS%7C18150%7CMCMID%7C01023594746882908429129513183339380608%7CMCAID%7CNONE%7CMCOPTOUT-1568149802s%7CNONE%7CvVersion%7C3.0.0%7CMCAAMLH-1568750141%7C9%7CMCAAMB-1568750141%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI',
        '_fbp': 'fb.1.1568145342299.1316504188',
        '_gat': '1',
        'AMCV_248F210755B762187F000101%40AdobeOrg': '1687686476%7CMCIDTS%7C18150%7CMCMID%7C02488456132187434068685646980771421773%7CMCAAMLH-1568768895%7C9%7CMCAAMB-1568768895%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1568171295s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0',
        'ak_bmsc': 'F9124FE70E4DA7FF4732D5506677C6E9B81D2384C70400000149785D20007B60~plcMbaaydIYeMqAhUYZiGzxSsIoGT84R9FW+C+zhKQ+27iybEUtOquEiG2PDi1H8mKJw1xeSYX3pRwikx84MNByaQWapOpL1exGTz7/qNDwrIY53rhkIVWIV1DvUjo7BNXMv2l84O99p96KzcpQNUAS6yksoDh2mVlc9287sB37SvSlAov/6lGFCJYj7ztAVXa5UQwYX+jLrw2RSge9icC7nsKabLUFien7z0VF9GibZg=',
        'mbox': 'PC#a78bbd12c599421f8e2bba4cdced28a5.28_95#1631408895|session#62025c767eb4484690a680a906ffa254#1568165974',
    }

    headers = {
        'Sec-Fetch-Mode': 'cors',
        'X-NewRelic-ID': 'VQECWF5UChAHUlNTBwgBVw==',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Sec-Fetch-Site': 'same-origin',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'Referer': 'https://stats.nba.com/teams/boxscores-traditional/?Season=2018-19&SeasonType=Regular%20Season',
        'Connection': 'keep-alive',
        'x-nba-stats-origin': 'stats',
    }

    params = (
        ('DateFrom', ''),
        ('DateTo', ''),
        ('GameSegment', ''),
        ('LastNGames', '0'),
        ('LeagueID', '00'),
        ('Location', ''),
        ('MeasureType', 'Base'),
        ('Month', '0'),
        ('OpponentTeamID', '0'),
        ('Outcome', ''),
        ('PORound', '0'),
        ('PaceAdjust', 'N'),
        ('PerMode', 'Totals'),
        ('Period', '0'),
        ('PlusMinus', 'N'),
        ('Rank', 'N'),
        ('Season', f'{year}-{str(year+1)[2:4]}'),
        ('SeasonSegment', ''),
        ('SeasonType', 'Regular Season'),
        ('ShotClockRange', ''),
        ('VsConference', ''),
        ('VsDivision', ''),
    )

    response = requests.get('https://stats.nba.com/stats/teamgamelogs', headers=headers, params=params, cookies=cookies)

    df = pd.DataFrame(response.json().get('resultSets')[0]['rowSet'])

    df.columns = response.json().get('resultSets')[0]['headers']

    df['Home'] = [x.count('vs') for x in df['MATCHUP']]

    df_less = df[['SEASON_YEAR', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID',
       'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M',
       'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST',
       'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'Home']]
    if less:
        return df_less
    else:
        return df



def GetAllSeasonsAndConcat():
  '''
  Scrapes all available seasons worth of game statistics from stats.nba.com

  Returns
  --------
  Pandas Dataframe with game data from all available seasons
  '''
    seasons = []
    for year in range(1996, 2018):
        seasons.append(GetSeason(year))
    return pd.concat(seasons)


#ESPN Standings data retrieval

def getWinPctDiff(year, AllCols = False):
  '''
  Scrapes Standings data with Home and Away records from ESPN.com for the season provided in the year parameter.
  Creates new columns Home Record, Home Win Percent, Away Record, Away Win Percent and Win Percent Difference.
  Returns dataframe with the added columns.

  Parameters
  -------------
  year - {int} - integer denoting which season of data to scrape

  AllCols - {boolean} - Optional boolean, if true, the returned dataframe will include some more exotic columns

  Returns
  -------------
  Pandas DataFrame with the standings and win percent difference for home and away for whichever season selected with the parameter year
  '''

    if year == 2019:
        HTML = pd.read_html('https://www.espn.com/nba/standings/_/group/league')
    else:
        HTML = pd.read_html(f'https://www.espn.com/nba/standings/_/season/{year}/group/league')
    if year <=2015:
        result = pd.DataFrame(HTML[0]['W'][2:32]).reset_index(drop = True)
        result['0'] = [x.strip('z --y --x --') for x in result['W']]
        result = pd.DataFrame(result['0']).join(HTML[3])
    else:
        result = pd.DataFrame(HTML[0]['W'][0].split('--')[1:31])
        result = result.join(HTML[3])

    result['HOME_LIST'] = result['HOME'].str.split('-')
    result.loc[:, 'HOME_WIN_PCT'] = result.HOME_LIST.map(lambda x:int(x[0])/(int(x[0])+int(x[1])))
    result['AWAY_LIST'] = result['AWAY'].str.split('-')
    result.loc[:, 'AWAY_WIN_PCT'] = result.AWAY_LIST.map(lambda x:int(x[0])/(int(x[0])+int(x[1])))
    result['win_pct_diff'] = result['HOME_WIN_PCT']-result['AWAY_WIN_PCT']
    result = result.rename(columns={0:'Team', '0':'Team'})
    result['year'] = year

    if AllCols:
        return result
    else:
        return result[['Team', 'win_pct_diff', 'year']]


def GetAllWinPctDiffSince(FirstYear):
  '''
  Scrapes all Standings data with Home and Away records from ESPN.com for the season provided in the year parameter.

  Parameters
  -------------
  FirstYear - {int} - year to begin scraping

  Returns
  -------------
  Pandas DataFrame with all of the standings and win percentage differences for every season starting with the season given with the parameter FirstYear
  '''
    seasons = []
    for year in range(FirstYear, 2020):
        seasons.append(getWinPctDiff(year))
    return pd.concat(seasons)


# ESPN attendance data retrieval

def getAttendance(year):
  '''
  Scrape a season worth of attendance data from ESPN

  Parameters
  -------------
  year - {int} - the year of attendance statistics to return

  Returns
  -------------
  Pandas DataFrame with the attendance statistics for the given year
  '''
    HTML = pd.read_html(f'http://www.espn.com/nba/attendance/_/year/{year}')
    df = HTML[0]
    df = df.drop([0, 1], axis = 0).reset_index(drop=True)
    df.columns = ['Rank', 'Team', 'Home_GMS', 'Tot_Attend', 'AVG_Attend', 'PCT_FILLED',
                   'Road_GMS', 'Road_AVG_Attend', 'Road_PCT_Filled', 'TOTAL_GMS',
                   'Overall_AVG_Attend', 'Overall_PCT_Filled']

    return df.iloc[0:30]

def getAllAttendance(firstyear):
  '''
  Scrapes all available attendance data from ESPN starting from the year provided

  Parameters
  -------------
  firstyear - {int} - year to begin scraping

  Returns
  -------------
  pandas DataFrame of all attendance data starting from firstyear
  '''
    if firstyear < 2001:
        firstyear = 2001
        print('attendance records only go back to 2001')
    result = []
    for year in range(firstyear, 2019):
        result.append(getAttendance(year))
    return pd.concat(result)


# ESPN Pace data retrieval

def PaceGetSeason(year):
  '''
  Scrapes a season of NBA Pace data from ESPN

  Parameters
  -------------
  year - {int} - season to scrape

  Returns
  -------------
  pandas Dataframe of all Pace data from the given season
  '''
    if year == 2019:
        ESPN = pd.read_html('http://www.espn.com/nba/hollinger/teamstats')
    else:
        ESPN = pd.read_html(f'http://www.espn.com/nba/hollinger/teamstats/_/sort/paceFactor/year/{year}')
    df = ESPN[0].drop([0], axis = 0).reset_index(drop=True)
    df.columns = df.iloc[0][:]
    df = df.drop([0], axis = 0).reset_index(drop=True)
    df['year'] = year
    return df


def PaceGetAllSeasons(firstyear):
  '''
  Scrapes all available Pace data from ESPN starting from the year provided

  Parameters
  -------------
  firstyear - {int} - year to begin scraping

  Returns
  -------------
  pandas DataFrame of all Pace data starting from firstyear

  '''
    if firstyear < 2003:
        firstyear = 2003
        print('Pace statistics only go back to 2003')
    seasons = []
    for year in range(firstyear, 2020):
        seasons.append(PaceGetSeason(year))
    return pd.concat(seasons)
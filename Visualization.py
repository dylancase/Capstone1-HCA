import matplotlib.pyplot as pyplot

def GraphZScores(df):
  '''
  Graphs (Bar) Z-scores of all relevant statistics in the passed in data frame

  Parameters
  ---------------
  df - {Pandas DataFrame} - DataFrame with all relevant columns found in statsToTest

  Returns
  ---------------
  None
  '''
    fig, ax = plt.subplots(figsize = (14, 10))
    statsToTest = ['FGA', 'FG_PCT', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST','TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS']
    y_data = []
    for stat in statsToTest:
        ztest, pval = stests.ztest(df[df['Home']==1][stat], x2 = df[df['Home']==0][stat], value = 0, alternative = 'two-sided')
        y_data.append(abs(ztest))
    ax.bar(statsToTest, y_data)
    ax.set_xlabel('NBA Statistics', size = 20)
    ax.set_ylabel('Z-Score', size = 20)
    fig.suptitle('Z-Score Stat Comparisons', size = 30)


def GraphStatsOverTime(statlist, df, save=False):
  '''
  Graphs a list of columns in df per year. In my use it graphs basketball statistics per season in the NBA

  Parameters
  --------------
  statlist - {list} - list of statistics to graph, must be columns of the dataframe

  df - {Pandas DataFrame} - a dataframe containing a column 'SEASON_YEAR' and the relevant columns in statlist

  save - {boolean} - Optional parameter, will save plot if True

  Returns
  --------------
  None
  '''
    fig, ax = plt.subplots(figsize = (14, 10))
    for col in statlist:
    ax.plot('SEASON_YEAR', col, data = df)
    plt.xticks(rotation = 45)
    ax.legend()
    ax.set_xlabel('Season', size = 20)
    ax.set_ylabel(' '.join(stats), size = 20)
    fig.suptitle(' '.join(stats) + ' Per NBA Season', size = 30)
    if save:
      plt.savefig(' '.join(stats) + 'PerSeason')
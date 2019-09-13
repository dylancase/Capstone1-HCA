import matplotlib.pyplot as pyplot

def GraphZScores(df):
  '''
  Graphs (Bar) Z-scores of all relevant statistics in the in df

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


def GraphTimeZonevsHCA(save = False):
    fig, ax = plt.subplots(figsize = (16, 10))
    ax.bar(['Pacific', 'Mountain','Central', 'Eastern'], TZWinPCT.groupby('Timezone').mean()['win_pct_diff'],
        color = ['purple', 'pink', 'yellow', 'green'], width = 0.5)
    ax.set_ylabel('WinPctDiff', size = 20)
    ax.set_xlabel('Timezone', size = 20)
    fig.suptitle('Avg Win Percent Difference by timezone', size = 30)
    if save:
      plt.savefig('WinPCTvsTZ')

def GraphHCAvsElevation(save = False):
    fig, ax = plt.subplots(figsize = (16,10))
    x_data, y_data = [], []
    for i, abb in enumerate(elev['Team_Abbreviation']):
        x_data.append(AllWinPct.groupby('Team_Abbreviation').agg({'win_pct_diff': 'mean'}).sort_values('win_pct_diff', ascending = False)['win_pct_diff'][abb])
        y_data.append(elev['Elevation'][i])
    ax.scatter(x_data, y_data)
    ax.set_xlabel('Win Percent Difference', size = 20)
    ax.set_ylabel('Elevation', size = 20)
    for i, label in enumerate(elev['Team_Abbreviation']):
        text = ax.annotate(label, (x_data[i]+.0015, y_data[i]))
        text.set_fontsize(20)
    fig.suptitle('Win Percent Difference vs Elevation', size = 40)
    if save:
      plt.savefig('WinPctDiffvsElevation')
import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats import weightstats as stests


def CalculateZScores(df):
  '''
  Function I built to calculate the Z scores of each statistic in statslist.

  Null hypothesis: Home and away statistics come from a population with the same mean

  Alternative hypothesis: Home and Away statistics come from separate populations with different means


  Parameters
  -------------
  df - {Pandas Dataframe} - dataframe with the relevant statistics

  Returns
  -------------
    A list of zscores for each statistic in statslist
  '''
    statslist = ['FGA', 'FG_PCT', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST','TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS']
    results = []
    for stat in statslist:
        homeMean = np.mean(df[df['Home']==1][stat])
        awayMean = np.mean(df[df['Home']==0][stat])
        OverallMean = np.mean(df[stat])
        ZscoreHome = (homeMean - OverallMean)/(np.std(df[stat])/np.sqrt(df.shape[0]))
        ZscoreAway = (OverallMean - awayMean)/(np.std(df[stat])/np.sqrt(df.shape[0]))
        results.append(stat + ' mean at home: ' + str(round(homeMean, 4))
                       + ' mean away: ' + str(round(awayMean, 4))
                      + ' Z score: ' + str(round(ZscoreHome, 4)))
    return results

def CalculateZScores2(df, alpha):
  '''
  Function to calculate Z scores, leveraging the built in stests.ztest. Ended up being a nice confirmation of the calculations I did in my original Zscore function

  Parameters
  -------------
  df - {Pandas DataFrame} -

  alpha - {float}  - Type 1 error rate

  Returns
  -------------
  A list of zscores for each statistic in statsToTest
  '''
    statsToTest = ['FGA', 'FG_PCT', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST','TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS']
    results = []
    for stat in statsToTest:
        ztest, pval = stests.ztest(df[df['Home']==1][stat], x2 = df[df['Home']==0][stat], value = 0, alternative = 'two-sided')
        results.append(str(stat) + ' z test: ' + str(ztest) + ' p-value: ' + str(pval) + ' significant for ' + str(stat) + ': ' + str(pval<alpha))
    return results


def CalculatePearsonC(df_HCA, df_stats, stat):
  '''

  Parameters
  -------------
  df_HCA - {Pandas DataFrame}

  df_stats - {Pandas DataFrame}

  stat - {string} - statistic to test for correlation with HCA


  Returns
  -------------
  Correlation coefficient and p-value
  '''
    return stats.pearsonr(df_HCA.groupby('year').mean()['win_pct_diff'], df_stats[stat][8:23])


def CalculatePearsonCorrelationAllStats(df_HCA,df_stats):
  '''
  Prints the correlation coefficient and p-value between HCA and every statistic in statsList
  Parameters
  -------------
  df_HCA - {Pandas DataFrame}

  df_stats - {Pandas DataFrame}

  Returns
  -------------
  None
  '''
    statslist = ['FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A',
          'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV',
          'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']
    for stat in statslist:
        correlation, pvalue = stats.pearsonr(df_HCA.groupby('year').mean()['win_pct_diff'], df_stats[stat][8:23])
        print(str(stat) + ' correlation: '+ str(correlation) + '  p-value: ' + str(pvalue) + ' significant: ' + str(pvalue < .05))
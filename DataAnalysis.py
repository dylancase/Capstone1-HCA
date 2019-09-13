import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats import weightstats as stests


def CalculateZScores(df):
    stats = ['FGA', 'FG_PCT', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST','TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS']
    results = []
    for stat in stats:
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
    statsToTest = ['FGA', 'FG_PCT', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST','TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS']
    results = []
    for stat in statsToTest:
        ztest, pval = stests.ztest(df[df['Home']==1][stat], x2 = df[df['Home']==0][stat], value = 0, alternative = 'two-sided')
        results.append(str(stat) + ' z test: ' + str(ztest) + ' p-value: ' + str(pval) + ' significant for ' + str(stat) + ': ' + str(pval<alpha))
    return results
import numpy as np

def overall(df):
    op = df[['City','Season','MatchNumber','Team1','Team2','WinningTeam']]
    return op

def City_year_list(df):
    years = df['Season'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    City = np.unique(df['City'].dropna().values).tolist()
    City.sort()
    City.insert(0, 'Overall')

    return years,City

def yearwise_analysis(df,Season,City,MatchNumber):
    op = df[['City','Season','MatchNumber','Teams','WinningTeam','Result']]
    if Season == "Overall" and City == "Overall" and MatchNumber =='Overall':
        temp = op

    if Season != "Overall" and City == "Overall" and MatchNumber =='Overall':
        temp = op[op['Season']==Season]

    if Season == "Overall" and City != "Overall" and MatchNumber =='Overall':
        temp = op[op['City']==City]
    
    if Season == "Overall" and City == "Overall" and MatchNumber !='Overall':
        temp = op[op['MatchNumber']==MatchNumber]

    if Season != "Overall" and City != "Overall" and MatchNumber =='Overall':
        temp = op[(op['Season']==Season) & (op['City']==City)]

    if Season != "Overall" and City == "Overall" and MatchNumber !='Overall':
        temp = op[(op['Season']==Season) & (op['MatchNumber']==MatchNumber)]

    if Season == "Overall" and City != "Overall" and MatchNumber !='Overall':
        temp = op[(op['City']==City) & (op['MatchNumber']==MatchNumber)]

    if Season != "Overall" and City != "Overall" and MatchNumber !='Overall':
        temp = op[(op['Season']==Season) & (op['City']==City) & (op['MatchNumber']==MatchNumber)]
    
    return temp



# def bat_vs_ball(df,batsman):

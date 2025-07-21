# import pandas as pd
# import plotly.express as px
# import streamlit as st

# df = pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
# season = pd.read_csv("IPL_Matches_2008_2022.csv")
# print(df)
# print(season)
# batsman = "YBK Jaiswal"
# target_season = 2022
# print(type(season))
# s1 = season[season["Season"] == target_season]
# df1 = df[df["batter"]==batsman]
# print(df1)
# print(s1)

# # fig = px.line(df, x='batter', y='batsman_run')
# # st.plotly_chart(fig)













from pandas import *
import plotly.express as px
import streamlit as st

# df = pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
# season_data = pd.read_csv("IPL_Matches_2008_2022.csv")
# print(df)
# print(season_data)
# batsman = "YBK Jaiswal"
# target_season = "2022"  # Rename the variable to avoid conflict
# print(type(target_season))
# s1 = season_data[season_data["Season"] == target_season]  # Filter using the correct variable
# df1 = df[df["batter"]==batsman]
# print(df1)
# print(s1)

# ID = s1['ID'].unique().tolist()
# ID.sort()
# print(ID[0])
# ID1 = ID[0]
# ID1 = str(ID1)
# print(type(ID))

# df2= df[df["batter"]==batsman ]
# df3 = df2[df2[df["ID"] == ID1]]
# print(df2)

# # fig = px.line(df, x='batter', y='batsman_run')
# # st.plotly_chart(fig)

# df = pd.read_csv("ball by ball.csv")
# batsman = "Wriddhiman Saha"
# target_season = 2022
# df1 = df[df["season"] == target_season]
# df2 = df1[df1["striker"] == batsman]
# print(df2)

# fig = px.line(df, x='bowler', y='runs_off_bat')
# st.plotly_chart(fig)
# team11 = input("Enter team 1 name : ")
# team12 = input("Enter team 2 name : ")
# team11 = "kkr"
# team12 = "csk"

# dfsq=read_csv("IPL_Ball_by_Ball_2008_2022.csv")
# team = dfsq['BattingTeam'].unique().tolist()
# team.insert(0, 'Overall')
team =['csk','dc','gt','kkr','lsg','mi','rcb','rr','srh','pk']
team11 = st.selectbox("Select team1",team)
team.remove(team11)
team12 = st.selectbox("Select team2",team)

x=team11+".csv"
t1 = read_csv(x)
# print(t1)
team1 = t1["player"].tolist()
# print(t11)

y=team12+".csv"
t2 = read_csv(y)
# print(t2)
team2 = t2["player"].tolist()
# print(t12)


dataset=read_csv('ball by ball.csv')
df=DataFrame(dataset)
def bbr(bat,ball):
  bbrun=df[(df['striker'] == bat) & (df['bowler'] == ball) ] ['runs_off_bat'].sum()
  bb2=(df['striker'] == bat) & (df['bowler'] == ball)
  bbball=bb2.sum()
  return bbrun, bbball

# t1='csk'
# t2='rcb'
# team1=['Ruturaj Gaikwad', 'Devon Conway', 'Shivam Dube', 'Ajinkya Rahane', 'Ambati Rayudu', 'MS Dhoni']
# team2=['Harshal Patel', 'Mohammed Siraj', 'Wayne Parnell', 'Vijaykumar Vyshak', 'Wanindu Hasaranga', 'Josh Hazlewood', 'Karn Sharma', 'David Willey', 'Akash Deep']



print("batter vs bowler (score, sr)")
print("----------------------------")
print("batter- ",team11," bowler- ",team12)
bbrun={'batter':[],
       'bowler':[],
       'runs':[],
       'balls':[],
       'strike rates':[]}
batr={'batter':[],
      'total':[]}
batsr={'batter':[],
       'strike rate':[]}
batrd=DataFrame(batr)
batsrd=DataFrame(batsr)
bbrund=DataFrame(bbrun)
for bat in team1:
  t=0
  t1s=0
  for ball in team2:
    r=bbr(bat,ball)
    if r is not None:
      a, b = r
      t+=a
      t1s+=b
      if(b>6):
        c=(a/b)*100
        nr={'batter':bat,'bowler':ball,'runs':a,'balls':b,'strike rates':round(c,2)}
        bbrund = concat([bbrund, DataFrame([nr])], ignore_index=True)
  if t>20:
    c=(t/t1s)*100
    nr={'batter': bat,'total':t}
    batrd = concat([batrd, DataFrame([nr])], ignore_index=True)
    nr={'batter':bat,'strike rate':round(c,2)}
    batsrd = concat([batsrd, DataFrame([nr])], ignore_index=True)
bbrund['runs']=bbrund['runs'].astype(int)
bbrund['balls']=bbrund['balls'].astype(int)
bbrund= bbrund.sort_values(by=['runs'],ascending=False)
batrd= batrd.sort_values(by=['total'],ascending=False)
batsrd= batsrd.sort_values(by=['strike rate'],ascending=False)
batrd['total']=batrd['total'].astype(int)
print(bbrund.head(10))
# print("-----------------------------")
# print(batrd)
# print("-----------------------------")
# print(batsrd)
st.table(bbrund)
# selected_team1 = st.sidebar.selectbox("Select Year",team1)
# selected_team2 = st.sidebar.selectbox("Select Year",team2)





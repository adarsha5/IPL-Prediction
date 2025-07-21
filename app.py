import streamlit as st
import pandas as pd
import helper
import plotly.express as px
import numpy as np

df = pd.read_csv("Match2023.csv")
ball_by_ball = pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
#region_df = pd.read_csv("noc_regions.csv")

#df = preprocessor.preprocess(df,region_df)
st.sidebar.title("Indian Premier League (IPL) Analysis")
st.sidebar.image('https://www.vhv.rs/file/max/29/294049_ipl-logo-png.png')
user_menu=st.sidebar.radio(
    'Select an Option',
    ('OverAll Analysis','Batsman vs Bowler','Top Player Analysis','Player Wise Analysis','Predict Win Rate')
)
def bbw(ball,bat):
    bb=(df['bowler'] == ball) & (df['player_dismissed']==bat)
    occur = bb.sum()
    return occur


def bbr(bat,ball):
    bbrun=df[(df['striker'] == bat) & (df['bowler'] == ball) ] ['runs_off_bat'].sum()
    bb2=(df['striker'] == bat) & (df['bowler'] == ball)
    bbball=bb2.sum()
    return bbrun, bbball

def bvr(bat,venue):
    vrun=df[(df['striker'] == bat) & (df['venue'] == venue) ] ['runs_off_bat'].sum()
    vm=df[(df['striker'] == bat) & (df['venue'] == venue)]['match_id'].nunique()
    return vrun,vm

def bvw(ball,venue):
    vch2=(df['bowler'] == ball) & (df['player_dismissed']!=0) & (df['venue'] == venue)
    vplay=df[(df['bowler'] == ball) & (df['venue'] == venue)]['match_id'].nunique()
    vwic = vch2.sum()
    return vwic,vplay

if user_menu=='OverAll Analysis':
    st.sidebar.header("OverAll Analysis")
    
    batter = ball_by_ball['batter'].unique().shape[0]
    bowler = ball_by_ball['bowler'].unique().shape[0]
    battingTeam = ball_by_ball['BattingTeam'].unique().shape[0]
    season = df['Season'].unique().shape[0]
    venue = df['match_venue_stadium'].unique().shape[0]
    city = df['City'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("BatsMan")
        st.title(batter)
    with col2:
        st.header("Bowler")
        st.title(bowler)
    with col3:
        st.header("Batting Team")
        st.title(battingTeam)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Season")
        st.title(season)
    with col2:
        st.header("Venue")
        st.title(venue)
    with col3:
        st.header("City")
        st.title(city)
    years , city =helper.City_year_list(df)
    st.header(" ")
    st.header("OverAll Analysis over 2008 - 2023")

    # selected_country = st.sidebar.selectbox("Select team1", Team1)
    # selected_country = st.sidebar.selectbox("Select team2", Team2)
    # winning_team = st.sidebar.selectbox("Select winning team", Winning_Team)
    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_city = st.sidebar.selectbox("Select City",city)
    selected_match = st.sidebar.selectbox("Select Match",['Overall','Final','1st Semi-Final','2nd Semi-Final','Qualifier 1','Qualifier 2','Eliminator'])

    matches=helper.yearwise_analysis(df,selected_year,selected_city,selected_match)
    # if selected_match != 'Overall':
    #     st.table(One_match)
    # else:
    st.table(matches)


if user_menu=='Venue Analysis':
    batter = ball_by_ball['batter'].unique().shape[0]
    bowler = ball_by_ball['bowler'].unique().shape[0]
    battingTeam = ball_by_ball['BattingTeam'].unique().shape[0]
    season = df['Season'].unique().shape[0]
    venue = df['match_venue_stadium'].unique().shape[0]
    city = df['City'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("BatsMan")
        st.title(batter)
    with col2:
        st.header("Bowler")
        st.title(bowler)
    with col3:
        st.header("Batting Team")
        st.title(battingTeam)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Season")
        st.title(season)
    with col2:
        st.header("Venue")
        st.title(venue)
    with col3:
        st.header("City")
        st.title(city)

    # df = pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
    # season = pd.read_csv("IPL_Matches_2008_2022.csv")
    # # print(df)
    # batsman = "YBK Jaiswal"
    # # for index,row in df.iterrows():
    # #     df=df.drop_duplicates(['season'])['season'].value_counts().reset_index().sort_values('Year')
    # #     fig = px.line(df, x='batsman_run', y='batter')
    # #     st.plotly_chart(fig)

    # batsman = "YBK Jaiswal"
    # season = '2020'
    # s1 = season[season["Season"] == season]
    # df1 = df[df["batter"]==batsman ]
    # # print(df1)
    # fig = px.line(df1, x='batsman_run', y='bowler')
    # st.plotly_chart(fig)



    
    # df = pd.read_csv("IPL_Ball_by_Ball_2008_2022.csv")
    # season_data = pd.read_csv("IPL_Matches_2008_2022.csv")
    # print(df)
    # print(season_data)
    # batsman = "YBK Jaiswal"
    # target_season = "2022"  # Rename the variable to avoid conflict
    # print(type(target_season))
    # s1 = season_data[season_data["Season"] == target_season]


    # years = df['Season'].unique().tolist()
    # years.sort()
    # df1 = df[df["batter"]==batsman]
    # print(df1)
    # print(s1)


    # df = pd.read_csv("ball by ball.csv")
    # batsman = "YBK Jaiswal"
    # target_season = "2022"
    # df1 = df[df["striker"]==batsman & df["season"] == target_season]['runs_off_bat'].sum() 
    # fig = px.line(df, x='bowler', y='runs_off_bat')
    # st.plotly_chart(fig)



    # df = pd.read_csv("ball by ball.csv")
    # batsman = "Wriddhiman Saha"
    # target_season = 2022
    # df1 = df[df["season"] == target_season]
    # df2 = df1[df1["striker"] == batsman]
    # fig = px.line(df, x='venue', y='runs_off_bat')
    # st.plotly_chart(fig)


if user_menu=='Player Wise Analysis':
    st.title("Player Details")
    gr = pd.read_csv("final_batting.csv")
    battters = gr['Player'].unique().tolist()
    battters.remove("Faf Du Plessis")
    battters.insert(0,' ')
    battters = st.selectbox("Select player",battters)
    if battters != ' ':
        xy = gr[gr['Player']==battters]
        st.header(f"About {battters}")

        
        # gr = pd.read_csv("ipl_players_info.csv")
        # xy = gr[gr['player_name']==battters]
        # st.image('')


        player_info = pd.read_csv("ipl_players_info.csv")
        # batters = player_info['player_name'].unique().tolist()
        # selected_batter = st.selectbox("Select player", batters)
        selected_player_info = player_info[player_info['player_name'] == battters]

        if not selected_player_info.empty:
            image_url = selected_player_info["image_url"].values[0]

            image_url = str(image_url)

            st.image(image_url ,width= 200)
        else:
            st.write("Player not found.")
        
        dob = selected_player_info["dob"].values[0]
        st.header("Date Of Birth - ")
        st.write(dob)
        st.header("Gender - ")
        st.write("Male")
        fig = px.line(xy, x='year', y='Runs')
        st.plotly_chart(fig)
        

if user_menu == "Top Player Analysis":
    from pandas import *
    import streamlit as st
    # import plotly.express as px
    dataset=read_csv('ball by ball.csv')
    df=DataFrame(dataset)
    df.fillna(0, inplace=True)
    d1=read_csv('csk.csv')
    d2=read_csv('mi.csv')
    d3=read_csv('gt.csv')
    d4=read_csv('pk.csv')
    d5=read_csv('rr.csv')
    d6=read_csv('kkr.csv')
    d7=read_csv('srh.csv')
    d8=read_csv('lsg.csv')
    d9=read_csv('dc.csv')
    d10=read_csv('rcb.csv')
    team_dataframes = {
        "csk": DataFrame(d1),
        "mi": DataFrame(d2),
        "gt": DataFrame(d3),
        "pk": DataFrame(d4),
        "rr": DataFrame(d5),
        "kkr": DataFrame(d6),
        "srh": DataFrame(d7),
        "lsg": DataFrame(d8),
        "dc": DataFrame(d9),
        "rcb": DataFrame(d10)
    }
    # global df
    venue_list= df.loc[df['season'] == 2023, 'venue'].unique().tolist()
    venue_list.insert(0,' ')
    # venue="M Chinnaswamy Stadium"
    # print(venue_list)
    # print(df)
    st.title("Top Player Analysis")
    team =[' ','csk','dc','gt','kkr','lsg','mi','rcb','rr','srh','pk']
    t1 = st.selectbox("Select team1",team)
    if t1 != ' ':
        team.remove(t1)
    t2 = st.selectbox("Select team2",team)
    venue = st.selectbox("Select venue",venue_list)
    # st.write(venue_list)
    
    if t1 != ' ' and t2 != ' ' and venue != ' ':

        team1=[]
        tbat1=[]
        tball1=[]
        tall1=[]
        twk1=[]
        if t1 in team_dataframes:
            t1d = team_dataframes[t1]
            team1=t1d['player'].tolist()
            print(team1)
        for i, row in t1d.iterrows():
            if row['speciality']=="batter":
                tbat1.append(row['player'])
            elif row['speciality']=="bowler":
                tball1.append(row['player'])
            elif row['speciality']=="wk":
                twk1.append(row['player'])
            else:
                tall1.append(row['player'])
        # print(tbat1)
        # print(tball1)
        # print(tall1)
        # print(twk1)


        tbat2=[]
        tball2=[]
        tall2=[]
        twk2=[]
        if t2 in team_dataframes:
            t2d = team_dataframes[t2]
            team2=t2d['player'].tolist()
            print(team2)
        for i, row in t2d.iterrows():
            if row['speciality']=="batter":
                tbat2.append(row['player'])
            elif row['speciality']=="bowler":
                tball2.append(row['player'])
            elif row['speciality']=="wk":
                twk2.append(row['player'])
            else:
                tall2.append(row['player'])
        # print(tbat2)
        # print(tball2)
        # print(tall2)
        # print(twk2)

        


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
        # print(bbrund.head(10))
        # print(batrd)
        # batsrd

        # print("batter- ",t2," bowler- ",t1)
        bbrun2={'batter':[],
            'bowler':[],
            'runs':[],
            'balls':[],
            'strike rates':[]}
        bbrund2=DataFrame(bbrun2)
        for bat in team2:
            t=0
            t1s=0
            for ball in team1:
                r=bbr(bat,ball)
                if r is not None:
                    a, b = r
                t+=a
                t1s+=b
                if(b>6):
                    c=(a/b)*100
                    nr={'batter':bat,'bowler':ball,'runs':a,'balls':b,'strike rates':round(c,2)}
                    bbrund2 = concat([bbrund2, DataFrame([nr])], ignore_index=True)
            if t>20:
                c=(t/t1s)*100
                nr={'batter': bat,'total':t}
                batrd = concat([batrd, DataFrame([nr])], ignore_index=True)
                nr={'batter':bat,'strike rate':round(c,2)}
                batsrd = concat([batsrd, DataFrame([nr])], ignore_index=True)
        bbrund2['runs']=bbrund2['runs'].astype(int)
        bbrund2['balls']=bbrund2['balls'].astype(int)
        bbrund2= bbrund2.sort_values(by=['runs'],ascending=False)
        batrd= batrd.sort_values(by=['total'],ascending=False)
        batsrd= batsrd.sort_values(by=['strike rate'],ascending=False)
        batrd['total']=batrd['total'].astype(int)
        batrd['points'] = batrd['total'].rank(method='dense', ascending=False).apply(lambda x: 26-x if x <= 25 else 0)
        batsrd['points'] = batsrd['strike rate'].rank(method='dense', ascending=False).apply(lambda x: 26-x if x <= 25 else 0)
        batrd['points']=batrd['points'].astype(int)
        batsrd['points']=batsrd['points'].astype(int)
        # print(bbrund2)
        # print(batrd)
        # batsrd

        # print("bowler vs batter")
        # print("----------------")
        # print("batter- ",t2," bowler- ",t1)
        bbwic={'bowler':[],
            'dismissed':[],
            'times':[]}
        ballr={'bowler':[],
            "2's":[],
            "1's":[],
            'multiple wic':[]}
        ballrd=DataFrame(ballr)
        bbwicd=DataFrame(bbwic)
        for ball in team1:
            t=0
            t1s=0
            for bat in team2:
                a=bbw(ball,bat)
                if a>0:
                    if a>1:
                        t1s+=1
                else:
                    t+=1
                if(a>1):
                    nr={'bowler':ball,'dismissed':bat,'times':a}
                    bbwicd = concat([bbwicd, DataFrame([nr])], ignore_index=True)
            if t>1 or t1s>0:
                nr={'bowler': ball,'multiple wic':(t+t1s),"1's":t,"2's":t1s}
                ballrd = concat([ballrd, DataFrame([nr])], ignore_index=True)
        bbwicd['times']=bbwicd['times'].astype(int)
        # bbwicd['matches']=bbwicd['matches'].astype(int)
        bbwicd= bbwicd.sort_values(by='times',ascending=False)
        ballrd= ballrd.sort_values(by="2's",ascending=False)
        ballrd["2's"]=ballrd["2's"].astype(int)
        ballrd["1's"]=ballrd["1's"].astype(int)
        ballrd["multiple wic"]=ballrd["multiple wic"].astype(int)
        # print(bbwicd)
        # print("bowlers dismissed n unique batters more than 2 and 1 time")
        # ballrd


        # print("batter- ",t1," bowler- ",t2)
        bbwic2={'bowler':[],
            'dismissed':[],
            'times':[]}
        bbwicd2=DataFrame(bbwic2)
        for ball in team2:
            t=0
            t1s=0
            for bat in team1:
                a =bbw(ball,bat)
                if a>0:
                    if a>1:
                        t1s+=1
                else:
                    t+=1
                if(a>1):
                    nr={'bowler':ball,'dismissed':bat,'times':a}
                    bbwicd2 = concat([bbwicd2, DataFrame([nr])], ignore_index=True)
            if (t>1) or (t1s>0):
                nr={'bowler': ball,'multiple wic':(t+t1s),"1's":t,"2's":t1s}
                ballrd = concat([ballrd, DataFrame([nr])], ignore_index=True)
        bbwicd2['times']=bbwicd2['times'].astype(int)
        bbwicd2= bbwicd2.sort_values(by='times',ascending=False)
        ballrd= ballrd.sort_values(by="2's",ascending=False)
        ballrd["2's"]=ballrd["2's"].astype(int)
        ballrd["1's"]=ballrd["1's"].astype(int)
        ballrd["multiple wic"]=ballrd["multiple wic"].astype(int)
        ballrd['point']=ballrd["2's"]*5+ballrd["1's"]*2
        # print(bbwicd2.head(5))
        # ballrd


        # print("venue vs batter")
        # print("-----------------")
        # print(t1)
        bvrun={'batter':[],
            'runs':[],
            'matches':[],
            'venue':[]}
        bva={'batter':[],
            'avg. run':[]}
        bvrund=DataFrame(bvrun)
        bvad=DataFrame(bva)
        for bat in team1:
            r= bvr(bat,venue)
            if r is not None:
                a, b = r
                if(b>0):
                    nr={'batter':bat,'runs':a,'matches':b,'venue':venue}
                    bvrund = concat([bvrund, DataFrame([nr])], ignore_index=True)
                    nr={'batter':bat,'avg. run':int(a/b)}
                    bvad = concat([bvad, DataFrame([nr])], ignore_index=True)
        bvrund['runs']=bvrund['runs'].astype(int)
        bvrund['matches']=bvrund['matches'].astype(int)
        bvad['avg. run']=bvad['avg. run'].astype(int)
        bvrund= bvrund.sort_values(by='runs',ascending=False)
        bvad= bvad.sort_values(by='avg. run',ascending=False)

        # print(bvrund)
        # bvad

        # print(t2)
        bvrun2={'batter':[],
            'runs':[],
            'balls':[],
            'venue':[]}
        bvrund2=DataFrame(bvrun2)
        for bat in team2:
            r= bvr(bat,venue)
            if r is not None:
                a, b = r
                if(b>0):
                    nr={'batter':bat,'runs':a,'balls':b,'venue':venue}
                    bvrund2 = concat([bvrund2, DataFrame([nr])], ignore_index=True)
                    nr={'batter':bat,'avg. run':int(a/b)}
                    bvad = concat([bvad, DataFrame([nr])], ignore_index=True)
                    bvad['avg. run']=bvad['avg. run'].astype(int)
                    bvrund2['runs']=bvrund2['runs'].astype(int)
                    bvrund2['balls']=bvrund2['balls'].astype(int)
        bvrund2= bvrund2.sort_values(by='runs',ascending=False)
        bvad= bvad.sort_values(by='avg. run',ascending=False)
        bvad['points'] = bvad['avg. run'].rank(method='dense', ascending=False).apply(lambda x: 26-x if x <= 25 else 0)
        bvad['points']=bvad['points'].astype(int)
        # print(bvrund2)
        # bvad

        # print("venue vs bowler")
        # print("-----------------")
        # print(t1)
        bvwic={'bowler':[],
            'matches':[],
            'wickets':[],
            'avg':[]}
        bvwicd=DataFrame(bvwic)
        for ball in team1:
            r= bvw(ball,venue)
            if r is not None:
                a, b = r
                if(a!=0):
                    nr={'bowler':ball,'matches':b,'wickets':a,'avg':round((a/b),1)}
                    bvwicd = concat([bvwicd, DataFrame([nr])], ignore_index=True)
                    bvwicd['matches']=bvwicd['matches'].astype(int)
                    bvwicd['wickets']=bvwicd['wickets'].astype(int)
        bvwicd= bvwicd.sort_values(by='avg',ascending=False)
        # bvwicd.head(5)


        # print(t2)
        for ball in team2:
            r= bvw(ball,venue)
            if r is not None:
                a, b = r
                if(a!=0):
                    nr={'bowler':ball,'matches':b,'wickets':a,'avg':round((a/b),1)}
                    bvwicd = concat([bvwicd, DataFrame([nr])], ignore_index=True)
                    bvwicd['matches']=bvwicd['matches'].astype(int)
                    bvwicd['wickets']=bvwicd['wickets'].astype(int)
        bvwicd= bvwicd.sort_values(by='avg',ascending=False)
        bvwicd['points'] = bvwicd['avg'].rank(method='dense', ascending=False).apply(lambda x: 26-x if x <= 25 else 0)
        bvwicd['points']=bvwicd['points'].astype(int)
        # bvwicd

        # print("dismissal vs batter")
        # print("----------------")
        # print("batter- ",t1," bowler- ",t2)
        db={'batter':[],
            "1's":[],
            "2's":[],
            'multiple':[]}
        dbd=DataFrame(db)
        for bat in team1:
            t=0
            t1s=0
            for ball in team2:
                a=bbw(ball,bat)
                if a>0:
                    if a>1:
                        t1s+=1
                else:
                    t+=1
            if t>1 or t1s>0:
                nr={'batter':bat,"1's":t,"2's":t1s,"multiple":t+t1s}
                dbd = concat([dbd, DataFrame([nr])], ignore_index=True)
        dbd["1's"]=dbd["1's"].astype(int)
        dbd["2's"]=dbd["2's"].astype(int)
        dbd["multiple"]=dbd["multiple"].astype(int)
        # bbwicd['matches']=bbwicd['matches'].astype(int)
        dbd= dbd.sort_values(by="2's",ascending=False)
        # dbd

        # print("dismissal vs batter")
        # print("----------------")
        # print("batter- ",t2," bowler- ",t1)
        for bat in team2:
            t=0
            t1s=0
            for ball in team1:
                a=bbw(ball,bat)
                if a>0:
                    if a>1:
                        t1s+=1
                else:
                    t+=1
            if t>1 or t1s>0:
                nr={'batter':bat,"1's":t,"2's":t1s,"multiple":t+t1s}
                dbd = concat([dbd, DataFrame([nr])], ignore_index=True)
        dbd["1's"]=dbd["1's"].astype(int)
        dbd["2's"]=dbd["2's"].astype(int)
        dbd["multiple"]=dbd["multiple"].astype(int)
        # bbwicd['matches']=bbwicd['matches'].astype(int)
        dbd= dbd.sort_values(by="2's",ascending=False)
        dbd['points']=dbd["2's"]*5+dbd["1's"]*2
        dbd["points"]=dbd["points"].astype(int)
        # dbd

        dbd=dbd.drop(["1's","multiple"],axis=1)
        merged_data = merge(batsrd, batrd, on='batter',how="outer",suffixes=('x', 'y'))
        # merged_data
        merged_data = merge(merged_data, bvad, on='batter',how="outer")
        merged_data = merge(merged_data, dbd, on='batter',how="outer",suffixes=('z', 'p'))
        merged_data.fillna(0, inplace=True)
        merged_data['point'] = merged_data['pointsx'] + merged_data['pointsy']+merged_data['pointsz']-merged_data['pointsp']
        merged_data=merged_data.drop(['pointsx','pointsy','pointsz','pointsp'],axis=1)
        merged_data= merged_data.sort_values(by="point",ascending=False)
        # merged_data

        merged_data=merged_data.drop(["strike rate","total","avg. run","2's"],axis=1)

        # merged_data.drop(merged_data[merged_data['batter'].isin(tall+tball1+tball2)].index,inplace=True)
        batter_rank=merged_data[merged_data['batter'].isin(tbat1+tbat2)]
        print(batter_rank)
        wk_rank=merged_data[merged_data['batter'].isin(twk1+twk2)]
        wk_rank.rename(columns = {'batter':'Wicket Kipper'}, inplace = True) 
        print(wk_rank)

        tall=tall1+tall2
        ttall = merged_data[merged_data['batter'].isin(tall)]
        # ttall

        ttall=ttall.rename(columns={'batter':'all rounder'})

        mdball = merge(bvwicd, ballrd, on='bowler',how="outer")
        mdball.fillna(0, inplace=True)
        mdball['point1'] = mdball['points'] + mdball['point']
        mdball=mdball.drop(['points','point',"matches","wickets","avg","2's","1's","multiple wic"],axis=1)
        mdball= mdball.sort_values(by="point1",ascending=False)
        # mdball

        bowler_rank=mdball[mdball['bowler'].isin(tball1+tball2)]
        print(bowler_rank)

        tallb=mdball[mdball['bowler'].isin(tall)]
        tallb=tallb.rename(columns={'bowler':'all rounder'})
        # tallb

        allrounder=merge(tallb, ttall, on='all rounder',how="outer")
        allrounder.fillna(0, inplace=True)
        allrounder["point"]=allrounder["point1"]+allrounder["point"]
        allrounder=allrounder.drop(['point1'],axis=1)
        allrounder_rank= allrounder.sort_values(by="point",ascending=False)
        print(allrounder_rank)

        st.table(allrounder_rank)
        st.table(batter_rank)
        st.table(bowler_rank)
        st.table(wk_rank)


if user_menu == "Batsman vs Bowler":
    st.title("Batsman vs bowler ")
    team =[' ','csk','dc','gt','kkr','lsg','mi','rcb','rr','srh','pk']
    team11 = st.selectbox("Select Bating team",team)
    if team11 != ' ':
        team.remove(team11)
    # team.remove(team11)
    team12 = st.selectbox("Select Bowling team",team)
    if team11 != ' ' and team12 != ' ':
        x=team11+".csv"
        t1 = pd.read_csv(x)
        # print(t1)
        team1 = t1["player"].tolist()
        # print(t11)

        y=team12+".csv"
        t2 = pd.read_csv(y)
        # print(t2)
        team2 = t2["player"].tolist()
        # print(t12)


        dataset=pd.read_csv('ball by ball.csv')
        df=pd.DataFrame(dataset)
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
        batrd=pd.DataFrame(batr)
        batsrd=pd.DataFrame(batsr)
        bbrund=pd.DataFrame(bbrun)
        from pandas import *
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


if user_menu == "Predict Win Rate":
    st.title("Win Rate Prediction")
    match = pd.read_csv('match.csv')
    delivery = pd.read_csv('delivery.csv')
    # (match.head())
    # (delivery.head())
    total_score_df=delivery.groupby(['match_id', 'innings_no'])['total_runs'].sum().reset_index()
    # (total_score_df)
    total_score_df = total_score_df[total_score_df['innings_no'] == 1]
    # (total_score_df)
    match_df = match.merge(total_score_df[['match_id','total_runs']],left_on='id',right_on='match_id')
    # (match_df['team1'].unique())
    teams = [
        'Sunrisers Hyderabad',
        'Mumbai Indians',
        'Royal Challengers Bangalore',
        'Kolkata Knight Riders',
        'Punjab Kings',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Delhi Capitals',
        'Gujarat Titans',
        'Lucknow Super Giants',
    ]

    match_df['team1'] = match_df['team1'].str.replace('Delhi Daredevils','Delhi Capitals')
    match_df['team2'] = match_df['team2'].str.replace('Delhi Daredevils','Delhi Capitals')

    match_df['team1'] = match_df['team1'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
    match_df['team2'] = match_df['team2'].str.replace('Deccan Chargers','Sunrisers Hyderabad')


    match_df['team1'] = match_df['team1'].str.replace('Kings XI Punjab','Punjab Kings')
    match_df['team2'] = match_df['team2'].str.replace('Kings XI Punjab','Punjab Kings')

    match_df = match_df[match_df['team1'].isin(teams)]
    match_df = match_df[match_df['team2'].isin(teams)]

    match_df['dl_applied'].value_counts()
    match_df = match_df[match_df['dl_applied'] == 0]
    match_df = match_df[['match_id','city','winner','total_runs','team1','team2']]
    match_df.merge(delivery,on='match_id')
    delivery_df = match_df.merge(delivery,on='match_id')
    delivery_df = delivery_df[delivery_df['innings_no'] == 2]
    delivery_df.groupby('match_id')['total_runs_y'].cumsum()
    delivery_df['current_score'] =delivery_df.groupby('match_id')['total_runs_y'].cumsum()
    # delivery_df['total_runs_x'] - delivery_df['current_score']

    delivery_df['current_score'] =delivery_df.groupby('match_id')['total_runs_y'].cumsum()
    delivery_df['balls_left'] = 126 - (delivery_df['over_number']*6 + delivery_df['ball_number'])
    delivery_df['runs_left'] = delivery_df['total_runs_x'] - delivery_df['current_score']
    delivery_df['crr'] = (delivery_df['current_score']*6)/(120 - delivery_df['balls_left'])
    delivery_df['rrr'] = (delivery_df['runs_left']*6)/delivery_df['balls_left']
    def result(row):
        return 1 if row['team1'] == row['winner'] else 0

    delivery_df['result'] = delivery_df.apply(result,axis=1)
    final_df = delivery_df[['team1','team2','city','runs_left','balls_left','current_innings_wickets','total_runs_x','crr','rrr','result']]
    final_df = final_df.sample(final_df.shape[0])
    final_df.isnull().sum()
    final_df.dropna(inplace=True)
    final_df = final_df[final_df['balls_left'] != 0] 
    X = final_df.iloc[:,:-1]
    y = final_df.iloc[:,-1]
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder

    # Define the ColumnTransformer
    trf = ColumnTransformer([
        ('trf', OneHotEncoder(drop='first'), ['team1', 'team2', 'city'])
    ], remainder='passthrough')

    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline

    pipe = Pipeline(steps=[
        ('step1',trf),
        ('step2',LogisticRegression(solver='liblinear'))
        
    ])

    pipe.fit(X_train,y_train)
    y_pred = pipe.predict(X_test)
    # team1="Royal Challengers Bangalore"
    # team2="Delhi Capitals"
    # selected_city="Ahmedabad"
    # runs_left= "105"
    # balls_left="85.0"
    # current_innings_wickets="9"
    # target="154.0"
    # crr="8.40"
    # rrr="7.411765"
    # input_df =pd.DataFrame({'team1':[team1],'team2':[team2],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'current_innings_wickets':[current_innings_wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    # # y_pred1 = pipe.predict(input_df)
    # # print(y_pred1)
    # print(pipe.predict_proba(input_df))

    # import gradio as gr
    teams = ['Sunrisers Hyderabad','Mumbai Indians','Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Punjab Kings',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals',
    'Gujarat Titans',
    'Lucknow Super Giants']
    teams.insert(0,' ')
    cities = ['Ahmedabad', 'Chennai', 'Mumbai', 'Bengaluru', 'Kolkata', 'Delhi',
        'Dharamsala', 'Hyderabad', 'Lucknow', 'Jaipur', 'Chandigarh',
        'Guwahati', 'Navi Mumbai', 'Pune', 'Dubai', 'Sharjah', 'Abu Dhabi',
        'Visakhapatnam', 'Indore', 'Bangalore', 'Raipur', 'Ranchi',
        'Cuttack', 'Nagpur', 'Johannesburg', 'Centurion', 'Durban',
        'Bloemfontein', 'Port Elizabeth', 'Kimberley', 'East London',
        'Cape Town']
    cities.insert(0,' ')
    batting_team = st.selectbox("Select first batting team",teams)
    if batting_team != ' ':
        teams.remove(batting_team)
    bowling_team = st.selectbox("Select chasing team",teams)
    host_city = st.selectbox("Select host city",cities)
    target = st.number_input('Target',step=1)
    score = st.number_input('Score',step=1)
    overs = st.number_input('Overs completed' ,min_value=1, max_value=20,step=1)
    current_innings_wickets = st.number_input('Wickets out', min_value=0, max_value=9,step=1)
    if score != 0.00 and overs != 0.00:
        runs_left = target - score
        balls_left = 120 - (overs*6)
        current_innings_wickets = 10 -current_innings_wickets
        crr = score / overs
        rrr = (runs_left * 6) / balls_left


        input_df = pd.DataFrame({
            'team1': [batting_team],
            'team2': [bowling_team],
            'city': [host_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'current_innings_wickets': [current_innings_wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]})
        y_pred = pipe.predict(X_test)
        r=pipe.predict_proba(input_df)
        # st.write(r)
        a=round(r[0][0]*100,2)
        b=round(r[0][1]*100,2)
        a=str(a)
        b=str(b)
        loss = "1. win rate of "+bowling_team+" "+a+"%"
        win = "2. win rate of "+batting_team+" "+b+"%"
        st.write(loss)
        st.write(win)

        import streamlit as st
        import matplotlib.pyplot as plt
        import numpy as np

        # Define the data
        y = []
        y.append(a)
        y.append(b)
        mylabels = [bowling_team, batting_team]
        explode=(0.1,0)

        # Create the pie chart
        fig, ax = plt.subplots()
        ax.pie(y, labels=mylabels, shadow= True,startangle=90,explode=explode)
        plt.title('Win Rates')

        # Display the pie chart in Streamlit
        st.pyplot(fig)

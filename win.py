import numpy as np
import pandas as pd
import streamlit as st
i=1
if i==1 :
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

    cities = ['Ahmedabad', 'Chennai', 'Mumbai', 'Bengaluru', 'Kolkata', 'Delhi',
        'Dharamsala', 'Hyderabad', 'Lucknow', 'Jaipur', 'Chandigarh',
        'Guwahati', 'Navi Mumbai', 'Pune', 'Dubai', 'Sharjah', 'Abu Dhabi',
        'Visakhapatnam', 'Indore', 'Bangalore', 'Raipur', 'Ranchi',
        'Cuttack', 'Nagpur', 'Johannesburg', 'Centurion', 'Durban',
        'Bloemfontein', 'Port Elizabeth', 'Kimberley', 'East London',
        'Cape Town']
    batting_team = st.selectbox("Select first batting team",teams)
    bowling_team = st.selectbox("Select chasing team",teams)
    host_city = st.selectbox("Select host city",cities)
    target = st.number_input('Target')
    score = st.number_input('Score')
    overs = st.number_input('Overs completed')
    current_innings_wickets = st.number_input('Wickets out')
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
# # Define the function to predict probabilities
# def predict_probability(batting_team, bowling_team, host_city, target, score, overs, wickets_out):
#     # Calculate remaining parameters like runs_left, balls_left, crr, rrr
#     runs_left = target - score
#     balls_left = 120 - (overs*6)
#     current_innings_wickets = 10 - wickets_out
#     crr = score / overs
#     rrr = (runs_left * 6) / balls_left

#     # Create input DataFrame
#     input_df = pd.DataFrame({
#         'team1': [batting_team],
#         'team2': [bowling_team],
#         'city': [host_city],
#         'runs_left': [runs_left],
#         'balls_left': [balls_left],
#         'current_innings_wickets': [current_innings_wickets],
#         'total_runs_x': [target],
#         'crr': [crr],
#         'rrr': [rrr]})

#     # Predict probabilities
#     result = pipe.predict_proba(input_df)
#     loss = result[0][0]
#     win = result[0][1]
    
#     return  win*100, loss*100
# # team_dropdown = gr.inputs.Dropdown(teams, label="Select Team")
# # city_dropdown = gr.inputs.Dropdown(cities, label="Select City")

# # demo = gr.Interface(
# #     fn=predict_probability,
# #     inputs=[
# #         gr.Dropdown(
# #             ['Sunrisers Hyderabad','Mumbai Indians','Royal Challengers Bangalore','Kolkata Knight Riders', 'Punjab Kings','Chennai Super Kings','Rajasthan Royals','Delhi Capitals','Gujarat Titans','Lucknow Super Giants'], label="team1", info="Will add more animals later!"
# #         ),
# #         gr.Dropdown(
# #             ['Sunrisers Hyderabad','Mumbai Indians','Royal Challengers Bangalore','Kolkata Knight Riders', 'Punjab Kings','Chennai Super Kings','Rajasthan Royals','Delhi Capitals','Gujarat Titans','Lucknow Super Giants'], label="team2", info="Will add more animals later!"
# #         ),
# #          gr.Dropdown(
# #             ['Ahmedabad', 'Chennai', 'Mumbai', 'Bengaluru', 'Kolkata', 'Delhi','Dharamsala', 'Hyderabad', 'Lucknow', 'Jaipur', 'Chandigarh','Guwahati', 'Navi Mumbai', 'Pune', 'Dubai', 'Sharjah', 'Abu Dhabi','Visakhapatnam', 'Indore', 'Bangalore', 'Raipur', 'Ranchi','Cuttack', 'Nagpur', 'Johannesburg', 'Centurion', 'Durban','Bloemfontein', 'Port Elizabeth', 'Kimberley', 'East London','Cape Town'], label="cities", info="Will add more animals later!"),
# #          "number", "number", "number", "number"
# #     ],
# #     outputs=["text","text"],
# #     title="IPL Win Predictor"
# # )


# # demo.launch()















# from sklearn.metrics import accuracy_score
# accuracy_score(y_test,y_pred)

# pipe.predict_proba(X_test)[89]
# def match_summary(row):
#     print("Batting team-" + row['team1'] + " | Bowling Team-" + row['team2'] + " | Target- " + str(row['total_runs_x']))

# def match_progression(x_df,match_id,pipe):
#     match = x_df[x_df['match_id'] == match_id]
#     match = match[(match['ball_number'] == 6)]
#     temp_df = match[['team1','team2','city','runs_left','balls_left','current_innings_wickets','total_runs_x','crr','rrr']].dropna()
#     temp_df = temp_df[temp_df['balls_left'] != 0]
#     result = pipe.predict_proba(temp_df)
#     temp_df['lose'] = np.round(result.T[0]*100,1)
#     temp_df['win'] = np.round(result.T[1]*100,1)
#     temp_df['end_of_over'] = range(1,temp_df.shape[0]+1)

#     target = temp_df['total_runs_x'].values[0]
#     runs = list(temp_df['runs_left'].values)
#     new_runs = runs[:]
#     runs.insert(0,target)
#     temp_df['runs_after_over'] = np.array(runs)[:-1] - np.array(new_runs)
#     wickets = list(temp_df['current_innings_wickets'].values)
#     new_wickets = wickets[:]
#     new_wickets.insert(0,10)
#     wickets.append(0)
#     w = np.array(wickets)
#     nw = np.array(new_wickets)
#     temp_df['wickets_in_over'] = (nw - w)[0:temp_df.shape[0]]

#     print("Target-",target)
#     temp_df = temp_df[['end_of_over','runs_after_over','wickets_in_over','lose','win']]
#     return temp_df,target

# def match_progression(x_df,match_id,pipe):
#     match = x_df[x_df['match_id'] == match_id]
#     match = match[(match['ball_number'] == 6)]
#     temp_df = match[['team1','team2','city','runs_left','balls_left','current_innings_wickets','total_runs_x','crr','rrr']].dropna()
#     temp_df = temp_df[temp_df['balls_left'] != 0]
#     result = pipe.predict_proba(temp_df)
#     temp_df['lose'] = np.round(result.T[0]*100,1)
#     temp_df['win'] = np.round(result.T[1]*100,1)
#     temp_df['end_of_over'] = range(1,temp_df.shape[0]+1)

#     target = temp_df['total_runs_x'].values[0]
#     runs = list(temp_df['runs_left'].values)
#     new_runs = runs[:]
#     runs.insert(0,target)
#     temp_df['runs_after_over'] = np.array(runs)[:-1] - np.array(new_runs)
#     wickets = list(temp_df['current_innings_wickets'].values)
#     new_wickets = wickets[:]
#     new_wickets.insert(0,10)
#     wickets.append(0)
#     w = np.array(wickets)
#     nw = np.array(new_wickets)
#     temp_df['wickets_in_over'] = (nw - w)[0:temp_df.shape[0]]

#     print("Target-",target)
#     temp_df = temp_df[['end_of_over','runs_after_over','wickets_in_over','lose','win']]
#     return temp_df,target

# temp_df,target = match_progression(delivery_df,	1370352,pipe)
# temp_df

# import matplotlib.pyplot as plt
# plt.figure(figsize=(18,8))
# plt.plot(temp_df['end_of_over'],temp_df['wickets_in_over'],color='yellow',linewidth=3)
# plt.plot(temp_df['end_of_over'],temp_df['win'],color='#00a65a',linewidth=4)
# plt.plot(temp_df['end_of_over'],temp_df['lose'],color='red',linewidth=4)
# plt.bar(temp_df['end_of_over'],temp_df['runs_after_over'])
# plt.title('Target-' + str(target))

# delivery_df







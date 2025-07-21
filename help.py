# import pandas as pd
# # import streamlit as st
# # gr = pd.read_csv("final_batting_2023.csv")
# # battters = gr['Player'].unique().tolist()
# # battters = st.selectbox("Select player",battters)
# batters = input("Enter a bats man : ")
# gr = pd.read_csv("ipl_players_info.csv")
# xy = gr[gr['player_name']==batters]
# y = xy["image_url"]
# print(y)
# print(xy)
# # name = xy["player_name"]
# # print(name)
# # print(y)

# import pandas as pd
# import streamlit as st

# gr = pd.read_csv("final_batting_2023.csv")
# batters = gr['Player'].unique().tolist()
# selected_batter = st.selectbox("Select player", batters)

# # Read player info from another CSV file
# player_info = pd.read_csv("ipl_players_info.csv")

# # Filter the player info based on the selected player
# selected_player_info = player_info[player_info['player_name'] == selected_batter]

# # Extract the image URL from the selected player's info
# image_url = selected_player_info["image_url"]
# name = selected_player_info["player_name"]
# st.title(name)

# # Display the image
# st.image('https://img1.hscicdn.com/image/upload/f_auto,t_ds_w_1280,q_80/lsci/db/PICTURES/CMS/356800/356803.1.png')





# import pandas as pd
# import streamlit as st

# gr = pd.read_csv("final_batting_2023.csv")
# batters = gr['Player'].unique().tolist()
# selected_batter = st.selectbox("Select player", batters)

# # Read player info from another CSV file
# player_info = pd.read_csv("ipl_players_info.csv")

# # Filter the player info based on the selected player
# selected_player_info = player_info[player_info['player_name'] == selected_batter]

# # Extract the image URL from the selected player's info
# image_url = selected_player_info["image_url"].values[0]

# # Convert the image URL object to a string
# image_url = str(image_url)

# # Display the image
# st.image(image_url)




import pandas as pd
import streamlit as st
import plotly.express as px
# gr = pd.read_csv("final_batting_2023.csv")
# batters = gr['Player'].unique().tolist()
# selected_batter = st.selectbox("Select player", batters)

# # Read player info from another CSV file
# player_info = pd.read_csv("ipl_players_info.csv")
# batters = player_info['player_name'].unique().tolist()
# selected_batter = st.selectbox("Select player", batters)
# # Filter the player info based on the selected player
# selected_player_info = player_info[player_info['player_name'] == selected_batter]

# # Check if there are any rows matching the selected player's name
# if not selected_player_info.empty:
#     # Extract the image URL from the selected player's info
#     image_url = selected_player_info["image_url"].values[0]

#     # Convert the image URL object to a string
#     image_url = str(image_url)

#     # Display the image
#     st.image(image_url ,width= 200)
# else:
#     st.write("Player not found.")





# from pandas import *
# data= read_csv("ball by ball.csv")
# df=DataFrame(data)
# ven= {"bat":[], "season":[], "total":[], "venue":[]}

# vend=DataFrame(ven)
# bat="Martin Guptill"
# venue="M Chinnaswamy Stadium"
# season=2022
# vrun=df[(df['striker'] == bat) & (df['season']==season) ] ['runs_off_bat'].sum()
# # vm=df[(df['striker'] == bat) & (df['venue'] == venue)]['match_id'].nunique()
# nr={'bat': bat,'season':season,'total':vrun,"venue":venue}
# vend = concat([vend, DataFrame([nr])], ignore_index=True)
# print(vend)


# fg = pd.read_csv("IPL_Matches_2008_2022.csv")
# bowler = pd.read_csv("ipl_bowling_card.csv")
# bowler = input("Enter a bowler : ")
i=1
if i==1:
    gr = pd.read_csv("final_batting.csv")
    battters = gr['Player'].unique().tolist()
    battters.insert(0,' ')
    battters = st.selectbox("Select player",battters)
    if battters != ' ':
        xy = gr[gr['Player']==battters]


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

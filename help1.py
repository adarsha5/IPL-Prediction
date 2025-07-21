import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("ball by ball.csv")
def bvr(bat,venue):
    vrun=df[(df['striker'] == bat) & (df['venue'] == venue) ] ['runs_off_bat'].sum()
    vm=df[(df['striker'] == bat) & (df['venue'] == venue)]['match_id'].nunique()
    return vrun,vm

print(bvr("Wriddhiman Saha","M Chinnaswamy Stadium"))
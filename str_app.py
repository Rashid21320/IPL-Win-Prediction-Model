import streamlit as st
import pickle
import pandas as pd
import base64
from PIL import Image

def get_base64_of_bin_file(bin_file):
    with open(bin_file,'rb')as f:
        data=f.read()
    return base64.b64encode(data).decode()
def set_jpg_as_page_bg(jpg_file):
    bin_str=get_base64_of_bin_file(jpg_file)
    page_bg_img='''
    <style>
    .stApp{
    background-image:url("data:/img.jpg;base64,%s");
    background-size:cover;
    opacity: 1streamlit run ;
    }
    <style>
    ''' % bin_str
    st.markdown(page_bg_img,unsafe_allow_html=True)
set_jpg_as_page_bg('./img.jpg')

teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Kolkata Knight Riders',
         'Royal Challengers Bangalore',
         'Punjab Kings',
         'Delhi Capitals',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Lucknow Super Giants',
        'Gujarat Titans']


cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']


pipe = pickle.load(open('pipe.pkl1','rb'))

st.title('IPL  Win  Predictor')

col1, col2 = st.columns(2)
with col1:
    Batting_team = st.selectbox('Select  Batting team',sorted(teams))
with col2:
    Bowling_team = st.selectbox('Select  Bowling team', sorted(teams))
selected_city = st.selectbox('Select Host City', sorted(cities))
target = st.number_input('Target',min_value=0,step=None)
col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Score',min_value=0,step=None)

with col4:
    overs = st.number_input('Overs ',min_value=0,max_value=20,step=None)
with col5:
    wickets = st.number_input('wicket out',min_value=0,max_value=10,step=None)
if st.button('Predict probability'):
    runs_left = target-score
    ball_left = 120-(overs*6)
    wickets = 10-wickets
    current_rr = score/overs
    Requied_rr = (runs_left*6)/ball_left

    input_df = pd.DataFrame({'batting_team': [Batting_team], 'bowling_team':[Bowling_team],

                         'city': [selected_city],'runs_left':[runs_left], 'ball_left':[ball_left],
                          'wickets': [wickets],
                          'total_runs_x': [target], 'current_rr': [current_rr],
                         'Requied_rr': [Requied_rr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(Batting_team + "- " + str(round(win*100)) + "%")
    st.header(Bowling_team + "- " + str(round(loss * 100)) + "%")



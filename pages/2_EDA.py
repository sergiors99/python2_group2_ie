import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px
import seaborn as sns
from streamlit_extras.app_logo import add_logo
from streamlit_extras.dataframe_explorer import dataframe_explorer
import datetime

add_logo("data/washington2.jpeg", height=100)

data = pd.read_csv('data/final_data.csv')
data['hr'] = pd.to_datetime(data['hr'])
data['hr'] = data['hr'].apply(lambda x: x.hour)

st.sidebar.markdown("# Exploratory Data Analysis")

st.header("EDA")

st.subheader("Dataframe")
st.text("Users Using the service")
st.markdown("###### DISCLAIMER: Very complex queries may crash the application")
interactive_data = dataframe_explorer(data)
interactive_data = pd.DataFrame(interactive_data.groupby('dteday')[['cnt','casual', 'registered']].sum())
st.bar_chart(interactive_data, use_container_width=True)

st.subheader("Distribution of users per year")
st.text("This distribution allow us to understand that most of the users comes from 2012\nand in a years the total usage of bicicles have double.")

fig = px.pie(data, values = 'cnt', names = 'year', title = 'Bike Sharing by Year')
st.plotly_chart(fig, use_container_width=True, sharing="streamlit", theme="streamlit")

st.subheader("Bike sharing by registered and casual users")
st.text("The usage of the previous graphs show the amount of casual and registed users\nper month and their behaviour.\nFor 2012 the total amount of users has a significant jump from feb to march.\nDuring march it had more users than any month of 2011.\nShowing a significant change of trend for the year 2012.\nNow the months of usage seems to deliver a significant amount of information\nof the total amount of as these related to the seasons.")
fig = px.histogram(data[data['year'] == 2011], x = 'month', y = ['casual', 'registered'], 
                   title = 'Bike Sharing by Casual and Registered Users - 2011' )
fig.update_layout(xaxis_title = 'Month', yaxis_title = 'Total Users', bargap = 0.1)
fig.update_xaxes(tickvals = [1,2,3,4,5,6,7,8,9,10,11,12], ticktext = ['Jan','Feb','Mar','Apr','May',
                                                                      'Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")

fig = px.histogram(data[data['year'] == 2012], x = 'month', y = ['casual', 'registered'], 
                   title = 'Bike Sharing by Casual and Registered Users - 2012')
fig.update_layout(xaxis_title = 'Month', yaxis_title = 'Total Users', bargap = 0.1)
fig.update_xaxes(tickvals = [1,2,3,4,5,6,7,8,9,10,11,12], ticktext = ['Jan','Feb','Mar','Apr','May',
                                                                      'Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")

fig = px.histogram(data, x = data['season'].astype(str), y = ['casual', 'registered'], 
                   title = 'Bike Sharing by Casual and Registered Users - Seasons')
fig.update_layout(xaxis_title = 'Season', yaxis_title = 'Total Users', bargap = 0.1)
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")

st.subheader("Bike Sharing by hour")
st.text("As can be infered from this graph the highest usage of bycicles occurs during the\nbeginning of the working hours at 8:00 and the the second picks occurs at\n17:00 and 18:00 when the users leave their jobs.\nAlso, the lowest usage occurs at 04:00 in the morning.")
fig = px.histogram(data, x = 'hr', y = ['casual', 'registered'], title = 'Bike sharing by hour')
fig.update_layout(xaxis_title = 'Hour', yaxis_title = 'Count', bargap = 0.1)
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")

st.subheader("Bike Sharing by weekday")
st.text("The distribution of days during the week doesn't show any significant trend.\nWhich tells us that the users constantly use the bikesharing service.")
filt = data.pivot_table(index = 'weekday', values = 'cnt', aggfunc = 'sum')
filt.reset_index(inplace = True)
filt['weekday'] = filt['weekday'].apply(lambda x: 'Sunday' if x == 0 else 'Monday' if x == 1 else 'Tuesday' if x == 2 
                                        else 'Wednesday' if x == 3 else 'Thursday' if x == 4 else 'Friday' if x == 5 
                                        else 'Saturday')
fig = px.histogram(filt, y = 'cnt', x = 'weekday', title = 'Bike Sharing by Weekday')
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")

st.subheader("Bike Sharing by Weather Situation")
st.text("As expected the highest usage of bikes occurs during good weather conditions\nas similiar to the summer days. Now with heavy rains and light the usage of the\nservice is drastically reduce due to the risks involved by the users.")
fig = px.histogram(data, x = 'weathersit', y = 'cnt', title = 'Bike Sharing by Weather Situation')
fig.update_layout(xaxis_title = 'Weather Situation', yaxis_title = 'Count', bargap = 0.1)
fig.update_xaxes(tickvals = [1,2,3,4], ticktext = ['Clear', 'Mist', 'Light Snow', 'Heavy Rain'])
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")

st.subheader("Bike Sharing by temperature")
st.text("Anything below 13.94 degrees is considered cold\nAnything between 13.94 degrees and 27.31 degrees is considered mild\nAnything above 27.06 degrees is considered warm")
filt = pd.pivot_table(data, index = 'temp', values = 'cnt', aggfunc = 'sum')
filt.reset_index(inplace = True)
filt['temp'] = filt['temp'].apply(lambda x: 'Cold' if x < 0.3 else 'Mild' if x >= 0.4 and x < 0.6 else 'Hot')
filt = filt.groupby('temp').sum()
filt.reset_index(inplace = True)
filt.sort_values(by = 'cnt', ascending = False, inplace = True)
fig = px.histogram(filt, x = 'temp', y = 'cnt', title = 'Bike Sharing by Temperature')
fig.update_layout(xaxis_title = 'Temperature', yaxis_title = 'Count')
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")

st.subheader("Bike Sharing by humidity")
st.text("Anything below 58.00 is considered dry\nAnything between 58.00 and 88.00 is considered humid\nAnything above 88.00 is considered very humid")
filt = pd.pivot_table(data, index = 'hum', values = 'cnt', aggfunc = 'sum')
filt.reset_index(inplace = True)
filt['hum'] = filt['hum'].apply(lambda x: 'Dry' if x < 0.48 else 'Humid' if x >= 0.48 and x < 0.78 else 'Very Humid')
filt = filt.groupby('hum').sum()
filt.reset_index(inplace = True)
filt.sort_values(by = 'cnt', ascending = False, inplace = True)
fig = px.histogram(filt, x = 'hum', y = 'cnt', title = 'Bike Sharing by Humidity')
fig.update_layout(xaxis_title = 'Humidity', yaxis_title = 'Count')
st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")

st.subheader("Correlation Matrix")
st.text("Based on the information presented it can be observed that season and month have\na high correlation. For the proupose of trainig of the model the variable will be\ndropped. The same analysis applies for temp, as the feeling of the temperature\nfor our prediciton analysis will have a deeper impact.")
cols_list = data.select_dtypes(include=np.number).columns.tolist()
plt.figure(figsize=(15, 7))
sns.heatmap(
    data[cols_list].corr(), annot=True, vmin=-1, vmax=1, fmt=".2f", cmap="Spectral")
st.pyplot(plt, clear_figure=True)
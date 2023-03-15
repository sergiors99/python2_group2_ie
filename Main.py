import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px
import seaborn as sns
from streamlit_extras.app_logo import add_logo

add_logo("data/washington2.jpeg", height=100)

st.sidebar.markdown("# Dashboard")
st.markdown("# Main page")

st.header("Index")

st.subheader("EDA")
st.markdown("- Users using the service")
st.markdown("- Distribution of users per year")
st.markdown("- Bike sharing by registered and casual users")
st.markdown("- Bike Sharing by hour")
st.markdown("- Bike Sharing by weekday")
st.markdown("- Bike Sharing by Weather Situation")
st.markdown("- Bike Sharing by temperature")
st.markdown("- Bike Sharing by humidity")
st.markdown("- Correlation Matrix")
st.markdown("- Dataframe")

st.subheader("Machine Learning")
st.markdown("- Feature Engineering")
st.markdown("- Modeling the data")
st.markdown("- Model Evaluation")
st.markdown("- Deploying Model")

st.subheader("Predictions Tool")
st.markdown("- Make your predictions in real time")
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
st.markdown("- [Users using the service](http://localhost:8501/EDA#users-using-the-service)")
st.markdown("- [Distribution of users per year](http://localhost:8501/EDA#distribution-of-users-per-year)")
st.markdown("- [Bike sharing by registered and casual users](http://localhost:8501/EDA#bike-sharing-by-registered-and-casual-users)")
st.markdown("- [Bike Sharing by hour](http://localhost:8501/EDA#bike-sharing-by-hour)")
st.markdown("- [Bike Sharing by weekday](http://localhost:8501/EDA#bike-sharing-by-weekday)")
st.markdown("- [Bike Sharing by Weather Situation](http://localhost:8501/EDA#bike-sharing-by-weather-situation)")
st.markdown("- [Bike Sharing by temperature](http://localhost:8501/EDA#bike-sharing-by-humidity)")
st.markdown("- [Bike Sharing by humidity](http://localhost:8501/EDA#bike-sharing-by-humidity)")
st.markdown("- [Correlation Matrix](http://localhost:8501/EDA#correlation-matrix)")
st.markdown("- [Dataframe](http://localhost:8501/EDA#dataframe)")

st.subheader("Machine Learning")
st.markdown("- [Step 1 - Train/Test Split](http://localhost:8501/Machine_Learning#step-1-train-test-split)")
st.markdown("- [Step 2 - Modeling the data](http://localhost:8501/Machine_Learning#step-2-modeling-the-data)")
st.markdown("- [Step 3 - Model Evaluation](http://localhost:8501/Machine_Learning#step-3-model-evaluation)")
st.markdown("- [Step 4 - Deploying Model](http://localhost:8501/Machine_Learning#step-4-deploying-model)")

st.subheader("Predictions Tool")
st.markdown("- [Make your predictions in real time](http://localhost:8501/Predictions_Tool#make-your-predictions-in-real-time)")

st.subheader("Suggestions")
st.markdown("- [Possible Solutions](http://localhost:8501/Suggestions#suggestions)")
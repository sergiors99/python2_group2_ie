import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px
import seaborn as sns
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.app_logo import add_logo
from streamlit_extras.echo_expander import echo_expander
from io import StringIO
from datetime import datetime, time
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

add_logo("data/washington2.jpeg", height=100)

st.sidebar.markdown("# Machine Learning Process")

st.markdown("# Machine Learning")
st.text("After doing the data preprocessing, we can start working on our model.\nOur goal is to predict the total amount of users since all the users are going to need a bike.")

st.subheader("Step 1 - Train/Test Split")
st.text("We need to divide the data into our train and test sets")
with echo_expander():
    from sklearn.model_selection import train_test_split

st.subheader("Step 2 - Modeling the data")
st.text("In this step we set up the algorithms for the models we will be using.")
with echo_expander():
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.neighbors import KNeighborsRegressor
    import xgboost as xgb
    from lightgbm import LGBMRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression

st.subheader("Step 3 - Model Evaluation")
st.text("Now we compare the score of the metrics we used to evaluate the model\nand choose the one that suits our needs best")
with echo_expander():
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

st.markdown("##### Linear Regression")
st.markdown("- Mean Absolute Error: 94.42")
st.markdown("- Mean Squared Error: 15685.24")
st.markdown("- Root Mean Squared Error: 125.24")
st.markdown("- R2 Score: 0.53")

st.markdown("##### K-neighbours")
st.markdown("- Mean Squared Error: ")
st.markdown("- Mean Absolute Error: ")
st.markdown("- Root Mean Squared Error: ")
st.markdown("- R2 Score: ")

st.markdown("##### Random Forest Regressor")
st.markdown("- Mean Absolute Error: 47.07")
st.markdown("- Mean Squared Error: 4767.46")
st.markdown("- Root Mean Squared Error: 69.05")
st.markdown("- R2 Score: 0.86")

st.markdown("##### LGBMRegressor")
st.markdown("- Mean Absolute Error: 26.17")
st.markdown("- Mean Squared Error: 1695.94")
st.markdown("- Root Mean Squared Error: 41.18")
st.markdown("- R2 Score: 0.95")

st.markdown("##### XGBRegressor")
st.markdown("- Mean Absolute Error: 24.78")
st.markdown("- Mean Squared Error: 1533.59")
st.markdown("- Root Mean Squared Error: 39.16")
st.markdown("- R2 Score: 0.95")

st.subheader("Step 4 - Deploying Model")
st.text("Once we have our best mode, on this case being XGBRegressor, because it returned\nthe best metrics for our business solution")
st.text("Now that we have our trained model we need to save it for future use, so that our\nclients can make predictions.")
with echo_expander():
    import pickle
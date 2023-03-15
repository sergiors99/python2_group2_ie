import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px
import seaborn as sns
from streamlit_card import card
from streamlit_extras.app_logo import add_logo
from streamlit_extras.metric_cards import style_metric_cards

add_logo("data/washington2.jpeg", height=100)

data = pd.read_csv('data/final_data.csv')

st.markdown("# Suggestions")
st.sidebar.markdown("# After going through all the data and analysing the information, we reached certain conclussions")

card(
    title="Maintenance Costs",
    text="Having the adequate amount of bikes in circulation during harsh weather will result in lower costs",
    image="https://cdn.shopify.com/s/files/1/0273/3604/8726/products/PureFluxOneElectricHybridBike_1_300x.jpg",
)

col1, col2, col3 = st.columns(3)
col1.metric(label="Gain", value=5000, delta=1000)
col2.metric(label="Loss", value=5000, delta=-1000)
col3.metric(label="No Change", value=5000, delta=0)
style_metric_cards()
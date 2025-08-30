import streamlit as st
import pandas as pd 

st.title('🤖 Machine Leaning App')

st.info('This is a machine Learning App!')

df = pd.reascsv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df

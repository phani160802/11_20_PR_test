import streamlit as st
import pandas as pd

st.markdown('''**virat Stats**''')
virat_stats = pd.read_csv("final_virat_stat.csv")
st.dataframe(virat_stats)

st.markdown(''' **Sachin Stats**''')
sachin_stats= pd.read_csv("final_sachin_stats.csv")
st.dataframe(sachin_stats)
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid


st.write("## Meu Aplicativo Web")

@st.cache_data
def load_data(path, sheet_name):
    df = pd.read_excel(path, sheet_name=sheet_name)
    return df



df = load_data("data/financeiro/quadro_atual_empresa.xlsx", "dados")

with st.container():
  AgGrid(df, height=200)    


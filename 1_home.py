import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime
import pprint

st.write(" # FIFA23_official_data")

if "data" not in st.session_state:
    df_data = pd.read_csv(r"C:\Users\DIEGO\Documents\GitHub\Streamlit_1app\datasets\FIFA23_official_data.csv",index_col=0)
    # df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    # df_data = df_data[df_data["Value(€)"] >0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data


st.sidebar.markdown("Desenvolvido por Diego")
btn1 = st.button("Acesse os dados do Kaggle")
if btn1:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(" O conjunto de dados conterá mais de 17 mil jogadores únicos e mais de 60 colunas, informações gerais e todos os KPIs que o famoso videogame oferece."
            ""
            
            " Este conjunto de dados contém estatísticas de jogadores do FIFA17 ao FIFA23,"
            ""
            
            
            
            "*Aproveitar !*  ")



# testando commit2ee

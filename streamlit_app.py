import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout = "wide")

df = pd.DataFrame(px.data.gapminder())

st.header("Estadísticas Mundiales")
page = st.sidebar.selectbox('Seleccione',
  ['Datos por países','Datos por continente'])

if page == 'Datos por países':
  # PAISES
  clist = df['country'].unique()

  country = st.selectbox("Seleccione un país:",clist)
  col1, col2 = st.columns(2)

  fig = px.line(df[df['country'] == country], 
    x = "year", y = "gdpPercap",title = "PIB per cápita",
    labels={"year": "Año",
            "gdpPercap": "PIB per cápita (dólares)"})
  
  col1.plotly_chart(fig,use_container_width = True)

  fig = px.line(df[df['country'] == country], 
    x = "year", y = "pop",title = "Crecimiento de la población",
    labels={"year": "Año",
            "pop": "Población (millones)"} )
  
  col2.plotly_chart(fig,use_container_width = True)

else:
  # CONTINENTES
  contlist = df['continent'].unique()
 
  continent = st.selectbox("Seleccione un continente:",contlist)
  col1,col2 = st.columns(2)
  fig = px.line(df[df['continent'] == continent], 
    x = "year", y = "gdpPercap",
    title = "PIB per cápita",color = 'country',
    labels={"year": "Año",
            "gdpPercap": "PIB per cápita (dólares)"})
  
  col1.plotly_chart(fig)
  fig = px.line(df[df['continent'] == continent], 
    x = "year", y = "pop",
    title = "Crecimiento de la población",color = 'country',
    labels={"year": "Año",
            "pop": "Población (millones)"})
  
  col2.plotly_chart(fig, use_container_width = True)

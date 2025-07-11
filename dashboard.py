import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Dashboard de Temperaturas IoT')

# Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg = pd.read_csv('view_avg_temp.csv')
fig1 = px.bar(df_avg, x='device_id', y='avg_temp')
st.plotly_chart(fig1)

# Leituras por hora do dia
st.header('Leituras por Hora do Dia')
df_hora = pd.read_csv('view_leituras_hora.csv')
fig2 = px.line(df_hora, x='hora', y='contagem')
st.plotly_chart(fig2)

# Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_dia = pd.read_csv('view_temp_max_min.csv')
fig3 = px.line(df_dia, x='data', y=['temp_max', 'temp_min'])
st.plotly_chart(fig3)

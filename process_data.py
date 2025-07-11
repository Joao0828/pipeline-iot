import pandas as pd
import os

# Caminho para o CSV
csv_path = os.path.join('data', 'IOT-temp.csv')
df = pd.read_csv(csv_path)

# Renomear colunas
df.columns = ['id', 'room_id', 'noted_date', 'temp', 'in_out']
df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M')

# View 1: Média de temperatura por dispositivo
avg_temp_por_dispositivo = df.groupby('room_id')['temp'].mean().reset_index()
avg_temp_por_dispositivo.columns = ['device_id', 'avg_temp']

# View 2: Contagem de leituras por hora
df['hora'] = df['noted_date'].dt.hour
leituras_por_hora = df.groupby('hora').size().reset_index(name='contagem')

# View 3: Temperaturas máximas e mínimas por dia
df['data'] = df['noted_date'].dt.date
temp_max_min_por_dia = df.groupby('data')['temp'].agg(['max', 'min']).reset_index()
temp_max_min_por_dia.columns = ['data', 'temp_max', 'temp_min']

# Salvar os DataFrames simulando views SQL
avg_temp_por_dispositivo.to_csv('view_avg_temp.csv', index=False)
leituras_por_hora.to_csv('view_leituras_hora.csv', index=False)
temp_max_min_por_dia.to_csv('view_temp_max_min.csv', index=False)

print("Views simuladas salvas com sucesso.")

import pandas as pd

arquivos = ['view_avg_temp.csv', 'view_leituras_hora.csv', 'view_temp_max_min.csv']

for arq in arquivos:
    print(f"\nConteúdo de {arq}:")
    df = pd.read_csv(arq)
    print(df.head())

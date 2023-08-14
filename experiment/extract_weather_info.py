import yaml
import pandas as pd
from os.path import join
from datetime import datetime, timedelta
from utils.functions import folder_creation

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

# Abrir o arquivo YAML
with open('configs.yaml', 'r') as file:
    dados = yaml.safe_load(file)

city = dados['city']
key = dados['key_visualcrossing']

URL = join(
    'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
    f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv'
)

dados = pd.read_csv(URL)
print(dados.head())

file_path = f'./data/{data_inicio}/'
folder_creation(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

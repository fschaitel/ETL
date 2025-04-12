# Vamos importar o que precisamos
import pandas as pd
import sqlite3
from datetime import datetime

# Definir o caminho para o arquivo JSONL
df = pd.read_json('data/data.jsonl', lines = True)

# Setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

# Adicionar a coluna _source com um valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/notebook"

# Adicionar a coluna _data_coleta com a data e hora atuais

df['_datetime'] = datetime.now()

# Tratar nulos
df['old_money'] = df['old_money'].fillna('0')
df['new_money'] = df['new_money'].fillna('0')
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
df['reviews_amount'] = df['reviews_amount'].fillna('(0)')

# Garantir que estão como strings antes de usar .str
df['old_money'] = df['old_money'].astype(str).str.replace('.', '', regex=False)
df['new_money'] = df['new_money'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace('[\(\)]', '', regex=True)

# Converter para números
df['old_money'] = df['old_money'].astype(float)
df['new_money'] = df['new_money'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)

# Tratar os preços como floats e calcular os valores totais
# Manter apenas produtos com preço entre 1000 e 10000 reais
df = df[
    (df['old_money'] >= 1000) & (df['old_money'] <= 10000) &
    (df['new_money'] >= 1000) & (df['new_money'] <= 10000)
]

# Remover as colunas antigas de preços

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('data/mercadolivre.db')

# Salvar o DataFrame no banco de dados SQLite
df.to_sql('notebook', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

# Configurar pandas para mostrar todas as colunas

# Exibir o DataFrame resultante
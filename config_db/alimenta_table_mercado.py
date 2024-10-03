import psycopg2
import json

# config do banco de dados
# conn = psycopg2.connect(
#     "postgresql://root:ZEnRnvAwnztnyA96VC3dsLUTzfvqPNtY@dpg-crtc7l3tq21c73dnhdcg-a.oregon-postgres.render.com/marketcheck_development"
# )
# cur = conn.cursor()

conn = psycopg2.connect(
dbname="marketcheck_development", ## criar um banco de dados chamado marketcheck
    user="postgres", ## subsituir pelo seu usuário
    password="1234", ## subsituir por sua senha
    host="localhost", 
    port="5432",
    options="-c client_encoding=UTF8"
)
cur = conn.cursor()

# crie uma função para inserir o arquivo create_table_mercado.sql e criar a tabela Mercado
def criar_tabela_mercado():
    with open('create_table_mercado.sql', 'r', encoding='utf-8') as f:
        cur.execute(f.read())
        conn.commit()
    print("Tabela Mercado criada com sucesso.")

criar_tabela_mercado()

cur.close()
conn.close()
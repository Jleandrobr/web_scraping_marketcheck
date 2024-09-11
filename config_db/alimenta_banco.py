import psycopg2
import json

# config do banco de dados
conn = psycopg2.connect(
    dbname="marketcheck", ## criar um banco de dados chamado marketcheck
    user="postgres", ## subsituir pelo seu usuário
    password="1234", ## subsituir por sua senha
    host="localhost", 
    port="5432",
    options="-c client_encoding=UTF8"
)
cur = conn.cursor()


def inserir_dados(mercado_id, produtos_json):
    for produto in produtos_json:
        cur.execute("""
            INSERT INTO Produtos (nome_produto, link_to_item, image_url, preco, categoria)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
        """, (produto['description'], produto['link_to_item'], produto['image_url'], float(produto['price'].replace(',', '.')), produto['category']))
        
        produto_id = cur.fetchone()[0] 
        
        # inserir preço do produto na tabela ProdutosPreco
        cur.execute("""
            INSERT INTO ProdutosPreco (produto_id, mercado_id, preco)
            VALUES (%s, %s, %s)
        """, (produto_id, mercado_id, float(produto['price'].replace(',', '.'))))

# ids de mercado
mercado_atacadao_id = 1  
mercado_menorpreco_id = 2  
mercado_paodeacucar_id = 3  
mercado_supermercadomanaira_id = 4  


def carregar_dados():
    with open('atacadao/atacadao_tratados_alimentos.json', 'r', encoding='utf-8') as f:
        produtos_atacadao_alimentos = json.load(f)
        inserir_dados(mercado_atacadao_id, produtos_atacadao_alimentos)
   
    with open('atacadao/atacadao_tratados_limpeza.json', 'r', encoding='utf-8') as f:
        produtos_atacadao_limpeza = json.load(f)
        inserir_dados(mercado_atacadao_id, produtos_atacadao_limpeza)

    with open('menorpreco/menorpreco_tratados_alimentos_basicos.json', 'r', encoding='utf-8') as f:
        produtos_menorpreco_alimentos_basicos = json.load(f)
        inserir_dados(mercado_menorpreco_id, produtos_menorpreco_alimentos_basicos)

    with open('menorpreco/menorpreco_tratados_limpeza.json', 'r', encoding='utf-8') as f:
        produtos_menorpreco_limpeza = json.load(f)
        inserir_dados(mercado_menorpreco_id, produtos_menorpreco_limpeza)

    with open('paodeacucar/paodeacucar_tratados_alimentos_basicos.json', 'r', encoding='utf-8') as f:
        produtos_paodeacucar_alimentos_basicos = json.load(f)
        inserir_dados(mercado_paodeacucar_id, produtos_paodeacucar_alimentos_basicos)
    
    with open('paodeacucar/paodeacucar_tratados_limpeza.json', 'r', encoding='utf-8') as f:
        produtos_paodeacucar_limpeza = json.load(f)
        inserir_dados(mercado_paodeacucar_id, produtos_paodeacucar_limpeza)

    with open('supermercado manaira/supermanaira_tratados_alimentos_basicos.json', 'r', encoding='utf-8') as f:
        produtos_supermanaira_alimentos_basicos = json.load(f)
        inserir_dados(mercado_supermercadomanaira_id, produtos_supermanaira_alimentos_basicos)

    with open('supermercado manaira/supermanaira_tratados_limpeza.json', 'r', encoding='utf-8') as f:
        produtos_supermanaira_limpeza = json.load(f)
        inserir_dados(mercado_supermercadomanaira_id, produtos_supermanaira_limpeza)


carregar_dados()


conn.commit()
cur.close()
conn.close()

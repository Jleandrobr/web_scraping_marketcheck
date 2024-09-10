import json

data_json = [

]
# Dados JSON fornecidos
for pastas in ['supermercado manaira/supermanaira_alimentos_basicos.json']:
    with open(pastas, 'r', encoding='utf-8') as f:
        data_json += json.load(f)
# Processar os dados
    for item in data_json:
        if 'item_number' in item:
            del item['item_number']
        item['price'] = item['price'].split('\n')[0].strip()  # Remove a parte da promoção e quebra de linha
        item['price'] = item['price'].replace('R$', '').strip()  # Remove o símbolo "R$"
        item['category'] = 'Mercearia'

# Salvar como JSON
with open('supermercado manaira/supermanaira_tratados_alimentos_basicos.json', 'w', encoding='utf-8') as f:
    json.dump(data_json, f, ensure_ascii=False, indent=4)

print("Dados salvos em 'supermanaira/supermanaira_tratados_alimentos_basicos.json'.")


import json

data_json = []

with open('supermercado manaira/supermanaira_limpeza.json', 'r', encoding='utf-8') as f:
    data_json = json.load(f)


    for item in data_json:
        if 'item_number' in item:
            del item['item_number']
        item['price'] = item['price'].split('\n')[0].strip()
        item['price'] = item['price'].replace('R$', '').strip()  
        item['category'] = 'Limpeza'


with open('supermercado manaira/supermanaira_tratados_limpeza.json', 'w', encoding='utf-8') as f:
    json.dump(data_json, f, ensure_ascii=False, indent=4)

print("Dados salvos em 'supermanaira/supermanaira_tratados_limpeza.json'.")

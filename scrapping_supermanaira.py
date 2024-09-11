import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
# chrome_options.add_argument("--headless") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# url = 'https://www.sitemercado.com.br/supermercadomanaira/joao-pessoa-loja-manaira-manaira-rua-joao-cancio/lista-pronta/dia-de-faxina' ## Limpeza
url = 'https://www.sitemercado.com.br/supermercadomanaira/joao-pessoa-loja-manaira-manaira-rua-joao-cancio/produtos/alimentos-basicos' ## Alimentos básicos

driver.get(url)

try:

    wait = WebDriverWait(driver, 20) 
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.list-product-item')))


    if elements:
        items = []
        for idx, element in enumerate(elements):
            try:
                description = element.find_element(By.CSS_SELECTOR, 'a.list-product-link').get_attribute('aria-label')

                link_to_item = element.find_element(By.CSS_SELECTOR, 'a.list-product-link').get_attribute('href')
                
                price = element.find_element(By.CSS_SELECTOR, 'div.area-bloco-preco.bloco-preco.pr-0.ng-star-inserted').text
                
                image_url = element.find_element(By.CSS_SELECTOR, 'img.img-fluid.ng-lazyloaded').get_attribute('src')
                
                item_data = {
                    "item_number": idx + 1,
                    "description": description,
                    "link_to_item": link_to_item,
                    "price": price,
                    "image_url": image_url
                }
                items.append(item_data)
            except Exception as e:
                print(f"Erro ao processar o elemento {idx + 1}: {e}")
        
        items_json = json.dumps(items, ensure_ascii=False, indent=4)

        with open('supermanaira.json', 'w', encoding='utf-8') as json_file:
            json_file.write(items_json)
        
        print("Dados salvos em 'supermanaira.json'.")
    else:
        print("Nenhum item encontrado.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()

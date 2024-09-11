import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")  # roda o chrome em modo headless (sem interface gráfica)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# url = 'https://loja.verdfrut.com.br/loja/672/categoria/17856' ## Limpeza
url = 'https://loja.verdfrut.com.br/loja/672/categoria/17861'   ## Massas

driver.get(url)

try:
    wait = WebDriverWait(driver, 10) 
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.MuiGrid-root.w-lg-20.store-card-product.px-1.fade.show.MuiGrid-item.MuiGrid-grid-xs-6.MuiGrid-grid-sm-4.MuiGrid-grid-md-3')))
    
    if elements:
        items = []
        for idx, element in enumerate(elements):
            item_data = {
                "item_number": idx + 1,
                "description": element.text,
                "image": element.find_element(By.CSS_SELECTOR, 'img').get_attribute('src'),
                "price": element.find_element(By.CSS_SELECTOR, 'p.current-price-product').text
            }
            items.append(item_data)
        
        items_json = json.dumps(items, ensure_ascii=False, indent=4)
        
        with open('verdfrut/verdfrut_massas.json', 'w', encoding='utf-8') as json_file:
            json_file.write(items_json)
        
        print("Dados salvos em 'verdfrut_massas.json'.")
    else:
        print("Nenhum item encontrado.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()

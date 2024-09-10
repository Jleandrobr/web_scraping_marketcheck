import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações do navegador
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Executa o Chrome em modo headless (sem interface gráfica)

# Cria uma instância do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL da página que você deseja acessar
# url = 'https://www.paodeacucar.com/especial/limpeza_hs_ofertas' ## Limpeza
url = 'https://www.paodeacucar.com/especial/hs_ofertas_mercearia?p=3' ## Produtos despesas

# Abre a página
driver.get(url)

try:
    scroll_pause_time = 2.0  # Tempo de espera após cada rolagem (em segundos)
    scroll_increment = 800  # Quantidade de pixels a rolar para baixo a cada passo

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        for i in range(0, last_height, scroll_increment):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)

            new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Se a altura da página não mudou, interrompe o loop
        last_height = new_height

        wait = WebDriverWait(driver, 20)
        break # Espera até 10 segundos

    # Espera até que os elementos estejam presentes na página
    wait = WebDriverWait(driver, 20)  # Espera até 10 segundos
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.product-cardstyles__CardStyled-sc-1uwpde0-0.bTCFJV.cardstyles__Card-yvvqkp-0.gXxQWo')))
    
    # Verifica se há elementos encontrados
    if elements:
        items = []
        for idx, element in enumerate(elements):
            try:
                description = element.find_element(By.CSS_SELECTOR, 'span.product-cardstyles__Text-sc-1uwpde0-7.hXaJKO').text

                link_to_item = element.find_element(By.CSS_SELECTOR, 'a.hyperlinkstyles__Link-j02w35-0.hbKsSa').get_attribute('href')
                
                try:
                    price = element.find_element(By.CSS_SELECTOR, 'p.price-tag-normalstyle__LabelPrice-sc-1co9fex-0.lkWvql').text
                except:
                    price = element.find_element(By.CSS_SELECTOR, 'div.seal-sale-box-divided__Value-pf7r6x-3.bgtGEw').text
                
                image_url = element.find_element(By.CSS_SELECTOR, 'img.product-cardstyles__Image-sc-1uwpde0-3.beZujn').get_attribute('src')
                
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
        
        # Converte a lista de itens em JSON
        items_json = json.dumps(items, ensure_ascii=False, indent=4)
        
        # Salva os dados em um arquivo JSON
        with open('paodeacucar/paodeacucar_alimentos_basicos.json', 'w', encoding='utf-8') as json_file:
            json_file.write(items_json)
        
        print("Dados salvos em 'paodeacucar_alimentos_basicos.json'.")
    else:
        print("Nenhum item encontrado.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Fecha o navegador
    driver.quit()

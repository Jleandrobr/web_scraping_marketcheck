from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# Inicializar o WebDriver (certifique-se de especificar o caminho para o seu WebDriver)
driver = webdriver.Chrome()

# Navegar para a URL desejada
driver.get("https://loja.verdfrut.com.br/loja/672/categoria/17856")

# Esperar até que o elemento do rodapé esteja presente usando um seletor mais simples
try:
    footer = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.current-price-product"))
    )

    # Definir a origem do scroll com base no elemento do rodapé
    scroll_origin = ScrollOrigin.from_element(footer)

    # Realizar o scroll na página usando ActionChains
    ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 3000)\
        .perform()

    # Pausar para visualizar os resultados (opcional)
    sleep(5)

finally:
    # Fechar o navegador
    driver.quit()

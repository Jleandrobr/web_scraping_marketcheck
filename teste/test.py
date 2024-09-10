from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# Initialize the WebDriver (make sure to specify the path to your WebDriver)
driver = webdriver.Chrome()

# Navigate to the desired URL
driver.get("https://selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html")

# Locate the iframe element
iframe = driver.find_element(By.TAG_NAME, "iframe")

# Define the scroll origin based on the iframe element
scroll_origin = ScrollOrigin.from_element(iframe)

# Scroll within the iframe using ActionChains
ActionChains(driver)\
    .scroll_from_origin(scroll_origin, 0, 200)\
    .perform()

# Pause to view the results (optional)
sleep(5)

# Close the browser
driver.quit()


# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# # Inicializar o WebDriver (certifique-se de especificar o caminho para o seu WebDriver)
# driver = webdriver.Chrome()

# # Navegar para a URL desejada
# driver.get("https://loja.verdfrut.com.br/loja/672/categoria/17856")

# # Esperar até que o elemento do rodapé esteja presente usando um seletor mais simples
# try:
#     footer = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div.footer-stock-message"))
#     )

#     # Definir a origem do scroll com base no elemento do rodapé
#     scroll_origin = ScrollOrigin.from_element(footer)

#     # Realizar o scroll na página usando ActionChains
#     ActionChains(driver)\
#         .scroll_from_origin(scroll_origin, 0, 200)\
#         .perform()

#     # Pausar para visualizar os resultados (opcional)
#     sleep(5)

# finally:
#     # Fechar o navegador
#     driver.quit()


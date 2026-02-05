from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# Configuração essencial para rodar em containers
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Conecta no container 'chrome' do docker-compose
driver = webdriver.Remote(
    command_executor='http://chrome:4444/wd/hub',
    options=options
)

try:
    driver.get("https://www.google.com")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    print("Página carregada:", driver.title)
finally:
    driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        options=options
    )

    try:
        executar(driver)
    finally:
        driver.quit()


def executar(driver):
    #Confiugurar o WebDriverWait para aguardar até 15 segundos por elementos
    wait = WebDriverWait(driver, 15)

    #Acessar a página de dados abertos da Imprensa Nacional
    driver.get("https://in.gov.br/acesso-a-informacao/dados-abertos/base-de-dados")
    print("Página carregada:", driver.title)

    #Aqui desenvolver o restante do código


if __name__ == "__main__":
    main()

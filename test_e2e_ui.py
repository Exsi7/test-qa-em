from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def test_purchase():
    # Настройки веб-драйвера для Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Открыть сайт
        driver.get("https://www.saucedemo.com")

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Выбор товара
        driver.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]').click()
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        
        # Перейти в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # Проверить наличие товара в корзине
        assert "Sauce Labs Backpack" in driver.page_source
        
        # Оформление покупки
        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("Test")
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        
        # Проверка завершения покупки
        success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert success_message == "Thank you for your order!"
        print("Тест пройден успешно!")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_purchase()
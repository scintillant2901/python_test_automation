# '''Shop: проверка цены в корзине'''
# 1. Откройте https://practice.automationtesting.in/
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00" •
# 5. Перейдите в корзину
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Логин
my_account_menu = driver.find_element_by_link_text("My Account").click()
username_field = driver.find_element_by_id("username")
username_field.send_keys("fortest87@bk.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("SomeHardTest")
login_btn_click = driver.find_element_by_name("login").click()
# Переход на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop").click()
# Добавление в корзину книги "HTML5 WebApp Development"
html5_webApp_development_book = driver.find_element_by_css_selector("[data-product_id='182']")
html5_webApp_development_book.click()
time.sleep(3)
# Добавление теста, что возле корзины количество товаров = "1 Item", а стоимость = "₹180.00"
cart_count = driver.find_element_by_css_selector("span.cartcontents")
cart_count_text = cart_count.text
assert cart_count.text == "1 Item"
time.sleep(3)
cart_price = driver.find_element_by_css_selector("span.amount")
cart_price_text = cart_price.text
assert cart_price.text == "₹180.00"
# Переход в корзину
cart = driver.find_element_by_css_selector("[title='View your shopping cart']")
cart.click()
# Проверка, что в Subtotal отобразилась стоимость
subtotal_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-subtotal .amount")))
time.sleep(3)
# Проверка, что в Total отобразилась стоимость
total_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-total .amount")))

driver.quit()
#'''Shop: количество товаров в категории'''
# 1. Откройте https://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте категорию "HTML"
# 5. Добавьте тест, что отображается три товара

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Логин
my_account_menu_click = driver.find_element_by_link_text("My Account").click()
username_field = driver.find_element_by_id("username")
username_field.send_keys("fortest87@bk.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("SomeHardTest")
login_btn = driver.find_element_by_name("login").click()
# Переход на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop").click()
# Открытие категории "HTML"
html_category = driver.find_element_by_css_selector(".product-categories li:nth-child(2)>a")
html_category.click()
# Добавление теста, что отображается три товара
#products_count = driver.find_element_by_css_selector("ul.products > li")
products_count = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product")))
assert len(products_count) == 3

driver.quit()
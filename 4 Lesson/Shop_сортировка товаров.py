#'''Shop: сортировка товаров'''
# 1. Откройте https://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# 5. Отсортируйте товары по цене от большей к меньшей
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей

from selenium import webdriver
from selenium.webdriver.support.select import Select

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
# Проверка, что в селекторе выбран вариант сортировки по умолчанию
default_option = driver.find_element_by_name("orderby")
selected_value = default_option.get_attribute("value")
assert selected_value == "menu_order"
# Сортировка товаров по цене от большей к меньшей
select_sort_by = Select(driver.find_element_by_name("orderby"))
select_sort_by.select_by_value("price-desc")
# Обновление переменной с локатором основного селектора сортировки
select_sort_by = Select(driver.find_element_by_name("orderby"))
# Проверка, что в селекторе выбран вариант сортировки по цене от большей к меньшей
current_option = select_sort_by.first_selected_option
assert current_option.get_attribute("value") == "price-desc"

driver.quit()
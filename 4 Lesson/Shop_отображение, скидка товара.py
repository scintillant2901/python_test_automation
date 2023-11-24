# '''Shop: отображение, скидка товара'''
# 1. Откройте https://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "Android Quick Start Guide"
# 5. Добавьте тест, что содержимое старой цены = "₹600.00"
# 6. Добавьте тест, что содержимое новой цены = "₹450.00"
# 7. Добавьте явное ожидание и нажмите на обложку книги
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)

from selenium import webdriver
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
# shop_tab_click = driver.find_element_by_id("menu-item-40").click()
# Открытие книги "Android Quick Start Guide"
android_quick_start_guide = driver.find_element_by_css_selector(".post-169 h3").click()
#android_quick_start_guide = driver.find_element_by_css_selector(".post-169 > a:nth-child(1)").click()
#android_quick_start_guide = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']").click()
# Получение значения старой и новой цены
guide_old_price = driver.find_element_by_css_selector(".price > del > span")
guide_old_price_text = guide_old_price.text
guide_new_price = driver.find_element_by_css_selector(".price > ins > span")
guide_new_price_text = guide_new_price.text
# Проверка значений цен
assert guide_old_price_text == "₹600.00"
assert guide_new_price_text == "₹450.00"
# Явное ожидание и нажатие на обложку книги
guide_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
guide_cover.click()
# Явное ожидание для кнопки закрытия обложки в режиме предпросмотра
guide_cover_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")))
guide_cover_close.click()

driver.quit()
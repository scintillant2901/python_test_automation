#'''Shop: отображение страницы товара'''
# 1. Откройте https://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "HTML5 Forms"
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"

from selenium import webdriver
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
# Открытие книги "HTML5 Forms"
html5_forms_book = driver.find_element_by_css_selector(".post-181 h3")
html5_forms_book.click()
# Проверка заголовка книги
html5_forms_book_title = driver.find_element_by_css_selector(".product_title.entry-title")
html5_forms_book_title_text = html5_forms_book_title.text
assert html5_forms_book_title_text == "HTML5 Forms"

driver.quit()
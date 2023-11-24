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


# '''Shop: работа в корзине'''
# 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# 4. Перейдите в корзину
# 5. Удалите первую книгу
# 6. Нажмите на Undo (отмена удаления)
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# 8. Нажмите на кнопку "UPDATE BASKET"
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# 10. Нажмите на кнопку "APPLY COUPON"
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Переход на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop").click()
# Скролл страницы вниз на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")
# Добавление в корзину книг "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
html5_webApp_development_book = driver.find_element_by_css_selector("[data-product_id='182']")
html5_webApp_development_book.click()
time.sleep(3)
js_data_structures_and_algorithm_book = driver.find_element_by_css_selector("[data-product_id='180']")
js_data_structures_and_algorithm_book.click()
time.sleep(5)
# Переход в корзину
cart = driver.find_element_by_css_selector("[title='View your shopping cart']")
cart.click()
time.sleep(3)
# Удаление книги "HTML5 WebApp Development"
html5_webApp_development_book_remove = driver.find_element_by_css_selector("td.product-remove [data-product_id='182']")
html5_webApp_development_book_remove.click()
# Отмена удаления книги "HTML5 WebApp Development"
html5_webApp_development_book_undo = driver.find_element_by_link_text("Undo?")
html5_webApp_development_book_undo.click()
# Увеличение количества товара до 3 шт для "JS Data Structures and Algorithm"
js_data_structures_and_algorithm_book_quantity_input = driver.find_element_by_css_selector("input[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
js_data_structures_and_algorithm_book_quantity_input.clear()
js_data_structures_and_algorithm_book_quantity_input.send_keys("3")
# Нажатие на кнопку "UPDATE BASKET"
update_basket_btn = driver.find_element_by_name("update_cart")
update_basket_btn.click()
# Проверка, что значение элемента quantity для "JS Data Structures and Algorithm" равно 3
js_data_structures_and_algorithm_book_quantity_value = driver.find_element_by_css_selector("input[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").get_attribute("value")
assert js_data_structures_and_algorithm_book_quantity_value == "3"
time.sleep(3)
# Нажатие на кнопку "APPLY COUPON"
apply_coupon_btn = driver.find_element_by_name("apply_coupon")
apply_coupon_btn.click()
time.sleep(3)
# Проверка, что возникло сообщение: "Please enter a coupon code."
WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))

driver.quit()


# '''Shop: покупка товара'''
# 1. Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# 4. Перейдите в корзину
# 5. Нажмите "PROCEED TO CHECKOUT"
#   • Перед нажатием, добавьте явное ожидание
# 6. Заполните все обязательные поля
# 7. Выберите способ оплаты "Check Payments"
#   • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# 8. Нажмите PLACE ORDER
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

path_to_extension = r'C:\Users\PC\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.13.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe',chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("https://practice.automationtesting.in/")

# Переход на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop").click()
# Скролл страницы вниз на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")
# Добавление в корзину книг "HTML5 WebApp Development"
html5_webApp_development_book = driver.find_element_by_css_selector("[data-product_id='182']")
html5_webApp_development_book.click()
time.sleep(3)
# Переход в корзину
cart = driver.find_element_by_css_selector("[title='View your shopping cart']")
cart.click()
# Нажатие на "PROCEED TO CHECKOUT"
wait = WebDriverWait(driver, 10)
proceed_to_checkout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
proceed_to_checkout_btn.click()
time.sleep(3)
# Заполнение всех обязательных полей
first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "billing_first_name")))
first_name_field.send_keys("Olga")
time.sleep(3)
last_name_field = driver.find_element_by_id("billing_last_name")
last_name_field.send_keys("Alatortseva")
time.sleep(3)
email_address_field = driver.find_element_by_id("billing_email")
email_address_field.send_keys("fortest87@bk.ru")
time.sleep(3)
phone_field = driver.find_element_by_id("billing_phone")
phone_field.send_keys("1086594329")
time.sleep(3)
country_dropdown = driver.find_element_by_css_selector(".select2-container .select2-choice .select2-arrow b").click()
country_search_field = driver.find_element_by_id("s2id_autogen1_search")
country_search_field.send_keys("France")
country_select = driver.find_element_by_css_selector(".select2-result-selectable")
country_select.click()
time.sleep(3)
address_field = driver.find_element_by_id("billing_address_1")
address_field.send_keys("France")
time.sleep(3)
postcode_field = driver.find_element_by_id("billing_postcode")
postcode_field.send_keys("24560")
time.sleep(3)
city_field = driver.find_element_by_id("billing_city")
city_field.send_keys("Bardou")
# Скролл страницы вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
# Выбор способа оплаты "Check Payments"
check_payments = driver.find_element_by_css_selector("#payment_method_cheque")
check_payments.click()
# Нажатие на "PLACE ORDER"
place_order = driver.find_element_by_id("place_order")
place_order.click()
time.sleep(5)
# Проверка, что отображается надпись "Thank you. Your order has been received."
thank_you_message = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
time.sleep(5)
# Проверка, что в Payment Method отображается текст "Check Payments"
payment_method = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.method > strong"), "Check Payments"))

driver.quit()
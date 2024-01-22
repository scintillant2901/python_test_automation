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
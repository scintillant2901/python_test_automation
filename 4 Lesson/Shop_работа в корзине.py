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
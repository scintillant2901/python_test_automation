# '''Home: добавление комментария'''
# 1. Откройте https://practice.automationtesting.in/
# 2. Проскролльте страницу вниз на 600 пикселей
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# 4. Нажмите на вкладку "REVIEWS"
# 5. Поставьте 5 звёзд
# 6. Заполните поле "Review" сообщением: "Nice book!"
# 7. Заполните поле "Name"
# 8. Заполните "Email"
# 9. Нажмите на кнопку "SUBMIT"

from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Скролл страницы вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# Клик на название книги "Selenium Ruby"
selenium_ruby_book = driver.find_element_by_css_selector(".post-160 h3").click()
# Клик на вкладку "REVIEWS"
reviews_btn = driver.find_element_by_css_selector("li.reviews_tab").click()
# Отзыв и оценка 5 звёзд
rating_review_5_stars = driver.find_element_by_css_selector("a.star-5").click()
review_field = driver.find_element_by_id("comment")
review_field.send_keys("Nice book!")
time.sleep(5)
name_field = driver.find_element_by_id("author")
name_field.send_keys("Olga")
time.sleep(5)
email_address_filed = driver.find_element_by_id("email")
email_address_filed.send_keys("fortest87@bk.ru")
time.sleep(5)
submit_btn_click = driver.find_element_by_css_selector("p.form-submit").click()

driver.quit()
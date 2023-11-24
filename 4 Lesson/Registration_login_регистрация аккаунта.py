# '''Registration_login: регистрация аккаунта'''
# 1. Откройте https://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account"
# 3. В разделе "Register", введите email для регистрации
# 4. В разделе "Register", введите пароль для регистрации
# 5. Нажмите на кнопку "Register"

from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()

# Регистрация аккаунта
my_account_menu = driver.find_element_by_link_text("My Account").click()
email_address_filed = driver.find_element_by_id("reg_email")
email_address_filed.send_keys("fortest87@bk.ru")
time.sleep(5)
password_field = driver.find_element_by_id("reg_password")
password_field.send_keys("SomeHardTest")
time.sleep(5)
register_btn = driver.find_element_by_name("register").click()

driver.quit()
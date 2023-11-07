import time
from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран, чтобы все кнопки были доступны для нажатия
# Логин в систему
driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(3) # ставим ожидание 3 секунды, чтобы страница успела прогрузиться
login = driver.find_element_by_name("username") # объявляем переменную login, задаём ей значение селектора поля логин
login.send_keys("Admin") # команда send_keys("значение") – нужна для ввода информации в поле
password = driver.find_element_by_name("password") # объявляем переменную password, задаём ей значение селектора поля пароль
password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find…. .send_keys(..))
login_btn = driver.find_element_by_css_selector(".oxd-button") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
login_btn.click() # команда click() – нужна для нажатия(клика) на элемент
driver.quit() # команда quit() – нужна для закрытия всех вкладок и завершения процесса webdriver, используется в конце
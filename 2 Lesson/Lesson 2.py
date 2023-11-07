import time
# Импортируем webdriver(набор команд для управления браузером)
from selenium import webdriver
# Вызываем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# Команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://google.ru")
time.sleep(5)
# Метод find_element_by_xpath позволяет найти нужный элемент на сайте
# Обсудим его чуть позже
# Ищем элемент поля поиска
textfield = driver.find_element_by_xpath("//textarea[@name='q']")
# Напишем текст в поле поиска
textfield.send_keys("погода на завтра")
time.sleep(5)
# Укажем путь к кнопке поиска
submit_button = driver.find_element_by_xpath("//div[@jsname='VlcLAe']//input[@class='gNO89b']")
# Нажмём на кнопку поиска с помощью команды .click()
submit_button.click() # После нажатия на кнопку должны появиться результаты поиска
time.sleep(5)
# Добавим команду, с помощью которой браузер будет сам закрываться после проведения теста
driver.quit()
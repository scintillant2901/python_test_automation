from selenium import webdriver # импортируем webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран
driver.get("https://www.dns-shop.ru/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
logo = driver.find_element_by_id("header-mobile-inner") # укажем путь к логотипу (можно было написать и без части "logo=", почему так лучше, разберём в дальнейшем)
driver.quit() # закроем драйвер в конце теста
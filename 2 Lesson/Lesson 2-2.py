from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://wiktionary.org")
driver.find_element(By.ID, "searchInput")
driver.quit()
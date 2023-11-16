from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.find_element_by_link_text("SwitchTo").click()
driver.find_element_by_link_text("Windows").click()
driver.find_element_by_css_selector(".active.tab-pane.col-md-6.col-md-offset-1.col-xs-4.col-xs-offset-1 .btn.btn-info").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.close()
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.find_element_by_link_text("Open Seperate Multiple Windows").click()
driver.find_element_by_tag_name("[onclick='multiwindow()']").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[2])
link_check = wait.until(EC.url_to_be("https://demo.automationtesting.in/Index.html"))
expected_tabs_count = 3
wait.until(EC.number_of_windows_to_be(expected_tabs_count))
actual_tabs_count = len(driver.window_handles)
print("Фактическое количество вкладок:", actual_tabs_count)
result = actual_tabs_count == expected_tabs_count
print("Открыто 3 вкладки:", result)
time.sleep(3)
email = driver.find_element_by_id("email")
email.send_keys("test@bk.ru")
time.sleep(3)
driver.find_element_by_id("enterimg").click()
wait.until(EC.url_to_be("https://demo.automationtesting.in/Register.html"))
driver.quit()
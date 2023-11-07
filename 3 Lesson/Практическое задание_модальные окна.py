from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")
time.sleep(3)
driver.find_element_by_link_text("SwitchTo").click()
time.sleep(3)
driver.find_element_by_link_text("Alerts").click()
time.sleep(3)
driver.find_element_by_css_selector("[onclick='alertbox()']").click()
time.sleep(3)
alert = driver.switch_to.alert
alert_text = alert.text
if alert_text == "I am an alert box!":
    print(alert_text)
else:
    print("Error. The alert is:", alert_text)
alert.accept()
time.sleep(3)
current_window = driver.current_window_handle
driver.execute_script("window.open();")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
time.sleep(3)
driver.get("https://demo.automationtesting.in/Alerts.html")
time.sleep(3)
driver.find_element_by_link_text("Alert with OK & Cancel").click()
time.sleep(3)
driver.find_element_by_css_selector("[onclick='confirmbox()']").click()
confirmbox = driver.switch_to.alert
time.sleep(3)
confirmbox.dismiss()
time.sleep(3)
driver.execute_script("window.open();")
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
time.sleep(3)
driver.get("https://demo.automationtesting.in/Alerts.html")
time.sleep(3)
driver.find_element_by_link_text("Alert with Textbox").click()
time.sleep(3)
driver.find_element_by_css_selector("[onclick='promptbox()']").click()
time.sleep(3)
prompt = driver.switch_to.alert
time.sleep(3)
prompt.send_keys("Ура! Задание выполнено!")
time.sleep(3)
prompt.accept()
time.sleep(5)
driver.quit()
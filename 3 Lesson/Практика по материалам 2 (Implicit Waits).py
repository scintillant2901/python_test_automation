from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
path_to_extension = r'C:\Users\PC\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.13.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe',chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.implicitly_wait(5)
driver.find_element_by_link_text("More").click()
driver.find_element_by_link_text("Dynamic Data").click()
window_header = driver.find_element_by_css_selector(".h3, h3")
window_header_text = window_header.text
assert "Loading the data Dynamically" in window_header_text
driver.find_element_by_id("save").click()
time.sleep(5)
img_element = driver.find_element_by_css_selector("#loading img")
img_link = img_element.get_attribute("src")
print(img_link)
driver.quit()
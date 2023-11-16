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
driver.find_element_by_link_text("File Upload").click()
photo = ('C:\cosmic_dream_4k.jpg')
upload = driver.find_element_by_id("input-4")
upload.send_keys(photo)
time.sleep(3)
driver.find_element_by_css_selector(".btn.btn-default.fileinput-remove.fileinput-remove-button").click()
time.sleep(3)
file = ('C:\hello.txt')
upload = driver.find_element_by_id("input-4")
upload.send_keys(file)
time.sleep(3)
driver.find_element_by_css_selector("span.close.kv-error-close").click()
upload_btn = driver.find_element_by_css_selector(".btn.btn-default.fileinput-upload.fileinput-upload-button")
if upload_btn.get_attribute("disabled"):
    print("Кнопка 'Upload' недоступна для нажатия")
else:
    print("Кнопка 'Upload' доступна для нажатия")
driver.quit()
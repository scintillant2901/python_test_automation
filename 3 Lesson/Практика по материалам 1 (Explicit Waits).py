from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
path_to_extension = r'C:\Users\PC\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.13.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe',chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.find_element_by_link_text("More").click()
driver.find_element_by_link_text("Loader").click()
run_btn = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, "loader"), "Run"))
run_btn = driver.find_element_by_id("loader").click()
lorem_text = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".modal-body"), "Lorem"))
save_changes_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer .btn+.btn"))).click()
driver.quit()
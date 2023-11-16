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
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://demo.automationtesting.in/WebTable.html")
driver.implicitly_wait(5)
driver.find_element_by_link_text("More").click()
driver.find_element_by_link_text("JQuery ProgressBar").click()
close_btn = WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog .ui-dialog-buttonpane button ")))
driver.find_element_by_id("downloadButton").click()
cancel_download_btn = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-buttonset"), "Cancel Download"))
driver.find_element_by_css_selector(".ui-dialog .ui-dialog-buttonpane button").click()
driver.find_element_by_id("downloadButton").click()
complete_text = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-content.ui-widget-content .progress-label"), "Complete!"))
driver.quit()
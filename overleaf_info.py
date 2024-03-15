import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions


email = sys.argv[1]
password = sys.argv[2]

LOGIN_URL = "https://www.overleaf.com/login"
ID_EMAIL = "email"
ID_PASSWORD = "password"

chrome_options = ChromeOptions()
chrome_options.add_argument('--disable-extensions')
# Cannot be run headless sometimes because google recaptcha might show up
# and it that case interactive user input is needed
# chrome_options.add_argument('--headless') 

driver = webdriver.Chrome(options=chrome_options)

driver.get(LOGIN_URL)

elem_email = driver.find_element(By.NAME, ID_EMAIL)
elem_password = driver.find_element(By.NAME, ID_PASSWORD)
elem_login_button = elem_password.find_element(By.XPATH, "following::div[@class='actions']//button")

elem_email.send_keys(email)
elem_password.send_keys(password)
driver.execute_script("arguments[0].click();", elem_login_button)

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.XPATH, "//footer")))

cookies = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in driver.get_cookies()])

# Look for 'Show all ' button
elem_show_all = driver.find_element(By.XPATH, "//button[contains(text(), 'Show all')]")

if(elem_show_all):
    driver.execute_script("arguments[0].click();", elem_show_all)
    # Wait until show more button disappears => makes sure all rows in table are loaded
    wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, "button.project-list-load-more-button")))  

project_elements = driver.find_elements(By.XPATH, '//*[@data-project-id]')
project_ids_string = ','.join([element.get_attribute('data-project-id') for element in project_elements])

print(cookies+"\n"+project_ids_string)

driver.quit()
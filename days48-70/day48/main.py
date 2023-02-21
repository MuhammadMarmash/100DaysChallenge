from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

running_time = input("enter the time you want to run the program in seconds: ")
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[text()="English"]')))
    element.click()
except TimeoutError:
    driver.quit()

cookie = driver.find_element(By.ID, "bigCookie")

try:
    with open(file="save_key.txt", mode="r") as file:
        key = file.read()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'prefsButton'))).click()

    import_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Import save"]')))
    import_.click()

    import_area = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'textareaPrompt')))
    import_area.send_keys(key)

    driver.find_element(By.XPATH, '//a[text()="Load"]').click()
    driver.find_element(By.CSS_SELECTOR, '.close.menuClose').click()

except FileNotFoundError:
    pass
timer = time.time() + int(running_time)
while time.time() < timer:
    t_end = time.time() + 10
    while (time.time() < t_end) and (time.time() < timer):
        cookie.click()
    upgrades = driver.find_elements(By.CSS_SELECTOR, '.upgrade.enabled')
    for upgrade in upgrades[::-1]:
        upgrade.click()
    upgrades = driver.find_elements(By.CSS_SELECTOR, '.unlocked.enabled')
    for upgrade in upgrades[::-1]:
        upgrade.click()

options = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[text()="Options"]')))
options.click()

export = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Export save"]')))
export.click()

export_key = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'textareaPrompt'))).text

with open(file="save_key.txt", mode="w") as file:
    file.write(export_key)

driver.quit()

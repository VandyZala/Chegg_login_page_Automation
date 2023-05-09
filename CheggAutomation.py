import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

driver.get("https://expert.chegg.com/qna/authoring/answer")
driver.find_element(By.ID,"username").send_keys("<Enter Your Chegg email>")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.ID,"password").send_keys("<Enter the password>")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.maximize_window()
time.sleep(20)


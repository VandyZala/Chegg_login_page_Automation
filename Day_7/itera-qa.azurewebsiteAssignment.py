from email.mime import image

from selenium import webdriver
from selenium.webdriver.common.by import By
from requests import request
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://itera-qa.azurewebsites.net/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Test Automation").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/input[1]").send_keys("xyz")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("8980528798")
driver.find_element(By.ID,"email").send_keys("xyz@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("xyz@123")
driver.find_element(By.ID,"address").send_keys("A-56,sdjsd nsjds, ksdsk-466656")
driver.find_element(By.CSS_SELECTOR,"button[name='submit']").click()
driver.find_element(By.XPATH,"//input[@id='female']").click()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname =='monday' or weekname == 'sunday' or weekname == 'tuesday':
        checkbox.click()

drpcity=Select(driver.find_element(By.XPATH,"//select[@class='custom-select']"))

alloptions = drpcity.options

for opt in alloptions:
    print(opt.text)

drpcity.select_by_value("3")

driver.find_element(By.XPATH,"//label[normalize-space()='1 year']").click()
driver.find_element(By.XPATH,"//div[@class='card-body']//div[2]//div[1]").click()

assdsdss

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, value="fName")
fName.send_keys("Abhishek")
lName = driver.find_element(By.NAME, value="lName")
lName.send_keys("Nayak")
email = driver.find_element(By.NAME, value="email")
email.send_keys("Abhishek.Nayak@rockstar.com")
btn = driver.find_element(By.CLASS_NAME, value="btn")
btn.click()

driver.quit()
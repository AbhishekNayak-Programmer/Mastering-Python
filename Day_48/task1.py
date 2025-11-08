from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

time_items = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
obj = {}

for i in range(0,len(event_names)):
    obj[i] = {'time': time_items[i].text ,'name': event_names[i].text}

print(obj)

driver.quit()
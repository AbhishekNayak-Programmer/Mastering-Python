from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('dtach', True)

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(article_count.text)
article_count.click()

person = driver.find_element(By.LINK_TEXT, value="Pages")
person.click()

search = driver.find_element(By.NAME, value="from")
search.send_keys("Abhishek Nayak", Keys.ENTER)
# search.send_keys(Keys.ENTER)


# driver.quit()
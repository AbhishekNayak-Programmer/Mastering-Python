from selenium import webdriver

# Keep chrome browswer open after program finishes
chorme_options = webdriver.ChromeOptions()
chorme_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chorme_options)
driver.get("https://www.amazon.in/")




# driver.close() # Closes a single tab when page loads
driver.quit() # Closes the browser 
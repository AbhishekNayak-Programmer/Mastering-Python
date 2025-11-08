from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome browswer open after program finishes
chorme_options = webdriver.ChromeOptions()
chorme_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chorme_options)
driver.get("https://www.amazon.in/Titan-Silicone-Tailored-Activity-Charging/dp/B0F5HS5XWK/ref=sr_1_3_sspa?crid=18JOZF2AEAO2A&dib=eyJ2IjoiMSJ9._yaaPrwSnEDKr40QrFdbxV9M-xh5Mf5r_cgqLF3-yZy14ehITpXkUuX5uGc9Xy-y-EC8fphV1zrh7WAdG2n9bK2xO6qHa4a79LNj-WjeYUQbZWHKN-51Fv_qD5pB1zNofEkvdJTC1lW-8RiwRJTE59wZzMASHavE1ohh1sqj2bRvDMEvLv_YDFg8el2OLvm_TmVXrYy5VJde3xgiMYjq0-NNiIj8Z-DiVVctFg_YSn7BMc4vdosLGUsALDk3HfTDb4Br_v2Xpnjl0qMGZU1kjjIs7xiy_68kqWJNaGBY-HQ.K9oBJNO0wgKzYMfPo5R-WTFDf1yYmTmowBLJfOgFEng&dib_tag=se&keywords=watch%2Bfor%2Bman&qid=1762482945&sprefix=watch%2Caps%2C214&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

# Finding using CLASSNAME
price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
print(f'The price is Rs-{price.text}')

# Finding using NAME
search_input_element = driver.find_element(By.NAME, value="field-keywords")
placeholder = search_input_element.get_attribute("placeholder")
print(f"The PlaceHolder is {placeholder}")

# Finding using ID
buy_now_btn = driver.find_element(By.ID, value="buy-now-button")
print(buy_now_btn)
print(buy_now_btn.size)

# Finding using CSS SELECTOR
headline = driver.find_element(By.CSS_SELECTOR, value=".a-size-large span")
print(headline.text)

# Finding using X Path
discount_percentage = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]')
print(discount_percentage.text)

# YOU CAN ALSO USES FIND ELEMENTS FOR MULTIPLE MATCHING ELEMENTS 

# driver.close() # Closes a single tab when page loads
driver.quit() # Closes the browser 
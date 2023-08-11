import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)


driver.get("https://www.makemytrip.com/")
driver.maximize_window()

driver.find_element("xpath", '//p[text()="Login or Create Account"]').click()

# string : name
# 	driver.switch_to.frame(frame_name)

# number: index

# webelement: locate iframe

# web element
# time.sleep(5)
# web_element = driver.find_element("xpath", '//iframe[@title="Sign in with Google Button"]')
# driver.switch_to.frame(web_element)
# driver.find_element("xpath", '//div[@id="container"]').click()


# index
time.sleep(5)
driver.switch_to.frame(0)
# driver.find_element("xpath", '//div[@id="container"]').click()


# switching_back to parent webpage
"""
1. switch_to.parent_frame()  --> switches the control to immediate parent
2. switch_to.default_content() --> switches the control to main page
"""

# driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.find_element("xpath", '//input[@id="username"]').send_keys("abc@gmail.com")
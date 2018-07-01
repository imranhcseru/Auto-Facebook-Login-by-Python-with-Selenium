from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.facebook.com')
email = ""#Enter facebook email address or phone number or user name
password = ""#Enter your facebook Password
email_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("pass")
email_input.send_keys(email)
password_input.send_keys(password)
login_button = driver.find_element_by_id("loginbutton")
login_button.click()
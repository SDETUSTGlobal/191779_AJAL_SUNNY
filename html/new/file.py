from selenium import webdriver
import time

print("test case started")
# open Google Chrome browser
driver = webdriver.Chrome("C:/Users/ustjavasdetb309/Downloads/chromedriver_win32/chromedriver.exe")
# maximize the window size
driver.maximize_window()
# delete the cookies
driver.delete_all_cookies()
# navigate to the url
driver.get("http://127.0.0.1:5000/")
time.sleep(2)
# identify the user name text box and enter the value
driver.find_element_by_id("name").send_keys("Ajal")
time.sleep(2)
driver.find_element_by_id("uid").send_keys("191779")
time.sleep(1)
driver.find_element_by_id("cname").send_keys("Ust")
time.sleep(2)
driver.find_element_by_id("cmail").send_keys("aj@ust-global.com")
time.sleep(1)
driver.find_element_by_id("password").send_keys("1234")
# Click on submit button
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[6]/button").click()
time.sleep(5)

# close the browser
driver.close()
print("Ust login has been successfully completed")
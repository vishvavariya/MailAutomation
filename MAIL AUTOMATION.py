from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random 
  

# create a new Firefox session
driver = webdriver.Firefox(executable_path = 'E:\Softwares\geckodriver.exe')
driver.maximize_window()

# Navigate to the application home page
driver.get("https://login.yahoo.com/?.src=ym&.partner=none&.lang=en-IN&.intl=in&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.intl%3Din%26.lang%3Den-IN%26.partner%3Dnone%26.src%3Dfp")

username = driver.find_element_by_id("login-username")
username.send_keys("YOUR_EMAIL_ID")
username.send_keys(Keys.RETURN)
driver.implicitly_wait(20)
password = driver.find_element_by_id("YOUR_PASSWORD")
password.send_keys("varii9898")
password.send_keys(Keys.RETURN)
driver.implicitly_wait(20)
driver.find_element_by_css_selector("a.e_dRA").click()
wishes = ["Hello","Hi"]
to = driver.find_element_by_id("message-to-field").send_keys("variyavishva98@yahoo.com")
word = random.choice(wishes)
driver.find_element_by_css_selector("input.q_T:nth-child(1)").send_keys(word)
word = random.choice(wishes)
driver.find_element_by_css_selector(".rte").send_keys(word)

driver.find_element_by_css_selector(".q_Z2aVTcY").click()


from selenium import webdriver
from selenium.webdriver.ie.options import ElementScrollBehavior
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://instagc.com/watch/")

folder = driver.find_element_by_xpath("//input[@name='username']")
folder.send_keys("")

folder = driver.find_element_by_xpath("//input[@name='password']")
folder.send_keys("")

folder = driver.find_element_by_xpath("//*[@id='login']/form/section/div[3]/button")
folder.click()

folder = driver.find_element_by_xpath("//*[@id='playlist1']/h2/button[1]")
folder.click()


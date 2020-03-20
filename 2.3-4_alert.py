from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button1 = browser.find_element_by_tag_name("button")
	button1.click()

	time.sleep(2)

	confirm = browser.switch_to.alert
	confirm.accept()

	time.sleep(1)

	x = browser.find_element_by_id("input_value").text
	y = calc(x)

	ans = browser.find_element_by_id("answer")
	ans.send_keys(y)

	button2 = browser.find_element_by_tag_name("button")
	button2.click()

finally:
	time.sleep(10)
	browser.quit()


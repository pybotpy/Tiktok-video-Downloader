from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.tiktok.com/en/")
driver.maximize_window()
driver.refresh()
driver.refresh()
driver.refresh()
while True:
	driver.get("https://www.tiktok.com/en/")
	time.sleep(2)
	#-------------------------------------get video link----------------------------------------------------------------------------
	driver.find_element_by_xpath("//video[@class='tiktok-lkdalv-VideoBasic e1yey0rl4']").click()
	time.sleep(2)
	copy_input = driver.find_element_by_xpath("//button[@class='tiktok-iyi993-ButtonCopyLink e1i8l1796']").click()
	time.sleep(1)
	#--------------------------------------go to download website--------------------------------------------------------------------
	driver.get("https://dltik.com/")
	#--------------------------------------download video----------------------------------------------------------------------------
	driver.find_element_by_css_selector("#txt-input-url").send_keys(Keys.CONTROL+ "v");
	time.sleep(1)
	driver.find_element_by_xpath("//button[@id='btn-submit-link']//i[@class='fa fa-download']").click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="download-section"]/div[3]/a[1]').click()
	time.sleep(5)
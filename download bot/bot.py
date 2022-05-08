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


	










#//a[@title='Download Server 1']














#.send_keys(Keys.CONTROL+ "v");

#sendKeys(Keys.DOWN
#find_element_by_xpath("").send_keys(Keys.ENTER)

#sign_up = driver.find_element_by_name('email').send_keys('hi')

#driver.find_element_by_css_selector("CSS Selectors")

#driver.find_element_by_xpath("//button[@type='submit']").click()
#find_element(By.ID,"searchinput")
#driver.find_element_by_xpath("//div[@id='sid4']//input[@placeholder='Enter Video URL']").send_keys('https://www.tiktok.com/@premiumfollower/video/7092698468354952453?is_from_webapp=1&sender_device=pc&web_id=7092944585303033350')

#driver.find_element_by_name('input1').send_keys('hi')


#//*[@id="__PWS_ROOT__"]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[3]/button[1]/div[1]/div[1]
#https://www.minuteinbox.com/


#close tab c+wpyautogui.press('enter')

#//a[.='Copy']

import time
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

qq = ''
password = ''


name = []
browser = webdriver.Chrome()
url = 'https://y.qq.com'
browser.get(url)
time.sleep(10)

browser.find_element_by_xpath("/html/body[@class='os_mac']/div[@class='mod_header']/div[@class='section_inner']/div[@class='header__opt']/span[@class='mod_top_login']/a[@class='top_login__link js_login']").click()
browser.switch_to.frame("frame_tips")
browser.find_element_by_id("switcher_plogin").click()

username = browser.find_element_by_id('u')
password = browser.find_element_by_id('p')

username.send_keys(q)
password.send_keys(password)
browser.find_element_by_id("login_button").click()

sea_url = 'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w='
time.sleep(3)
fild = []
for x in name:
	try:
		url = sea_url+x.encode('utf-8')
		browser.get(url)
		time.sleep(1)
		actions = ActionChains(browser)
		actions.click(browser.find_element_by_css_selector("i.list_menu__icon_add")).perform()
		time.sleep(1)
		lists = browser.find_elements_by_css_selector("li.operate_menu__item")
		lists[1].click()  
		time.sleep(1)
	except :
		try:
			browser.find_element_by_css_selector("a.popup__close").click()
		except:
			pass
		else:
			pass
		fild.append(x)
		print x.encode('utf-8')
	else:
		pass

print fild
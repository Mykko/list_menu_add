# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup 
#import time
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


headers = { 
	'Referer':'http://music.163.com/', 
	'Host':'music.163.com', 
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0', 
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' 
	} 
play_url = 'http://music.163.com/playlist?id=488400576' 
s = requests.session() 

t = BeautifulSoup(s.get(play_url,headers = headers).content, "html.parser")

main = t.find('ul',{'class':'f-hide'}) 
name = []
for music in main.find_all('a'): 
	song_url = 'http://music.163.com' + music.get('href')
	t = BeautifulSoup(s.get(song_url,headers = headers).content, "html.parser")
	t = t.find('head')
	t = t.find('title')
	name_text = t.text.replace(' -' + t.text.split('-')[-2] + '-' + t.text.split('-')[-1],'')
	name.append(name_text) 

print name
print len(name)

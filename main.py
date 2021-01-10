from selenium import webdriver 
import time 
from cred2 import username,password
chrome = webdriver.Chrome()
time.sleep(1)

chrome.maximize_window()

#goes to instagram
chrome.get("https://www.instagram.com/")
time.sleep(4)
#enters username 
usern = chrome.find_element_by_name("username")     
usern.send_keys(username)    
  
#enters password
passw = chrome.find_element_by_name("password")     
passw.send_keys(password)

time.sleep(2) 
  
log_cl = chrome.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")     
log_cl.click()   
time.sleep(3)
 
log_cla = chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")     
log_cla.click()  
time.sleep(3)

log_clb = chrome.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")     
log_clb.click()   
time.sleep(3)
#clicks on first story
log_clc = chrome.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[4]/div/button/div[1]/span/img")     
log_clc.click()   
time.sleep(3)

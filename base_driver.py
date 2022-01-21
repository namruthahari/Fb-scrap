 # import webdriver
from struct import unpack
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from utilities.utils import Utils

PATH = "C:\Program Files (x86)\chromedriver.exe"
# create webdriver object
driver = webdriver.Chrome(PATH)

# get website
driver.get("https://en-gb.facebook.com/BurnsNursingandRehab/")

# Mazimize current window
driver.maximize_window()

# waiting web-page to load
delay = 3 # seconds
WebDriverWait(driver, delay).until(lambda x: x.find_element_by_xpath("//a[@aria-label='Facebook']//*[name()='svg']"))

#scroll-down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# close pop-up
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Close']")))
button = driver.find_element_by_xpath("//div[@aria-label='Close']")
button.click()

# scroll-up
driver.execute_script("scrollBy(0,-500);")
time.sleep(3)

# wait until element visible
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,'@')))

# get element 
data = driver.find_element_by_partial_link_text('@').get_attribute("href")
  
# print complete element
print(data)

# close browser
driver.close()

# .oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.py34i1dx
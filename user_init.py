import csv
import pandas as pd
import time
from struct import unpack
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""initialization"""

# final output csv file name
output_file = 'FBProfiles.csv'
#title names
title_1 = 'Page Name'
title_2 = 'FB URL'
title_3 = 'Email'

# input data csv file name
input_file = 'NH_ProviderInfo_Nov2021.csv'

# create webdriver object
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#count
count=0

"""open new .csv file"""

writer = csv.writer(open(output_file, 'w')) # preparing csv file to store parsing result later
writer.writerow([title_1, title_2, title_3]) # writing titles names

"""read data from exsisting .csv file"""

file = pd.read_csv(input_file, encoding='cp1252')
df = pd.DataFrame(file)

# computing number of rows
rows = len(df.axes[0])
# computing number of columns
cols = len(df.axes[1])
  
print(df)
print("Number of Rows: ", rows)
print("Number of Columns: ", cols)

# columns
for index, row in df.iterrows():
    page_name = row['Provider Name']
    page_name = page_name.capitalize()

    bad_chars = [';',' ',',', ':', '!', "*"]
    for i in bad_chars :
        page_name = page_name.replace(i, '')

    def get_url(page_name):
        return "https://en-gb.facebook.com/{}/".format(page_name)
    fb_url = get_url(page_name)

    # print name and url in console to check through loop
    # print(page_name)
    print(fb_url)

    # get website
    driver.get(fb_url)

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
    email_id = driver.find_element_by_partial_link_text('@').get_attribute("href")
  
    # print complete element
    print(email_id)

    # close browser
    driver.close()

    #data value getting
    count = count+1
    final_page_name = page_name
    final_email_id = email_id
    final_fb_url = email_id
    
    # print to console for testing purpose
    print("\n")
    print(count)
    print(final_page_name)
    print(final_fb_url)
    print(final_email_id)
    print("\n")

    #writing final data to csv
    writer.writerow([final_page_name, final_fb_url, final_email_id])
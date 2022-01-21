import time
from selenium import webdriver
import csv
import excel_read

writer = csv.writer(open('FBProfiles.csv', 'w')) # preparing csv file to store parsing result later
writer.writerow(['page_name', 'fb_url', 'email_id'])

page_name = "hi"
email_id = "hi"
fb_url = "hi"

# print to console for testing purpose
print(page_name)
print(fb_url)
print(email_id)
writer.writerow([page_name, fb_url, email_id])
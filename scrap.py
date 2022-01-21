from facebook_page_scraper import Facebook_scraper

#instantiate the Facebook_scraper class

page_name = "BurnsNursingandRehab"
browser = "firefox"
proxy = "IP:PORT" #if proxy requires authentication then user:password@IP:PORT
facebook_ai = Facebook_scraper(page_name,browser,proxy=proxy)

#call the scrap_to_json() method

json_data = facebook_ai.scrap_to_json()
print(json_data)

#call scrap_to_csv(filename,directory) method

filename = "data_file"  #file name without CSV extension,where data will be saved
directory = "E:\Work" #directory where CSV file will be saved
facebook_ai.scrap_to_csv(filename,directory)

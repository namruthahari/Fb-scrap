import pandas as pd

# csv file name
# filename = r"E:\Work\web_scraper\facebook_page_scraper\NH_ProviderInfo_Nov2021.csv"
filename = pd.read_csv('NH_ProviderInfo_Nov2021.csv', encoding='cp1252')
# with open(filename, 'a') as f:
df = pd.DataFrame(filename)

total_rows = len(df.axes[0])
total_cols = len(df.axes[1])
  
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

    def remove_space(page_name):
        return page_name.replace(" ", "")
    
    page_name = remove_space(page_name)    
    # print(page_name)

    def get_url(page_name):
        return "https://en-gb.facebook.com/{}/".format(page_name)
    
    fb_url = get_url(page_name)
    print(fb_url)


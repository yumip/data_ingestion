from bs4 import BeautifulSoup as bs
import requests
# outpath = '/Users/MichaelHu/Documents/Internship/property_values'
url = "https://valuation.property.nsw.gov.au/embed/propertySalesInformation"
print('Reading: ', url)
req = requests.get(url)
soup = bs(req.text, 'lxml')
print(soup.title)
date_files = soup.find_all('a', class_='btn')
# print(date_files)
prop_file=[]
for dates in date_files:
    # print(dates.a)
    
    prop_file.append([dates.text, dates.get('href')])
# print(date_files)
print(prop_file)

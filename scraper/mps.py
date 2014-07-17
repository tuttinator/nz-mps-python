import requests
from bs4 import BeautifulSoup

# Get the HTML of all the Current MPs
result = requests.get('http://www.parliament.nz/en-nz/mpp/mps/current?Criteria.ViewAll=1')

soup = BeautifulSoup(result.text)

table_rows = soup.find_all('div#content div.copy form table tbody tr')

print(table_rows)

#print(result.text)

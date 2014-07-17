import requests
from bs4 import BeautifulSoup
from mp import MP

# Get the HTML of all the Current MPs
result = requests.get('http://www.parliament.nz/en-nz/mpp/mps/current?Criteria.ViewAll=1')

soup = BeautifulSoup(result.text)

table_rows = soup.find('tbody').find_all('tr')

mps = []

for row in table_rows:
    cells = row.find_all('td')
    a_tag = cells[0].find('a')

    mps.append(MP(a_tag.string, a_tag.get('href'), cells[1].string))

print(mps)

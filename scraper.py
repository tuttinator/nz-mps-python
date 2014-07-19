import requests
from bs4 import BeautifulSoup
from models.mp import MP
from database import db_session

mp_list_url = 'http://www.parliament.nz/en-nz/mpp/mps/current?Criteria.ViewAll=1'

print('Fetching ' + mp_list_url)
result = requests.get(mp_list_url)

soup = BeautifulSoup(result.text)

table_rows = soup.find('tbody').find_all('tr')

mps = []

for row in table_rows:
    cells = row.find_all('td')
    a_tag = cells[0].find('a')

    mp = MP(a_tag.string, a_tag.get('href'), cells[1].string)

    print('Fetching ' + mp.details_url)
    req = requests.get(mp.details_url)
    detail_soup = BeautifulSoup(req.text)
    image_td = detail_soup.find('td', class_='image')
    if(image_td != None):
        src = image_td.find('img').get('src')
        mp.image_from_src(src)
    else:
        print('  .... no image for this MP')

    mps.append(mp)

db_session.query(MP).delete()

for mp in mps:
    db_session.add(mp)

db_session.commit()

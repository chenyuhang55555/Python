import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://sockslist.net/list/proxy-socks-5-list/')

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table', attrs={"class": "proxytbl"})

res = []
table_rows = table.find_all('tr')
for tr in table_rows:
    tds = tr.find_all('td')
    # print(tds.__dict__.keys())
    row = [td.text.strip() for td in tds if td.text.strip() and td.attrs["class"][0] in ["t_ip", "t_country", "t_type", "t_checked"]]
    if row:
        # print(row)
        res.append(row)
df = pd.DataFrame(res, columns=["ip", "country", "type", "checked"])
print(df)
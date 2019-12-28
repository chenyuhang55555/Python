
'''
Web scraping free socks5 proxies from https://sockslist.net/list/proxy-socks-5-list/.
Write them into /etc/proxychains.conf
'''

from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

## config
proxychainsconf = "fake_etc_proxychains.conf"
safe_zone_delimiter = "######### Safe Zone Ends Here #########\n"
preferred_country = ["Netherlands", "Japan", "China"]
preferred_socks = ["5", "4/5"]

## 1. web scraping
session = HTMLSession()
r = session.get('https://sockslist.net/list/proxy-socks-5-list/')
# r = requests.get('https://sockslist.net/list/proxy-socks-5-list/')
r.html.render()
soup = BeautifulSoup(r.html.html, 'html.parser')
table = soup.find('table', attrs={"class": "proxytbl"})

res = []
table_rows = table.find_all('tr')
for tr in table_rows:
    tds = tr.find_all('td')
    row = [td.contents[-1].strip() for td in tds if
           td.text.strip() and td.attrs["class"][0] in ["t_ip", "t_port", "t_country", "t_type", "t_checked"]]
    if row:
        res.append(row)
df = pd.DataFrame(res, columns=["ip", "port", "country", "type", "checked"])
df = df[df.type.isin(preferred_socks)]

n_valid = df.shape[0]
n_preferred = df.country.isin(preferred_country).sum()
print(df)
print("Fetched {} valid proxies.".format(n_valid))
print("{} preferred.".format(n_preferred))

df_preferred = df[df.country.isin(preferred_country)]
df_unpreferred = df[~df.country.isin(preferred_country)]
df_sorted = df_preferred.append(df_unpreferred)
top5 = df_sorted[:5] if df_sorted.shape[0] >= 5 else df_sorted

## 2. read & write to proxychainsconf
target_lines = []
for _, row in top5.iterrows():
    target_str = "socks5 {ip} {port}".format(ip=row.ip, port=row.port)
    print(target_str)
    target_lines.append(target_str + "\n")

fr = open(proxychainsconf, "r")
lines = fr.readlines()
if safe_zone_delimiter in lines:
    tail_pos = lines.index(safe_zone_delimiter)
    add_delimiter = 0
else:
    tail_pos = len(lines) - 1
    add_delimiter = 1
fr.close()

fw = open(proxychainsconf, "w")
fw.writelines(lines[:tail_pos + 1] + [safe_zone_delimiter] * add_delimiter + target_lines)
fw.close()

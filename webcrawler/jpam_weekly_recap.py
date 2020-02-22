
from bs4 import BeautifulSoup 
from requests_html import HTMLSession
import requests

session = HTMLSession()
r = session.get("https://am.jpmorgan.com/us/en/asset-management/gim/adv/insights/weekly-market-recap")
r.html.render()
soup = BeautifulSoup(r.html.html, 'html.parser')
a_string = soup.find(string="View the recap")
link=a_string.find_parents("a")[0]
pdf_url="https://am.jpmorgan.com"+link.get("href")

r_with_pdf = requests.get(pdf_url)

from datetime import date
from datetime import datetime
from datetime import timedelta
from pathlib import Path
#today_str = date.today().strftime("%Y%m%d")
report_day_str = (date.today() - timedelta(date.today().weekday())).strftime("%Y%m%d")
home = str(Path.home())
output_dir = "/".join([home,"Documents/Investment/Macro/JPAM/Weekly Recap"])
output_file = "/".join([output_dir,"weekly_market_recap{}.pdf".format(report_day_str)])
with open(output_file,"wb") as pdf:
    pdf.write(r_with_pdf.content)

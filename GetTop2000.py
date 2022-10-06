import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#import numpy as np
#import pandas as pd
from urllib.request import urlopen

company = list()
for i in range(1,21):
  url = "https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap/?page={}/".format(i)
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  object = soup.find(id="cmkt")
  items = object.find_all(class_="company-code")
  for i in items:
    company.append(i.get_text())
with open("Top2000.txt", "w") as output:
    for i in company:
        output.write(str(i)+'\n')
    
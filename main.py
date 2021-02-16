import requests
import pandas as pd

r = requests.get('http://www.dougstats.com/20-21RD.txt')
lines = r.text.split('\n')
headers = lines[0].split()
data = [dict(zip(headers, line.split())) for line in lines[1:]]
print(pd.DataFrame(data).dropna(how='all'))




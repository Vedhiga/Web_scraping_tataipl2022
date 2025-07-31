import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

# Get table headers
table = soup.find("table", class_="ih-td-tab w-100 auction-tbl")
headers = [th.text.strip() for th in table.find_all("th")]
df = pd.DataFrame(columns=headers)

# Extract rows
rows = table.find_all("tr")

for i in rows[1:]:
    tds = i.find_all("td")
    if len(tds) < 4:
        continue

    first_column = tds[0].get_text(separator=" ", strip=True)
    other_columns = [td.text.strip() for td in tds[1:]]
    row = [first_column] + other_columns

    # ✅ Ensure column count matches
    if len(row) == len(df.columns):
        df.loc[len(df)] = row

print(df)

df.to_csv("C:\\Users\\Vedhiga V.B\\OneDrive\\Desktop\\project2025\\AI music\\Web scraping\\tata_ipl.csv")

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url = "https://www.iplt20.com/auction/2022"
# r= requests.get(url)
# # print(r)

# soup = BeautifulSoup(r.text,'lxml')
# # print(soup)

# table = soup.find("table", class_="ih-td-tab w-100 auction-tbl")
# # print(table)
# title = table.find_all("th")
# # print(title)
# headers = []
# for i in title:
#     name = i.text
#     headers.append(name)

# # print(headers)

# df = pd.DataFrame(columns=headers)
# # print(df)

# rows = table.find_all("tr")
# print(rows)
# # for i in rows[1:]:
# #     first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic")
# #     team_name = first_td.get_text(separator=" ", strip=True) if first_td else "N/A"

# #     #first_td=i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
# #     data = i.find_all("td")[1:]
# #     row = [tr.text for tr in data]
# #     row.insert(0,first_td)
# #     l=len(df)
# #     df.loc[l]=row
# # print(df)

# # tds = i.find_all("td")
# # div = tds[0].find("div", class_="ih-pt-ic") if tds else None

# # if div:
# #     first_td = div.text.strip()
# #     data = tds[1:]
# #     row = [tr.text.strip() for tr in data]
# #     row.insert(0, first_td)
# #     df.loc[len(df)] = row
# # print(df)

# # tds = i.find_all("td")
# # div = tds[0].find("div", class_="ih-pt-ic") if tds else None

# # if div:
# #     team_name = div.get_text(separator=" ", strip=True)
# # else:
# #     team_name = "N/A"

# # data = [td.text.strip() for td in tds[1:]]
# # data.insert(0, team_name)
# # df.loc[len(df)] = data


# for i in rows[1:]:
#     tds = i.find_all("td")
#     if len(tds) < 4:
#         continue

#     # Extract entire text from 1st <td> (which includes SR. NO. + TEAM)
#     td_text = tds[0].get_text(separator=" ", strip=True).split()

#     # SR. NO. is the first word, TEAM is the rest
#     sr_no = td_text[0]
#     team_name = " ".join(td_text[1:])

#     # Extract other columns
#     data = [td.text.strip() for td in tds[1:]]
    
#     # Create the full row: [SR. NO., TEAM, ...]
#     row = [sr_no, team_name] + data
#     df.loc[len(df)] = row

# print(df)

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
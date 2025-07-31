# 🏏 IPL Auction 2022 – Web Scraping Project

Welcome! This project is all about extracting structured data from the official **IPL 2022 Auction page** using **Python, BeautifulSoup, and pandas**.

We fetch data like team names, funds remaining, overseas players, and total squad size — all from the auction table on [ipl20.com](https://www.iplt20.com/auction/2022).

---

## 📑 Table of Contents

- [📌 Overview](#-overview)
- [📚 Concepts Covered](#-concepts-covered)
- [🚀 Project Workflow](#-project-workflow)
  - [1. Setup & Imports](#1-setup--imports)
  - [2. Sending the Request](#2-sending-the-request)
  - [3. Parsing the HTML](#3-parsing-the-html)
  - [4. Extracting Table Data](#4-extracting-table-data)
  - [5. Cleaning & Structuring the Data](#5-cleaning--structuring-the-data)
  - [6. Final Output](#6-final-output)
- [🛠️ Tools & Libraries](#-tools--libraries)
- [📸 Screenshots](#-screenshots)
- [🧠 What I Learned](#-what-i-learned)
- [📌 Conclusion](#-conclusion)

---

## 📌 Overview

This project is a simple and beginner-friendly exercise in web scraping using real-world sports data. We use Python to collect tabular data from the IPL website and convert it into a usable DataFrame.

You can use this as a base for data visualization, analysis, or just to learn how to scrape HTML tables.

---

## 📚 Concepts Covered

- Web Scraping basics
- HTML parsing with BeautifulSoup
- Working with `<table>` and `<tr>` tags
- DataFrame creation with pandas
- Cleaning and debugging common web scraping issues

---

## 🚀 Project Workflow

### 1. Setup & Imports

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

2. Sending the Request
We send a GET request to the IPL 2022 auction page:

python
Copy
Edit
url = "https://www.iplt20.com/auction/2022"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
3. Parsing the HTML
We locate the auction table from the page using class names:

python
Copy
Edit
table = soup.find("table", class_="ih-pg-sq-tbl")
4. Extracting Table Data
We loop through the rows and extract data:

python
Copy
Edit
data = []
for row in table.find_all("tr")[1:]:  # Skip header
    cols = row.find_all("td")
    if cols:
        data.append([col.text.strip() for col in cols])
5. Cleaning & Structuring the Data
We define column names (excluding SR. NO. as it's not meaningful) and build the DataFrame:

python
Copy
Edit
columns = ["TEAM", "FUNDS REMAINING", "OVERSEAS PLAYERS", "TOTAL PLAYERS"]
df = pd.DataFrame(data, columns=["SR. NO."] + columns)

6. Final Output
bash
Copy
Edit
   SR. NO.                     TEAM FUNDS REMAINING  OVERSEAS PLAYERS  TOTAL PLAYERS
0     N/A      Chennai Super Kings     ₹2,95,00,000                 8             25
1     N/A           Delhi Capitals       ₹10,00,000                 7             24
...   ...                       ...               ...               ...            ...
```

🛠️ Tools & Libraries
requests – for sending HTTP requests

BeautifulSoup – for parsing HTML content

pandas – for tabular data manipulation

Jupyter Notebook or any IDE (like VS Code)

🧠 What I Learned
How to navigate HTML content programmatically

How to debug common issues like:

NoneType errors while locating table

Mismatched columns during DataFrame creation

The importance of data cleaning, even for structured websites

📌 Conclusion
This was a fun and insightful project to get hands-on with web scraping and real-world sports data 🏆
I plan to extend this into an interactive IPL dashboard using Plotly or Streamlit.

Feel free to fork, suggest changes, or build something new with this!

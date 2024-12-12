import pandas as pd
import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the website
url = 'https://www.bseindia.com/sensex/code/53'  # Replace with the target URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')


data = []
table = soup.find('div')  # Adjust as necessary
for row in table.find_all('a'):
    cols = row.find_all('a')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Step 3: Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('products.csv', index=False, header=True)  # Adjust header as needed


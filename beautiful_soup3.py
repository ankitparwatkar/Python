import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?gs_ssp=eJzj4tLP1TdILkqpqihQYDRgdGDw4kjLySzITiwqAQBm2Afs&q=flipkart&rlz=1C1CHBF_en-GBIN1109IN1110&oq=flip&gs_lcrp=EgZjaHJvbWUqGAgBEC4YQxiDARjHARixAxjRAxiABBiKBTIRCAAQRRg5GEMYsQMYgAQYigUyGAgBEC4YQxiDARjHARixAxjRAxiABBiKBTINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDIPCAUQABhDGLEDGIAEGIoFMg8IBhAuGEMYsQMYgAQYigUyBwgHEAAYjwIyBwgIEAAYjwLSAQk1NzgwajBqMTWoAgiwAgHxBdJlTWqy4Dtz&sourceid=chrome&ie=UTF-8"  # Replace with the actual URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print("Failed to fetch the page")
    
soup = BeautifulSoup(response.text, "html.parser")

# Print the first 500 characters to see the HTML content
print(soup.prettify()[:500])

# Find the first table on the page
table = soup.find("tr")

# Extract table headers
headers = [header.text.strip() for header in table.find_all("tr")]

# Extract table rows
data = []
table=soup.find("table")
for row in table.find_all("tr"):  # Skipping header row
    columns = row.find_all("td")
    row_data = [column.text.strip() for column in columns]
    data.append(row_data)

# Convert to Pandas DataFrame
df = pd.DataFrame(data, columns=headers)

# Display the first few rows
print(df.head())

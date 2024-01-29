from bs4 import BeautifulSoup
import requests

# Define the URL of the CoinMarketCap website
url = "https://coinmarketcap.com/"

# Make a request to the website and retrieve the HTML content
result = requests.get(url).text

# Parse the HTML content using BeautifulSoup
doc = BeautifulSoup(result, "html.parser")

# Access the <tbody> element containing the cryptocurrency information
tbody = doc.tbody

# Extract the list of <tr> (table rows) elements from the <tbody>
trs = tbody.contents

# Loop through the first 10 <tr> elements (representing the top 10 cryptocurrencies)
for tr in trs[:10]:
    # Extract the name and price from each <tr>
    name, price = tr.contents[2:4]

    # Extract the text content of the <p> tag inside the name element
    fixed_name = name.p.string

    # Extract the text content of the <a> tag inside the price element
    fixed_price = price.a.string

    # Print the fixed name and price of each cryptocurrency
    print(fixed_name)
    print(fixed_price)
    print()

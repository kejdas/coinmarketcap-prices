The script uses the requests library to make an HTTP GET request to the CoinMarketCap website and retrieves the HTML content.

BeautifulSoup is employed to parse the HTML content and create a document object (doc).

The script accesses the <tbody> element containing the cryptocurrency information on the page.

It extracts the list of <tr> (table rows) elements within the <tbody>.

The script then iterates over the first 10 <tr> elements, representing the top 10 cryptocurrencies.

For each <tr>, it extracts the name and price elements and further extracts the text content of specific child elements (<p> for name and <a> for price).

The cleaned and formatted cryptocurrency name and price are printed for each of the top 10 cryptocurrencies.

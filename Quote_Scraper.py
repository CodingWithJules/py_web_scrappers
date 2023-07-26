import requests
import bs4

# Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from
# the homepage.
res = requests.get("http://quotes.toscrape.com/")
print(res.text)

# Get the names of all the authors on the first page.
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup.select(".author"))

authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)

# Create a list of all the quotes on the first page.
quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)
print(quotes)

# Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top
# right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath
# each quote, try to find a class only present in the top right tags, perhaps check the span.

soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup.select('.tag-item'))

for item in soup.select(".tag-item"):
    print(item.text)

# Loop through all the pages and get all the unique authors on the website

url = 'http://quotes.toscrape.com/page/'

# Choose some huge page number we know doesn't exist
page_url = url+str(9999999)

# Obtain Request
res = requests.get(page_url)

# Turn into Soup
soup = bs4.BeautifulSoup(res.text, 'lxml')

print(soup)

# This solution requires that the string "No quotes found!" only occurs on the last page.
# If for some reason this string was on the other pages, we would need to be more detailed.
# "No quotes found!" in res.text

page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url + str(page)

    # Obtain Request
    res = requests.get(page_url)

    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break

    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

    # Go to Next Page
    page += 1

print(authors)




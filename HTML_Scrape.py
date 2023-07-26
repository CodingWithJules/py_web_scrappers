import bs4
import requests

# GOOD PRACTICE ----> IDENTIFIER
headers = {'User Agent': 'GOOGLE --> MY USER AGENT'}

url = 'https://finance.yahoo.com/news/'

r = requests.get(url)

# CHECK WEBPAGE ---> print(r.status_code) ---> 200 ERROR CODE ---> 404 NO GOOD

soup = bs4.BeautifulSoup(r.text, 'html.parser')

news = soup.find('title')
# news = soup.find('HTML SELECTOR', {'class': 'CLASS DESCRIPTION'}

print(news)

# ENSURE THE DATA BEING SCRAPED IS HTML
# CHECK BY COPY AND PASTING DATA INTO THE SOURCE

import bs4
import requests

url = "https://coinmarketcap.com/currencies/"

def fetchIcon(name):
    link = url+name
    pageData = requests.get(link)
    cleanPageData = bs4.BeautifulSoup(pageData.text, 'html.parser')
    icon = cleanPageData.find(height="32", width="32")
    iconUrl = icon.get("src")
    return iconUrl
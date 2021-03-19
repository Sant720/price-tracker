import requests
from bs4 import BeautifulSoup

def main():
    URL = get_valid_url()
    if URL:
        title, price = get_data(URL)
        print(title)
        print(price)

def get_data(URL):
    # Headers are used to pass as real user and prevent blocks from website
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 
        "Accept-Encoding":"gzip, deflate", 
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
        "DNT":"1",
        "Connection":"close", 
        "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    title, price = title.strip(), float(price.strip()[1:])
    return title, price

def get_valid_url():
    URL = input("URL: ")
    valid_urls = {
        "https://marinimport.com.pe/producto/",
        "https://www.amazon.com/"
    }
    if any([URL.startswith(x) for x in valid_urls]):
        return URL
    print("Not a valid URL. Please check the URL!")
    return ""

if __name__ == "__main__":
    main()
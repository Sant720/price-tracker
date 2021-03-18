import requests
from bs4 import BeautifulSoup

def main():
    title, price = get_data()
    print(title)
    print(price)

def get_data():
    # Will collect URl from user input in the future. This is a test URl
    URL = "https://marinimport.com.pe/producto/microfonos-condensadores-se-electronics-dm1-mic-pre/"

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

    title = soup.find("h2", {"class": "product_title entry-title"}).get_text()
    price = soup.find("ins").find("span", {"class": "woocommerce-Price-amount amount"}).get_text()
    title, price = title.strip(), to_float(price)
    return title, price

def to_float(string):
    result = ""
    for char in string:
        if char.isdigit():
            result += char
    return "{:.2f}".format(float(result) / 100)

if __name__ == "__main__":
    main()
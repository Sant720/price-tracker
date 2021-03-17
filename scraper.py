import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/AKG-Pro-Audio-K92-Closed-Back/dp/B01AIO8XVA/?_encoding=UTF8&pd_rd_w=whu2F&pf_rd_p=49ff6d7e-521c-4ccb-9f0a-35346bfc72eb&pf_rd_r=GE1E8E3KRHC43N354ZY6&pd_rd_r=509d7a96-e005-4c1c-86a0-2862d3a7d031&pd_rd_wg=NLSwX&ref_=pd_gw_ci_mcx_mr_hp_d"

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

print(title.strip())
print(price.strip())
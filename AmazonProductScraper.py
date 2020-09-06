from bs4 import BeautifulSoup
import http.cookiejar
from urllib.request import Request, urlopen
import re

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
outFile = open("Products.txt","w+")
reg_url = "https://www.amazon.it/s?k=smartwatch+tondo"
html = BeautifulSoup(urlopen(Request(url=reg_url, headers=headers)).read(), features='lxml')

elements = html.find_all("div", attrs={"data-cel-widget": lambda x: x is not None and 'search_result_' in x})
print(elements)
exit()
for el in elements:
    if "€" in str(el):
        if el.text.split("€")[0].strip() != el.text.split("€")[1]:
                print(el.text.split("€")[0])
                outFile.write(str(el) + "\n\n")
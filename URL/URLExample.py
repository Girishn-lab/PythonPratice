import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen('https://money.rediff.com/companies/State-Bank-Of-India/14030001') as f:
    soup = BeautifulSoup(f, 'html.parser')
    for tags in soup.find_all(id="ltpid"):
        print(tags.get_text())

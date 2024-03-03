import requests
from lxml import html

response = requests.get("https://rhino/vorwand#/id=81260487")

tree = html.fromstring(response.text)

locator = '//*[contains(text(),"Описание")]//..//td/text()'
passwords = tree.xpath(locator)

for password in passwords:
    password = str(password).strip()
    print(password)
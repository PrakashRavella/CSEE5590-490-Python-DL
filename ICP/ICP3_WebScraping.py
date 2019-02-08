from bs4 import BeautifulSoup
import requests

page_response = requests.get('https://en.wikipedia.org/wiki/Deep_learning')

page_content = BeautifulSoup(page_response.text, "html.parser")

print("Title of the webpage is :",page_content.title.string)

for a in page_content.find_all('a'):
    print(a.get('href'))
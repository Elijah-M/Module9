import requests
import bs4 as bs

url = 'https://realpython.com/python-modules-packages/'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()

soup = bs.BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())
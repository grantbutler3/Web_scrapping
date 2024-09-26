from bs4 import BeautifulSoup
import requests

# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]

print(tags.find_all("b"))

# HTML From Website
url = "https://www.nike.com/t/sportswear-tech-fleece-windrunner-mens-full-zip-hoodie-2QLsNw/FB7921-361"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
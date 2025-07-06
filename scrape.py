import requests
from bs4 import BeautifulSoup

URL = "https://easyfitness.club/studio/easyfitness-bornheim/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
meterbubble = soup.find_all("span", class_="meterbubble")
firstBubble = meterbubble[0] # for some reason there are TWO bubble Objects?
print("Das Studio hat " + firstBubble.text + " Auslastung momentan")


import requests
from bs4 import BeautifulSoup
# obtain list of all brands, change URL to scrape and add??
# for each category, filter by north america
URL = "https://directory.goodonyou.eco/brand/zara"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'lxml')


text = soup.body.get_text(' ', strip = True)

rstart = text.find("Rated: ")
rend = text.find(" price") 
overall = text[rstart:rend]


ptstart = text.find("Planet ")
ptend = text.find(" out of 5")
planet = text[ptstart : ptend]
pplstart = text.find("People ")
pplend = text.find(" out of 5 Animals")
ppl = text[pplstart : pplend]
anistart = text.find("Animals ")
aniend = text.find(" Overall")
aniend2 = text.find(" out of 5 Overall")
if (aniend2 != -1):
    aniend = aniend2
animals = text[anistart : aniend]

info = [overall, planet, ppl, animals]
# turn into raw numbers??

print(info)


#python list w/ [overall rating, planet, people, animals]
#-1 = not applicable

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent().random

print("Type \"en\" if you want to translate from French into English"
      ", or \"fr\" if you want to translate from English into French:")
language = input()
lang = ""
if language == "en":
    lang = "french-english"
else:
    lang = "english-french"
print("Type the word you want to translate:")
word = input()
print("You chose " + language + " as the language to translate " + word + " to.")

url = "https://context.reverso.net/translation/" + lang + "/" + word
headers = {'User-Agent': ua}
page = requests.get(url, headers=headers)
pageSoup = BeautifulSoup(page.content, "html.parser")
if page:
    print("200 OK")

print("Translations")

unformatted_list = pageSoup.find_all("span", class_="display-term")
for i in range(len(unformatted_list)):
    unformatted_list[i] = unformatted_list[i].text
print(unformatted_list)

unformatted_list_stc = pageSoup.find_all("div", {'class': ['src ltr', 'trg ltr']})
for i in range(len(unformatted_list_stc)):
    unformatted_list_stc[i] = unformatted_list_stc[i].text.strip()
print(unformatted_list_stc)






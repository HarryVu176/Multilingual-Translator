import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent().random
language_tuple = ('Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
                  'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish')

print("Hello, welcome to the translator. Translator supports:")
for i in range(len(language_tuple)):
    print(f"{i + 1}. {language_tuple[i]}")
print("Type the number of your language:")
lang1 = language_tuple[int(input()) - 1].lower()
print("Type the number of language you want to translate to:")
lang2 = language_tuple[int(input()) - 1].lower()
print("Type the word you want to translate:")
word = input()

url = "https://context.reverso.net/translation/" + lang1 + "-" + lang2 + "/" + word
print(url)
headers = {'User-Agent': ua}
page = requests.get(url, headers=headers)
pageSoup = BeautifulSoup(page.content, "html.parser")

unformatted_list = pageSoup.find_all("span", class_="display-term")
for i in range(len(unformatted_list)):
    unformatted_list[i] = unformatted_list[i].text

unformatted_list_stc = pageSoup.find_all("div", {'class': ['src ltr', 'trg ltr']})
for i in range(len(unformatted_list_stc)):
    unformatted_list_stc[i] = unformatted_list_stc[i].text.strip()

print()
print(f"{lang2.title()} Translations:")
for words in unformatted_list:
    print(words)

print()
print(f"{lang2.title()} Examples:")
i = 0
for stc in unformatted_list_stc:
    i = i + 1
    print(stc)
    if i == 2:
        print("")
        i = 0









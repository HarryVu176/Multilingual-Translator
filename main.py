import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Random User Agent to prevent website from blocking the request
ua = UserAgent().random

# Languages supported by the program
language_tuple = ('Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
                  'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish')

print("Hello, welcome to the translator. Translator supports:")
# Print the languages supported by the program
for i in range(len(language_tuple)):
    print(f"{i + 1}. {language_tuple[i]}")
# Get the origin language and the destination language, both to lowercase
print("Type the number of your language:")
lang1 = language_tuple[int(input()) - 1].lower()
print("Type the number of language you want to translate to:")
lang2 = language_tuple[int(input()) - 1].lower()
print("Type the word you want to translate:")
word = input()

# URL example: https://context.reverso.net/translation/german-english/haus
url = "https://context.reverso.net/translation/" + lang1 + "-" + lang2 + "/" + word
# Parse the URL
headers = {'User-Agent': ua}
page = requests.get(url, headers=headers)
pageSoup = BeautifulSoup(page.content, "html.parser")

# Get the translations WORDs from the website
# Example: <span class="display-term">house</span>
unformatted_list = pageSoup.find_all("span", class_="display-term")
for i in range(len(unformatted_list)):
    unformatted_list[i] = unformatted_list[i].text

# Get the translations SENTENCEs from the website
# class_="src ltr" is the origin language sentence and class_="trg ltr" is the destination language sentence
unformatted_list_stc = pageSoup.find_all("div", {'class': ['src ltr', 'trg ltr']})
for i in range(len(unformatted_list_stc)):
    unformatted_list_stc[i] = unformatted_list_stc[i].text.strip()

# Print the translations WORDs
print()
print(f"{lang2.title()} Translations:")
for words in unformatted_list:
    print(words)

# Print the translations SENTENCEs
print()
print(f"{lang2.title()} Examples:")
i = 0
for stc in unformatted_list_stc:
    i = i + 1
    print(stc)
    if i == 2:
        print("")
        i = 0









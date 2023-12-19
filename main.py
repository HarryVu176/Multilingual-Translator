import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Random User Agent to prevent website from blocking the request
ua = UserAgent().random

#Hello Harry

# Languages supported by the program
language_tuple = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
                  'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']

print("Hello, welcome to the translator. Translator supports:")
# Print the languages supported by the program
for i in range(len(language_tuple)):
    print(f"{i + 1}. {language_tuple[i]}")
# Get the origin language and the destination language, both to lowercase
print("Type the number of your language:")
lang1 = language_tuple[int(input()) - 1].lower()
print("Type the number of a language you want to translate to or '0' to translate to all languages:")
il2 = int(input())
lang2 = language_tuple[il2 - 1].lower() if il2 != 0 else "all"
print("Type the word you want to translate:")
word = input()
file_name = word + ".txt"
file = open(file_name, "w", encoding="utf-8")

i = 0
if lang2 == "all":
    language_tuple.remove(lang1.title())
    for i in range(len(language_tuple)):
        lang2 = language_tuple[i].lower()
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

        # Get the translated word and format it to be printed/written
        # Example: English Translations:
        #          house
        translated_word = f"{lang2.title()} Translations:\n{unformatted_list[0]}\n\n"

        # Get the translated sentence and format it to be printed/written
        # Example: English Examples:
        #          I live in a house.
        translated_stc = f"{lang2.title()} Examples:\n{unformatted_list_stc[0]}:\n{unformatted_list_stc[1]}\n\n"

        file.write(translated_word)
        file.write(translated_stc)
else:
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

    # Get the translated word and format it to be printed/written
    # Example: English Translations:
    #          house
    translated_word = f"{lang2.title()} Translations:\n{unformatted_list[0]}\n\n"

    # Get the translated sentence and format it to be printed/written
    # Example: English Examples:
    #          I live in a house.
    translated_stc = f"{lang2.title()} Examples:\n{unformatted_list_stc[0]}:\n{unformatted_list_stc[1]}\n\n"

    file.write(translated_word)
    file.write(translated_stc)

# Print whole file
file = open(file_name, "r", encoding="utf-8")
print(file.read())
file.close()







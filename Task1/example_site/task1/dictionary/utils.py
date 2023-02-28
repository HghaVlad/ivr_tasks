from django.conf import settings


def get_words():
    file = open(settings.FILE_PATH, "r", encoding="utf-8").read().splitlines()
    original_language = []
    translations = []
    for line in file:
        word1, word2 = line.split("-")
        original_language.append(word1)
        translations.append(word2)
    return original_language, translations


def add_words(word1, word2):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


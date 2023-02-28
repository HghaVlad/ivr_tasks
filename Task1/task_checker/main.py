import requests
from bs4 import BeautifulSoup

link = "http://127.0.0.1:8000/"
work = True


def main_page():
    global work
    try:
        site = requests.get(link)
        page = BeautifulSoup(site.text, "lxml")
        if "My dictionary" not in page.find("title").string:
            work = False
            return
    except Exception as e:
        print(e)
        work = False
        return
    try:
        site = requests.get(link + "home")
        page = BeautifulSoup(site.text, "lxml")
        if "My dictionary" not in page.find("title").string:
            work = False
            return
    except Exception as e:
        print(e)
        work = False
        return
    print("fine")


def word_list_page():
    global work
    try:
        page = BeautifulSoup(requests.get(link + "words_list").text, "lxml")
        tds = page.find("table", "words_list").find_all("td")
        add_new_word("orange", "апельсин")  # Add some words
        page2 = BeautifulSoup(requests.get(link + "words_list").text, "lxml")
        tds2 = page2.find("table", "words_list").find_all("td")  # Get updates
        if len(tds) == len(tds2):
            work = False
            return
        a = "orange"  # Check having this word
        for td in tds2:
            if td.string == "orange":
                a = "апельсин"
            elif td.string == a:
                break
        else:
            print("orange ")
            work = False
            return
        add_new_word("man", "бежать")  # Add some words again
        page3 = BeautifulSoup(requests.get(link + "words_list").text, "lxml")
        table3 = page3.find("table", "words_list")
        tds3 = table3.find_all("td")
        if len(tds2) == len(tds3):
            work = False
            return
        a = "man"
        for td in tds3:
            if td.string == "man":
                a = "бежать"
            elif td.string == a:
                break
        else:
            work = False
            return
    except Exception as e:
        print(e)
        work = False
        return


def add_word_page():
    global work
    try:
        site = requests.get(link + "add_word")
        page = BeautifulSoup(site.text, "lxml")
        form = page.find("form")
        inputs = form.find_all("input")
        if len(inputs) < 2:
            work = False
            return
        if form.get("method") == "post" or form.get("method") == "POST":
            pass
        else:
            work = False
            return
    except Exception as e:
        print(e)
        work = False
        return


def add_new_word(word1, word2):
    client = requests.session()
    client.get(link + "add_word")
    csrftoken = client.cookies['csrftoken']
    info = client.post(link + "add_word", data={"word1": word1, "word2": word2, "csrfmiddlewaretoken":csrftoken}, headers={"Referer": link + "add_word"})
    print(info)


print(work)
main_page()
print("Step 1:", work)
add_word_page()
print("Step 2:", work)
word_list_page()
print("Step 3:", work)

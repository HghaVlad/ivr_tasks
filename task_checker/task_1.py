import requests
from bs4 import BeautifulSoup

example_link = "http://127.0.0.1:8000/"


def main_page(link):
    try:
        site = requests.get(link)
        page = BeautifulSoup(site.text, "lxml")
        if "My dictionary" not in page.find("title").string:
            return False
    except Exception as e:
        print(e)
        return False
    try:
        site = requests.get(link + "home")
        page = BeautifulSoup(site.text, "lxml")
        if "My dictionary" not in page.find("title").string:
            return False
    except Exception as e:
        print(e)
        
        return False
    return True


def word_list_page(link):
    try:
        page = BeautifulSoup(requests.get(link + "words_list").text, "lxml")
        tds = page.find("table", "words_list").find_all("td")
        add_new_word("orange", "апельсин", link)  # Add some words
        page2 = BeautifulSoup(requests.get(link + "words_list").text, "lxml")
        tds2 = page2.find("table", "words_list").find_all("td")  # Get updates
        if len(tds) == len(tds2):
            return False
        a = "orange"  # Check having this word
        for td in tds2:
            if td.string == "orange":
                a = "апельсин"
            elif td.string == a:
                break
        else:
            print("orange ")
            return False
        add_new_word("man", "бежать", link)  # Add some words again
        page3 = BeautifulSoup(requests.get(link + "words_list").text, "lxml")
        table3 = page3.find("table", "words_list")
        tds3 = table3.find_all("td")
        if len(tds2) == len(tds3):
            return False
        a = "man"
        for td in tds3:
            if td.string == "man":
                a = "бежать"
            elif td.string == a:
                break
        else:
            return False
    except Exception as e:
        print(e)
        return False
    return True


def add_word_page(link):
    try:
        site = requests.get(link + "add_word")
        page = BeautifulSoup(site.text, "lxml")
        form = page.find("form")
        inputs = form.find_all("input")
        if len(inputs) < 2:
            return False
        if form.get("method") == "post" or form.get("method") == "POST":
            pass
        else:
            return False
    except Exception as e:
        print(e)
        return False
    return True


def add_new_word(word1, word2, link):
    client = requests.session()
    client.get(link + "add_word")
    csrftoken = client.cookies['csrftoken']
    info = client.post(link + "add_word", data={"word1": word1, "word2": word2, "csrfmiddlewaretoken":csrftoken}, headers={"Referer": link + "add_word"})
    print(info)


def get_result(link):
    return [main_page(link), add_word_page(link), word_list_page(link)]


if __name__ == "__main__":
    print(main_page(example_link))
    print(add_word_page(example_link))
    print(word_list_page(example_link))

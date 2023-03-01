from django.shortcuts import render, redirect
from .utils import add_words, get_words
# Create your views here.


def home_page(request):
    return render(request, "home_page.html")


def words_list(request):
    list1, list2 = get_words()
    return render(request, "show_words.html", {"words": zip(list1, list2)})


def add_word(request):
    if request.method == "GET":
        return render(request, "add_word.html")
    else:
        word1, word2 = request.POST["word1"], request.POST["word2"]
        add_words(word1, word2)
        return redirect("/")

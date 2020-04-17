from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache



# Create your views here.
import requests
import json


def index(request):
    return render(request, "index.html")


def scrape(request):
    cache.clear()
    request.session.set_expiry(100)

    if request.method == "GET":
        return redirect("/users/index/")

    if request.method == "POST":

        keyword = request.POST.get("keyword")
        # keyword = request.POST["keyword"]
        crypto = requests.get(
            "https://min-api.cryptocompare.com/data/v2/news/?" + keyword
        )

        crypto = json.loads(crypto.content)

        if not keyword:
            notfound = "Enter a crypto currency symbol into the form above..."
            return render(request, "scrape_result.html", {"notfound": notfound})

        return render(
            request, "scrape_result.html", {"keyword": keyword, "crypto": crypto}
        )

    else:
        return render(request, "index.html")

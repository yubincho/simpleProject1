
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def scrape(request):

    if request.method == "POST":
        import requests
        import json

        keyword = request.POST["keyword"]
        keyword = keyword.upper()

        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/v2/news/?" + keyword)

        crypto = json.loads(crypto_request.content)

        return render(request, "scrape_result.html", {"keyword": keyword, "crypto": crypto})

    else:
        notfound = "Enter a crypto currency symbol into the form above..."
        return render(request, "index.html", {"notfound": notfound})


    

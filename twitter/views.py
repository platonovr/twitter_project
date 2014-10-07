from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "twitter/index.html",
                  {"user": "Huilo", "tweets": []
                  }
    )


def process(request):
    tweet = request.POST["tweet"]
    print tweet
    return HttpResponseRedirect("/")

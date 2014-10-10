from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.core.urlresolvers import reverse
from twitter.models import RawTweet


def index(request):
    return render(request, "twitter/index.html",
                  {"user": "Huilo", "tweets": RawTweet.objects.all().order_by("-p_date")}
    )


def process(request):
    tweet = request.POST["tweet"]
    t = RawTweet(text=tweet, p_date=datetime.now())
    t.save()
    return HttpResponseRedirect(reverse('index'))  # args=(book.id,)

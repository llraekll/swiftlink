import random
import string
from django.shortcuts import redirect, render
from .forms import Url
from .models import Urls

def home(request):
    form = Url()
    if request.method == "POST":
        form = Url(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            if ("http://" not in url) and ("https://" not in url) :
                url = "https://" + url 
            N=5
            mini_url = res = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase+ 
                             string.digits, k=N))
            new_url = Urls(url=url, mini_url=mini_url)
            new_url.save()
            context = {
                "mini_url": mini_url
            }
            return  render(request, 'final.html', context)
    context  = {
        "form": form
    }
    return render(request, 'index.html', context)

def reroute(request, pk):
    url_details = Urls.objects.get(mini_url=pk)
    return redirect(url_details.url)





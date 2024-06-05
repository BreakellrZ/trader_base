from django.shortcuts import render
from django.views import generic


# Create your views here.
def home(request):

    return render(
        request,
        "index.html",
        {"home": home},
    )
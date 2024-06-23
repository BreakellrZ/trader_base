from django.shortcuts import render
from django.views import generic
from .models import Journal


# Create your views here.
class PostList(generic.ListView):
    queryset = Journal.objects.all().order_by("-date")
    template_name = "post.html"
    paginate_by = 3

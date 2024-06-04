from django.shortcuts import render
from django.views import generic
from .models import Journal


# Create your views here.
class PostList(generic.ListView):
    queryset = Journal.objects.all().order_by("-created_on").filter(status=1)
    template_name = "post.html"

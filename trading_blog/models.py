from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="trading_blog_posts"
    )
    content = models.TextField()
    date = models.DateField(auto_now=True, auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    #Image model when I get to cloudinary

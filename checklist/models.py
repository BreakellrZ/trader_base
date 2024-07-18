from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Checkbox(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='todo_items')
    

    def __str__(self):
        return self.title
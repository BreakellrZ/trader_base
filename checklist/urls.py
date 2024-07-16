from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.list , name='checklist'),
]

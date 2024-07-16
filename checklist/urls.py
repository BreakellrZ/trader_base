from . import views
from django.urls import path

urlpatterns = [
    path('checklist/', views.checklist, name='checklist'),
]

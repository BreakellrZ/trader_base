from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.list , name='checklist'),
    path('update_list/<str:pk>/', views.updateList, name="update_list"),
    path('delete_list/<str:pk>/', views.deleteList, name="delete_list")
]

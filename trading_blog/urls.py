from . import views
from django.urls import path


urlpatterns = [
    path('tradingblog/', views.PostList.as_view(), name ='trading_blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
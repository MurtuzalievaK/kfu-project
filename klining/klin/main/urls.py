from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('contacts', views.contacts, name='contacts'),
    path('users/', include('users.urls', namespace="users")),
    path('send-order/', views.send_order, name='send_order'),
    path('orderForm/', views.send_order, name='orderForm'),
    path('news/<int:news_id>/', views.get_news_description, name='get_news_description'),
]

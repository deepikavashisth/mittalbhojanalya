from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('about/', views.about, name='about'),
    path('review/', views.review, name='review'),
    path('ajax/subscribe/', views.ajax_subscribe, name='ajax_subscribe'),
]


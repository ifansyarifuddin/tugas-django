from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.member, name='member'),
   path('contact/', views.contact, name='contact'),
    path('picture/', views.picture, name='picture'),
   
]
from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('blog/',views.blog),
    path('cart/',views.cart),
    path('checkout/',views.checkout),
    path('contact/',views.contact),
    path('services/',views.services),
    path('shop/',views.shop),
    path('thankyou/',views.thankyou),
]

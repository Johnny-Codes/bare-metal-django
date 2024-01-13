from django.urls import path

from .views import blinky

urlpatterns = [
    path("blinky/", blinky),
]

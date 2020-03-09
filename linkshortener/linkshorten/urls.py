from django.urls import path

from . import views

urlpatterns = [
    path('shorten/', views.ShortenLink.as_view(), name='shorten_link')
]

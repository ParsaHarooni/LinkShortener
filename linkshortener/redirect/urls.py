from django.urls import path

from redirect.views import Redirect

urlpatterns = [
    path('<url_hash>/', Redirect.as_view(), name="redirect")
]

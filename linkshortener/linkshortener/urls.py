from django.urls import path, include
from authentication import urls as authentication_urls

api_urlpatterns = [
    path('auth/', include(authentication_urls))
]

urlpatterns = [
    path('api/', include(api_urlpatterns)),
]
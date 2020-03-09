from django.urls import path, include
from authentication import urls as authentication_urls
from linkshorten import urls as shorten_urls

api_urlpatterns = [
    path('auth/', include(authentication_urls)),
    path('shorten/', include(shorten_urls))
]

urlpatterns = [
    path('api/', include(api_urlpatterns)),
]

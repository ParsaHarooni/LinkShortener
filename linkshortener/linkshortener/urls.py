from django.urls import path, include
from authentication import urls as authentication_urls
from linkshorten import urls as shorten_urls
from redirect import urls as redirect_urls
from analytics import urls as analytics_urls

api_urlpatterns = [
    path('auth/', include(authentication_urls), name='auth'),
    path('shorten/', include(shorten_urls), name='shorten'),
    path('analytics/', include(analytics_urls), name='analytics')

]

urlpatterns = [
    path('api/', include(api_urlpatterns), name='api'),
    path('r/', include(redirect_urls))
]

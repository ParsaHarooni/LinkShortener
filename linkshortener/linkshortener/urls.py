from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from authentication import urls as authentication_urls
from linkshorten import urls as shorten_urls
from redirect import urls as redirect_urls
from analytics import urls as analytics_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = [
    path('auth/', include(authentication_urls), name='auth'),
    path('shorten/', include(shorten_urls), name='shorten'),
    path('analytics/', include(analytics_urls), name='analytics')

]

urlpatterns = [
    path('api/', include(api_urlpatterns), name='api'),
    path('r/', include(redirect_urls)),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

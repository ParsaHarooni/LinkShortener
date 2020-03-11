from django.urls import path

from analytics.views import GetAllVisits

urlpatterns = [
    path('all/', GetAllVisits.as_view(), name='get_all')
]

from unicodedata import name
from django.urls import path

from listings.api.views import ListingApiView

urlpatterns = [
    path('listing/', ListingApiView.as_view(), name="listing"),
]

from unicodedata import name
from django.urls import path

from listings.api.views import ListingApiView, BookingInfoApiView

urlpatterns = [
    path('listing/', ListingApiView.as_view(), name="listing"),
    path('bookingInfos/', BookingInfoApiView.as_view(), name="bookingInfos"),
]

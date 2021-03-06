from unicodedata import name
from django.urls import path

from listings.api.views import (
    ListingApiView, 
    BookingInfoApiView, 
    AvailableListingsApiView, 
    AllHotelRoomsApiView
)

urlpatterns = [
    path('listings/', ListingApiView.as_view(), name="listings"),
    path('bookingInfos/', BookingInfoApiView.as_view(), name="bookingInfos"),
    path('allRooms/', AllHotelRoomsApiView.as_view(), name="allRooms"),
    path(
        'available_listings/',
        AvailableListingsApiView.as_view(),
        name="available_listings"
    ),
]

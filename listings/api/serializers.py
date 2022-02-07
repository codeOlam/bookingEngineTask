from rest_framework import serializers

from listings.models import HotelRoom, HotelRoomType, Listing, BookingInfo


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_type', 'title', 'country', 'city']


class BookingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingInfo
        fields = '__all__'

class HotelRoomTypeSerializer(serializers.ModelSerializer):
    hotel = ListingSerializer(required=True)
    class Meta:
        model = HotelRoomType
        fields = ['hotel']


class AvailableListingsSerializer(serializers.ModelSerializer):
    hotel_room_type = HotelRoomTypeSerializer(required=True)

    class Meta:
        model = HotelRoom
        fields = ['hotel_room_type', 'price']

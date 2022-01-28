from rest_framework import serializers

from listings.models import Listing, BookingInfo, Reservation


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_type', 'title', 'country', 'city']


class BookingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingInfo
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class AvailableListingsSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(required=True)
    # booking_info = ReservationSerializer()
    # print('booking_info: ', booking_info.data)
    # booking_info = BookingInfoSerializer(required=True)

    class Meta:
        # model = Reservation
        model = BookingInfo
        fields = ['id', 'listing', 'price']
        # fields = ['booking_info', 'listing', 'check_in', 'check_out']

from rest_framework import serializers

from listings.models import Listing, BookingInfo


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_type', 'title', 'country', 'city']


class BookingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingInfo
        fields = '__all__'


class AvailableListingsSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(required=True)

    class Meta:
        model = BookingInfo
        fields = ['id', 'listing', 'price']

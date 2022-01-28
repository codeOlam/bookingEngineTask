from rest_framework import status, views, generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from listings.models import Listing, BookingInfo

from .serializers import ListingSerializer, BookingInfoSerializer, AvailableListingsSerializer


class ListingApiView(views.APIView):
    serializer_class = ListingSerializer

    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)

        data = serializer.data

        response_payload = {
            'status': {
                'message': 'success',
                'code': f"{status.HTTP_200_OK} OK"
            },
            'listings': data,
            'response_code': status.HTTP_200_OK,
        }

        return Response(response_payload, status=status.HTTP_200_OK)


class BookingInfoApiView(views.APIView):
    serializer_class = ListingSerializer

    def get(self, request):
        bookingInfo = BookingInfo.objects.all().order_by('price')
        serializer = BookingInfoSerializer(bookingInfo, many=True)

        data = serializer.data

        response_payload = {
            'status': {
                'message': 'success',
                'code': f"{status.HTTP_200_OK} OK"
            },
            'bookingInfos': data,
            'response_code': status.HTTP_200_OK,
        }

        return Response(response_payload, status=status.HTTP_200_OK)


class BookingInfoFilter(filters.FilterSet):
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    check_in = filters.DateFilter(
        field_name="check_in", exclude=True, lookup_expr='gte')
    check_out = filters.DateFilter(
        field_name="check_out", exclude=True, lookup_expr='lte')

    class Meta:
        model = BookingInfo
        fields = ['check_in', 'check_out', 'max_price']


class AvailableListingsApiView(generics.ListAPIView):
    serializer_class = AvailableListingsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookingInfoFilter
    queryset = BookingInfo.objects.all().order_by('price')

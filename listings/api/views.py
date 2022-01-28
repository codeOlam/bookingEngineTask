from rest_framework import status, views
from rest_framework.response import Response

from listings.models import Listing, BookingInfo

from .serializers import ListingSerializer, BookingInfoSerializer


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

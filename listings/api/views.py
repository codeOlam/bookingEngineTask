from rest_framework import status, views
from rest_framework.response import Response

from listings.models import Listing

from .serializers import ListingSerializer

class ListingApiView(views.APIView):
  serializer_class = ListingSerializer

  def get(self, request):
    print ('request: ', request)
    listings = Listing.objects.all()
    serializer = ListingSerializer(listings, many=True)
    print('\nserializer: ', serializer)

    data = serializer.data
    print ('\ndata: ', data)

    response_payload= {
      'status': {
          'message': 'success',
          'code': f"{status.HTTP_200_OK} OK"
      },
      'listings': data,
      'response_code': status.HTTP_200_OK,
    }

    return Response(response_payload, status=status.HTTP_200_OK)



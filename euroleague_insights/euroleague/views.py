from rest_framework.views import APIView
from rest_framework.views import Response

from euroleague_insights.euroleague.serializers import ClubSerializer
from euroleague_insights.euroleague.services import list_clubs


class ListClubsView(APIView):
    """
    API view to list all clubs.
    """

    def get(self, request):
        clubs = list_clubs()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

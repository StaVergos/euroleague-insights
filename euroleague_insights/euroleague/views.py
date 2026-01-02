from rest_framework.views import APIView
from rest_framework.views import Response

from euroleague_insights.euroleague.serializers import ClubSerializer
from euroleague_insights.euroleague.serializers import PlayerSerializer
from euroleague_insights.euroleague.services import list_club_players
from euroleague_insights.euroleague.services import list_clubs
from euroleague_insights.euroleague.services import list_players


class ListClubsView(APIView):
    """
    API view to list all clubs.
    """

    def get(self, request):
        clubs = list_clubs()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)


class ListPlayersView(APIView):
    """
    API view to list all players.
    """

    def get(self, request):
        players = list_players()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


class ListClubPlayersView(APIView):
    """
    API view to list selected club players.
    """

    def get(self, request, code):
        players = list_club_players(code)
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.views import Response

from euroleague_insights.euroleague.serializers import ClubSerializer
from euroleague_insights.euroleague.serializers import MatchSerializer
from euroleague_insights.euroleague.serializers import PlayerSerializer
from euroleague_insights.euroleague.services import list_club_matches
from euroleague_insights.euroleague.services import list_club_players
from euroleague_insights.euroleague.services import list_clubs
from euroleague_insights.euroleague.services import list_matches
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

    def get(self, request, club_code):
        players = list_club_players(club_code)
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


class ListMatchesView(APIView):
    """
    API view to list all matches
    """

    def get(self, request):
        matches = list_matches()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)


class ListClubMatchesView(APIView):
    """
    API view to list selected club matches.
    """

    def get(self, request, club_code):
        matches = list_club_matches(club_code)
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

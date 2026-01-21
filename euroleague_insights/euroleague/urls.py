from django.urls import path

from euroleague_insights.euroleague.views import ListClubMatchesView
from euroleague_insights.euroleague.views import ListClubPlayersView
from euroleague_insights.euroleague.views import ListClubsView
from euroleague_insights.euroleague.views import ListMatchesView
from euroleague_insights.euroleague.views import ListMatchTopScorersView
from euroleague_insights.euroleague.views import ListPlayByPlayView
from euroleague_insights.euroleague.views import ListPlayersView

urlpatterns = [
    path("clubs/", ListClubsView.as_view(), name="list-clubs"),
    path("players/", ListPlayersView.as_view(), name="list-players"),
    path(
        "clubs/<str:club_code>/players/",
        ListClubPlayersView.as_view(),
        name="list-club-players",
    ),
    path("matches/", ListMatchesView.as_view(), name="list-matches"),
    path(
        "matches/<str:club_code>/",
        ListClubMatchesView.as_view(),
        name="list-club-matches",
    ),
    path(
        "playbyplay/<str:game_code>/",
        ListPlayByPlayView.as_view(),
        name="list-plays",
    ),
    path(
        "insights/top_match_scorers/<str:game_code>/",
        ListMatchTopScorersView.as_view(),
        name="list-match-top-scorers",
    ),
]

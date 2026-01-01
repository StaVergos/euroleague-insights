from django.urls import path

from euroleague_insights.euroleague.views import (
    ListPlayersView,
    ListClubPlayersView,
    ListClubsView,
)

urlpatterns = [
    path("clubs/", ListClubsView.as_view(), name="list-clubs"),
    path("players/", ListPlayersView.as_view(), name="list-players"),
    path(
        "clubs/<str:club_code>/players/",
        ListClubPlayersView.as_view(),
        name="list-club-players",
    ),
]

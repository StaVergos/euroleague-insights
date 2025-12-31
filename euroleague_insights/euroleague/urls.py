from django.urls import path

from euroleague_insights.euroleague.views import ListClubPlayersView, ListClubsView
from euroleague_insights.euroleague.views import ListPlayersView

urlpatterns = [
    path("clubs/", ListClubsView.as_view(), name="list-clubs"),
    path("players/", ListPlayersView.as_view(), name="list-players"),
    path(
        "clubs/<str:code>/players/",
        ListClubPlayersView.as_view(),
        name="list-club-players",
    ),
]

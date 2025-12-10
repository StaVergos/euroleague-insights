from django.urls import path

from euroleague_insights.euroleague.views import ListClubsView

urlpatterns = [
    path("clubs/", ListClubsView.as_view(), name="list-clubs"),
]

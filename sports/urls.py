from django.urls import path

from . import views


app_name = "sports"

urlpatterns = [
    path("", views.index, name='index'),
    path("<league_name>/", views.league, name='league'),
    path("<league_name>/<team_name>/", views.team, name='team'),
    path("<league_name>/<team_name>/<season_year>/", views.season, name='season')
]

from django.shortcuts import render
from .models import League, Team, Season
import sys
import os
from pathlib import Path
from send2trash import send2trash
from .programs import NhlStats
# Create your views here.


def error_500(request):
    leagues = League.objects.all()
    return render(request, "404_500.html", context={'leagues': leagues})


def error_404(request, exception):
    leagues = League.objects.all()
    return render(request, "404_500.html", context={'leagues': leagues})


def index(request):
    leagues = League.objects.all()
    return render(request, "sports/index.html", context={"leagues": leagues})


def league(request, league_name):
    leagues = League.objects.all()
    league = League.objects.get(name=league_name.upper())
    teams = Team.objects.filter(league=league).order_by('name')
    return render(request, "sports/league.html", context={"league": league, "teams": teams, "leagues": leagues})


def team(request, league_name, team_name):
    leagues = League.objects.all()
    league = League.objects.get(name=league_name.upper())
    team = Team.objects.get(name=team_name.title())
    seasons = Season.objects.filter(team__name=team).order_by('-year')
    return render(request, "sports/team.html", context={
        "league": league, "team": team, "seasons": seasons,
        "leagues": leagues
    })


def season(request, league_name, team_name, season_year):
    def render_link(export_type):
        return render(request, "sports/season.html", context={
            "league": league, "team": team, "season": season, "leagues": leagues,
            "link": link, f"post_{export_type}": True
        })

    def empty_media():
        for file_folder in os.listdir(str(Path.cwd()/'media')):
            send2trash(str(Path.cwd()/'media'/file_folder))

    def export_nhl(export_type):
        nhl_obj = NhlStats(
            team.name, season.year, folder=str(Path.cwd()/"media"), titled_folder=False, export_type=export_type).download()
        return nhl_obj

    leagues = League.objects.all()
    league = League.objects.get(name=league_name.upper())
    team = Team.objects.get(name=team_name.title())
    season = Season.objects.get(year=season_year)

    if request.method == "GET":
        # empty_media()
        return render(request, "sports/season.html", context={
            "league": league, "team": team, "season": season, "leagues": leagues
        })
    elif request.method == "POST":
        if "xlsx_script" in request.POST:
            if league.name == "NHL":
                link = export_nhl("xlsx")
            return render_link("xlsx")

        elif "pdf_script" in request.POST:
            if league.name == "NHL":
                link = export_nhl("pdf")
            return render_link("pdf")

        elif "csv_script" in request.POST:
            if league.name == "NHL":
                link = export_nhl("csv")
            return render_link('csv')

        elif "json_script" in request.POST:
            if league.name == "NHL":
                link = export_nhl("json")
            return render_link("json")

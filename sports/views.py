from django.shortcuts import render
from .models import League, Team, Season
import sys
import os
from pathlib import Path
from send2trash import send2trash
from .programs import NhlStats
import time
# Create your views here.


def error_500(request):
    leagues = League.objects.all()
    return render(request, "404_500.html", context={'leagues': leagues})


def error_404(request, exception):
    leagues = League.objects.all()
    return render(request, "404_500.html", context={'leagues': leagues})


def index(request):
    # leagues = League.objects.all()
    leagues = League.objects.raw("SELECT id, name FROM sports_league")
    return render(request, "sports/index.html", context={"leagues": leagues})


def league(request, league_name):
    # leagues = League.objects.all()
    leagues = League.objects.raw("SELECT id, name FROM sports_league")
    # league = League.objects.get(name=league_name.upper())
    league = League.objects.raw(
        "SELECT * FROM sports_league WHERE name = %s", [league_name.upper()])[0]
    # teams = Team.objects.filter(league=league).order_by('name')
    teams = Team.objects.raw(
        "SELECT * FROM sports_team WHERE league_id = %s ORDER BY name", [league.id])
    # return render(request, "sports/league.html", context={"league": league, "teams": teams, "leagues": leagues})
    return render(request, "sports/league.html", context={"league": league, "teams": teams, "leagues": leagues})


def team(request, league_name, team_name):
    # leagues = League.objects.all()
    leagues = League.objects.raw("SELECT id, name FROM sports_league")
    # league = League.objects.get(name=league_name.upper())
    league = League.objects.raw(
        "SELECT * FROM sports_league WHERE name = %s", [league_name.upper()])[0]
    if team_name.lower() == 'philadelphia-76ers':
        team = Team.objects.raw(
            "Select * from sports_team WHERE name = 'Philadelphia-76ers'")[0]
    else:
        # team = Team.objects.get(name=team_name.title())
        team = Team.objects.raw(
            "SELECT * FROM sports_team WHERE name = %s", [team_name.title()])[0]
    # seasons = Season.objects.filter(team__name=team).order_by('-year')
    seasons = Season.objects.raw(
        "SELECT * FROM sports_season JOIN sports_season_team ON season_id = sports_season.id WHERE team_id = %s ORDER BY year DESC", [team.id])
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
            if file_folder.endswith('.txt'):
                continue
            for file in os.listdir(str(Path.cwd()/'media'/file_folder)):
                send2trash(str(Path.cwd()/'media'/file_folder/file))

    def export_nhl(export_type):
        print(os.listdir(str(Path.cwd()/"media")))
        # os.makedirs(Path(str(Path.cwd()/"media"))/team.name.title(), exist_ok=True)
        nhl_obj = NhlStats(
            team.name, season.year, folder=str(Path.cwd()/"media"), titled_folder=False, export_type=export_type).download()
        return nhl_obj

    # leagues = League.objects.all()
    leagues = League.objects.raw("SELECT id, name FROM sports_league")
    # league = League.objects.get(name=league_name.upper())
    league = League.objects.raw(
        "SELECT * FROM sports_league WHERE name = %s", [league_name.upper()])[0]
    # team = Team.objects.get(name=team_name.title())
    team = Team.objects.raw(
        "SELECT * FROM sports_team WHERE name = %s", [team_name.title()])[0]
    # season = Season.objects.get(year=season_year)
    season = Season.objects.raw(
        "SELECT * FROM sports_season WHERE year = %s", [season_year])[0]

    if request.method == "GET":
        empty_media()
        return render(request, "sports/season.html", context={
            "league": league, "team": team, "season": season, "leagues": leagues
        })
    elif request.method == "POST":
        if "xlsx_script" in request.POST:
            if league.name == "NHL":
                link = export_nhl("xlsx")
            print(os.listdir(str(Path.cwd()/"media")))
            print(os.listdir(str(Path.cwd()/"media"/"montreal-canadiens")))
            time.sleep(2)
            return render_link("xlsx")

        elif "pdf_script" in request.POST:
            if league.name == "NHL":
                link = export_nhl("pdf_html")
            print(os.listdir(str(Path.cwd()/"media")))
            print(os.listdir(str(Path.cwd()/"media"/"montreal-canadiens")))
            time.sleep(2)
            return render_link("pdf_html")

        elif "csv_script" in request.POST:
            if league.name == "NHL":
                link = export_nhl("csv")
            print(os.listdir(str(Path.cwd()/"media")))
            print(os.listdir(str(Path.cwd()/"media"/"montreal-canadiens")))
            time.sleep(2)
            return render_link('csv')

        elif "json_script" in request.POST:
            if league.name == "NHL":
                link = export_nhl("json")
            print(os.listdir(str(Path.cwd()/"media")))
            print(os.listdir(str(Path.cwd()/"media"/"montreal-canadiens")))
            time.sleep(2)
            return render_link("json")

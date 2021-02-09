from sports.programs import NhlStats
from django.core.management import call_command
import django
import sys
from bs4 import BeautifulSoup
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "My_Portfolio.settings")

django.setup()
from sports.models import Season, Team


def update_seasons(team, season):
    season_year = Season.objects.filter(year=season)
    if not season_year:
        Season.objects.create(year=season)
        season_obj = Season.objects.get(year=season)
    else:
        season_obj = season_year[0]

    if not season_obj.team.filter(name=team.title()):
        team_obj = Team.objects.get(name=team.title())
        season_obj.team.add(team_obj)


def update_league(league, update='all_seasons', season=None, start=None, end=None):
    if league == "NHL":
        lst_teams = [
            'Anaheim-Ducks',
            'Arizona-Coyotes',
            'Boston-Bruins',
            'Buffalo-Sabres',
            'Calgary-Flames',
            'Carolina-Hurricanes',
            'Chicago-Blackhawks',
            'Colorado-Avalanche',
            'Columbus-Blue-Jackets',
            'Dallas-Stars',
            'Detroit-Red-Wings',
            'Edmonton-Oilers',
            'Florida-Panthers',
            'Los-Angeles-Kings',
            'Minnesota-Wild',
            'Montreal-Canadiens',
            'Nashville-Predators',
            'New-Jersey-Devils',
            'New-York-Islanders',
            'New-York-Rangers',
            'Ottawa-Senators',
            'Philadelphia-Flyers',
            'Pittsburgh-Penguins',
            'San-Jose-Sharks',
            'St-Louis-Blues',
            'Tampa-Bay-Lightning',
            'Toronto-Maple-Leafs',
            'Vancouver-Canucks',
            'Vegas-Golden-Knights',
            'Washington-Capitals',
            'Winnipeg-Jets'
        ]
        if not start:
            start_i = 0
        else:
            for i in range(len(lst_teams)):
                if start.lower() in lst_teams[i].lower():
                    start_i = i
                    break

        if not end:
            end_i = None
        else:
            for i in range(len(lst_teams)):
                if end.lower() in lst_teams[i].lower():
                    end_i = i + 1
                    break

        if update == "all_seasons":
            for team in lst_teams[start_i:end_i]:
                NhlYears(team, "2020-2021").update_all_seasons()
        elif update == "one_season":
            for team in lst_teams[start_i:end_i]:
                NhlYears(team, season).update_one_season()


class NhlYears(NhlStats):
    def test_update_year(self, season):
        def get_soup():
            soup = BeautifulSoup(res.text, 'html.parser')
            base_css = 'table.table-striped.table-sortable.skater-stats.highlight-stats tbody + tbody tr:not(.space) '
            return soup.select(base_css + '.txt-blue')

        team = self.changed_name(self.team, season)
        url = f'https://www.eliteprospects.com/team/{self.index}/{team.lower()}/{season}?tab=stats'
        res = requests.get(url)
        res.raise_for_status()

        player_names = get_soup()
        if not player_names:
            return "No season"

        update_seasons(self.team, season)

    def update_one_season(self):
        self.test_update_year(self.season)

    def update_all_seasons(self):
        season = "2020-2021"
        while True:
            updated = self.test_update_year(season)
            if updated == "No season" and season != "2004-2005":
                break

            season = f"{int(season[:4])-1}-{int(season[-4:])-1}"


if __name__ == "__main__":
    NhlYears("canadiens", '2004-2005').update_one_season()

from django import template
import re
from ..models import Team

register = template.Library()


@register.simple_tag
def league_teams(league):
    teams = Team.objects.filter(league=league).order_by("name")
    return teams


@register.simple_tag
def clean_name(team):
    team = str(team.name).replace('-', ' ')
    return team


@register.simple_tag
def url_nhl_values(team):
    values_dict = {
        'Anaheim-Ducks': 'ducks',
        'Arizona-Coyotes': 'coyotes',
        'Boston-Bruins': 'bruins',
        'Buffalo-Sabres': 'sabres',
        'Calgary-Flames': 'flames',
        'Carolina-Hurricanes': 'hurricanes',
        'Chicago-Blackhawks': 'blackhawks',
        'Colorado-Avalanche': 'avalanche',
        'Columbus-Blue-Jackets': 'bluejackets',
        'Dallas-Stars': 'stars',
        'Detroit-Red-Wings': 'redwings',
        'Edmonton-Oilers': 'oilers',
        'Florida-Panthers': 'panthers',
        'Los-Angeles-Kings': 'kings',
        'Minnesota-Wild': 'wild',
        'Montreal-Canadiens': 'canadiens',
        'Nashville-Predators': 'predators',
        'New-Jersey-Devils': 'devils',
        'New-York-Islanders': 'islanders',
        'New-York-Rangers': 'rangers',
        'Ottawa-Senators': 'senators',
        'Philadelphia-Flyers': 'flyers',
        'Pittsburgh-Penguins': 'penguins',
        'San-Jose-Sharks': 'sharks',
        'St.-Louis-Blues': 'blues',
        'Tampa-Bay-Lightning': 'lightning',
        'Toronto-Maple-Leafs': 'mapleleafs',
        'Vancouver-Canucks': 'canucks',
        'Vegas-Golden-Knights': 'goldenknights',
        'Washington-Capitals': 'capitals',
        'Winnipeg-Jets': 'jets'
    }
    return values_dict[team.name]


@register.simple_tag
def url_elitep_values(team):
    values_dict = {
        'Anaheim-Ducks': 1580,
        'Arizona-Coyotes': 72,
        'Boston-Bruins': 52,
        'Buffalo-Sabres': 53,
        'Calgary-Flames': 54,
        'Carolina-Hurricanes': 55,
        'Chicago-Blackhawks': 56,
        'Colorado-Avalanche': 57,
        'Columbus-Blue-Jackets': 58,
        'Dallas-Stars': 59,
        'Detroit-Red-Wings': 60,
        'Edmonton-Oilers': 61,
        'Florida-Panthers': 62,
        'Los-Angeles-Kings': 79,
        'Minnesota-Wild': 63,
        'Montreal-Canadiens': 64,
        'Nashville-Predators': 65,
        'New-Jersey-Devils': 66,
        'New-York-Islanders': 67,
        'New-York-Rangers': 68,
        'Ottawa-Senators': 69,
        'Philadelphia-Flyers': 70,
        'Pittsburgh-Penguins': 71,
        'San-Jose-Sharks': 73,
        'St.-Louis-Blues': 74,
        'Tampa-Bay-Lightning': 75,
        'Toronto-Maple-Leafs': 76,
        'Vancouver-Canucks': 77,
        'Vegas-Golden-Knights': 22211,
        'Washington-Capitals': 78,
        'Winnipeg-Jets': 9966
    }
    return values_dict[team.name]


@register.simple_tag
def url_db_values(team, season):
    values_dict = {
        'Anaheim-Ducks': '004312',
        'Arizona-Coyotes': '007166',
        'Boston-Bruins': '000032',
        'Buffalo-Sabres': '000033',
        'Calgary-Flames': '000043',
        'Carolina-Hurricanes': '000979',
        'Chicago-Blackhawks': '000035',
        'Colorado-Avalanche': '000690',
        'Columbus-Blue-Jackets': '002330',
        'Dallas-Stars': '000233',
        'Detroit-Red-Wings': '000034',
        'Edmonton-Oilers': '000041',
        'Florida-Panthers': '000234',
        'Los-Angeles-Kings': '000040',
        'Minnesota-Wild': '002331',
        'Montreal-Canadiens': '000045',
        'Nashville-Predators': '001412',
        'New-Jersey-Devils': '000051',
        'New-York-Islanders': '007440',
        'New-York-Rangers': '000048',
        'Ottawa-Senators': '000054',
        'Philadelphia-Flyers': '000053',
        'Pittsburgh-Penguins': '000050',
        'San-Jose-Sharks': '000044',
        'St.-Louis-Blues': '000036',
        'Tampa-Bay-Lightning': '000055',
        'Toronto-Maple-Leafs': '000038',
        'Vancouver-Canucks': '000039',
        'Vegas-Golden-Knights': '007776',
        'Washington-Capitals': '000049',
        'Winnipeg-Jets': '006378'
    }
    season = season.year[5:]
    return values_dict[team.name] + season


@register.simple_tag
def clean_link(raw_link):
    link_regex = re.compile(r'(\\|/)media.*\.(xlsx|csv|pdf|json|txt)')
    return link_regex.search(raw_link).group(0)


@ register.simple_tag
def lower(string):
    return string.lower()


@ register.simple_tag
def url_nba_values(team, season):
    values_dict = {
        'Atlanta-Hawks': 'hawks',
        'Boston-Celtics': 'celtics',
        'Brooklyn-Nets': 'nets',
        'Charlotte-Hornets': 'hornets',
        'Chicago-Bulls': 'bulls',
        'Cleveland-Cavaliers': 'cavaliers',
        'Dallas-Mavericks': 'mavericks',
        'Denver-Nuggets': 'nuggets',
        'Detroit-Pistons': 'pistons',
        'Golden-State-Warriors': 'warriors',
        'Houston-Rockets': 'rockets',
        'Indiana-Pacers': 'pacers',
        'Los-Angeles-Clippers': 'clippers',
        'Los-Angeles-Lakers': 'lakers',
        'Memphis-Grizzlies': 'grizzlies',
        'Miami-Heat': 'heat',
        'Milwaukee-Bucks': 'bucks',
        'Minnesota-Timberwolves': 'timberwolves',
        'New-Orleans-Pelicans': 'pelicans',
        'New-York-Knicks': 'knicks',
        'Oklahoma-City-Thunder': 'thunder',
        'Orlando-Magic': 'magic',
        'Philadelphia-76ers': '76ers',
        'Phoenix-Suns': 'suns',
        'Portland-Trail-Blazers': 'blazers',
        'Sacramento-Kings': 'kings',
        'San-Antonio-Spurs': 'spurs',
        'Toronto-Raptors': 'raptors',
        'Utah-Jazz': 'jazz',
        'Washington-Wizards': 'wizards',
    }
    season_regex = re.compile(r'(\d{4}\-)\d{2}(\d{2})')
    season_obj = season_regex.search(season.year)
    season_year = season_obj.group(1) + season_obj.group(2)
    return f'{values_dict[team.name]}/stats?season={season_year}'


@ register.simple_tag
def url_espn_nba_values(team, season):
    values_dict = {
        'Atlanta-Hawks': 'atl',
        'Boston-Celtics': 'bos',
        'Brooklyn-Nets': 'bkn',
        'Charlotte-Hornets': 'cha',
        'Chicago-Bulls': 'chi',
        'Cleveland-Cavaliers': 'cle',
        'Dallas-Mavericks': 'dal',
        'Denver-Nuggets': 'den',
        'Detroit-Pistons': 'det',
        'Golden-State-Warriors': 'gs',
        'Houston-Rockets': 'hou',
        'Indiana-Pacers': 'ind',
        'Los-Angeles-Clippers': 'lac',
        'Los-Angeles-Lakers': 'lal',
        'Memphis-Grizzlies': 'mem',
        'Miami-Heat': 'mia',
        'Milwaukee-Bucks': 'mil',
        'Minnesota-Timberwolves': 'min',
        'New-Orleans-Pelicans': 'no',
        'New-York-Knicks': 'ny',
        'Oklahoma-City-Thunder': 'okc',
        'Orlando-Magic': 'orl',
        'Philadelphia-76ers': 'phi',
        'Phoenix-Suns': 'phx',
        'Portland-Trail-Blazers': 'por',
        'Sacramento-Kings': 'sac',
        'San-Antonio-Spurs': 'sa',
        'Toronto-Raptors': 'tor',
        'Utah-Jazz': 'utah',
        'Washington-Wizards': 'wsh',
    }
    season_year = season.year[-4:]
    return f'{values_dict[team.name]}/season/{season_year}'


@ register.simple_tag
def url_bask_ref_values(team, season):
    values_dict = {
        'Atlanta-Hawks': 'ATL',
        'Boston-Celtics': 'BOS',
        'Brooklyn-Nets': 'BRK',
        'Charlotte-Hornets': 'CHA',
        'Chicago-Bulls': 'CHI',
        'Cleveland-Cavaliers': 'CLE',
        'Dallas-Mavericks': 'DAL',
        'Denver-Nuggets': 'DEN',
        'Detroit-Pistons': 'DET',
        'Golden-State-Warriors': 'GSW',
        'Houston-Rockets': 'HOU',
        'Indiana-Pacers': 'IND',
        'Los-Angeles-Clippers': 'LAC',
        'Los-Angeles-Lakers': 'LAL',
        'Memphis-Grizzlies': 'MEM',
        'Miami-Heat': 'MIA',
        'Milwaukee-Bucks': 'MIL',
        'Minnesota-Timberwolves': 'MIN',
        'New-Orleans-Pelicans': 'NOP',
        'New-York-Knicks': 'NYK',
        'Oklahoma-City-Thunder': 'OKC',
        'Orlando-Magic': 'ORL',
        'Philadelphia-76ers': 'PHI',
        'Phoenix-Suns': 'PHO',
        'Portland-Trail-Blazers': 'POR',
        'Sacramento-Kings': 'SAC',
        'San-Antonio-Spurs': 'SAS',
        'Toronto-Raptors': 'TOR',
        'Utah-Jazz': 'UTA',
        'Washington-Wizards': 'WAS',
    }
    season_year = season.year[-4:]
    return f"{values_dict[team.name]}/{season_year}"


@ register.simple_tag
def url_mlb_values(team, season):
    values_dict = {
        'Arizona-Diamondbacks': 'dbacks',
        'Atlanta-Braves': 'braves',
        'Baltimore-Orioles': 'orioles',
        'Boston-Red-Sox': 'redsox',
        'Chicago-White-Sox': 'whitesox',
        'Chicago-Cubs': 'cubs',
        'Cincinnati-Reds': 'reds',
        'Cleveland-Indians': 'indians',
        'Colorado-Rockies': 'rockies',
        'Detroit-Tigers': 'tigers',
        'Houston-Astros': 'astros',
        'Kansas-City-Royals': 'royals',
        'Los-Angeles-Angels': 'angels',
        'Los-Angeles-Dodgers': 'dodgers',
        'Miami-Marlins': 'marlins',
        'Milwaukee-Brewers': 'brewers',
        'Minnesota-Twins': 'twins',
        'New-York-Yankees': 'yankees',
        'New-York-Mets': 'mets',
        'Oakland-Athletics': 'athletics',
        'Philadelphia-Phillies': 'phillies',
        'Pittsburgh-Pirates': 'pirates',
        'San-Diego-Padres': 'padres',
        'San-Francisco-Giants': 'giants',
        'Seattle-Mariners': 'mariners',
        'St-Louis-Cardinals': 'cardinals',
        'Tampa-Bay-Rays': 'rays',
        'Texas-Rangers': 'rangers',
        'Toronto-Blue-Jays': 'bluejays',
        'Washington-Nationals': 'nationals'
    }
    season_year = season.year[-4:]

    return f"{values_dict[team.name]}/stats/{season_year}"


@ register.simple_tag
def url_espn_mlb_values(team, season):
    values_dict = {
        'Arizona-Diamondbacks': 'ari',
        'Atlanta-Braves': 'atl',
        'Baltimore-Orioles': 'bal',
        'Boston-Red-Sox': 'bos',
        'Chicago-White-Sox': 'chw',
        'Chicago-Cubs': 'chc',
        'Cincinnati-Reds': 'cin',
        'Cleveland-Indians': 'cle',
        'Colorado-Rockies': 'col',
        'Detroit-Tigers': 'det',
        'Houston-Astros': 'hou',
        'Kansas-City-Royals': 'kc',
        'Los-Angeles-Angels': 'laa',
        'Los-Angeles-Dodgers': 'lad',
        'Miami-Marlins': 'mia',
        'Milwaukee-Brewers': 'mil',
        'Minnesota-Twins': 'min',
        'New-York-Yankees': 'nyy',
        'New-York-Mets': 'nym',
        'Oakland-Athletics': 'oak',
        'Philadelphia-Phillies': 'phi',
        'Pittsburgh-Pirates': 'pit',
        'San-Diego-Padres': 'sd',
        'San-Francisco-Giants': 'sf',
        'Seattle-Mariners': 'sea',
        'St-Louis-Cardinals': 'stl',
        'Tampa-Bay-Rays': 'tb',
        'Texas-Rangers': 'tex',
        'Toronto-Blue-Jays': 'tor',
        'Washington-Nationals': 'wsh'
    }
    season_year = season.year[-4:]
    return f'{values_dict[team.name]}/season/{season_year}'


@ register.simple_tag
def url_base_ref_values(team, season):
    values_dict = {
        'Arizona-Diamondbacks': 'ARI',
        'Atlanta-Braves': 'ATL',
        'Baltimore-Orioles': 'BAL',
        'Boston-Red-Sox': 'BOS',
        'Chicago-White-Sox': 'CHW',
        'Chicago-Cubs': 'CHC',
        'Cincinnati-Reds': 'CIN',
        'Cleveland-Indians': 'CLE',
        'Colorado-Rockies': 'COL',
        'Detroit-Tigers': 'DET',
        'Houston-Astros': 'HOU',
        'Kansas-City-Royals': 'KCR',
        'Los-Angeles-Angels': 'LAA',
        'Los-Angeles-Dodgers': 'LAD',
        'Miami-Marlins': 'MIA',
        'Milwaukee-Brewers': 'MIL',
        'Minnesota-Twins': 'MIN',
        'New-York-Yankees': 'NYY',
        'New-York-Mets': 'NYM',
        'Oakland-Athletics': 'OAK',
        'Philadelphia-Phillies': 'PHI',
        'Pittsburgh-Pirates': 'PIT',
        'San-Diego-Padres': 'SDP',
        'San-Francisco-Giants': 'SFG',
        'Seattle-Mariners': 'SEA',
        'St-Louis-Cardinals': 'STL',
        'Tampa-Bay-Rays': 'TBR',
        'Texas-Rangers': 'TEX',
        'Toronto-Blue-Jays': 'TOR',
        'Washington-Nationals': 'WSN'
    }
    season_year = season.year[-4:]
    return f"{values_dict[team.name]}/{season_year}"


@ register.simple_tag
def url_nfl_values(team, season):
    values_dict = {
        'Arizona-Cardinals': 'azcardinals',
        'Atlanta-Falcons': 'atlantafalcons',
        'Baltimore-Ravens': 'baltimoreravens',
        'Buffalo-Bills': 'buffalobills',
        'Carolina-Panthers': 'panthers',
        'Chicago-Bears': 'chicagobears',
        'Cincinnati-Bengals': 'bengals',
        'Cleveland-Browns': 'clevelandbrowns',
        'Dallas-Cowboys': 'dallascowboys',
        'Denver-Broncos': 'denverbroncos',
        'Detroit-Lions': 'detroitlions',
        'Green-Bay-Packers': 'packers',
        'Houston-Texans': 'houstontexans',
        'Indianapolis-Colts': 'colts',
        'Jacksonville-Jaguars': 'jaguars',
        'Kansas-City-Chiefs': 'chiefs',
        'Las-Vegas-Raiders': 'raiders',
        'Los-Angeles-Chargers': 'chargers',
        'Los-Angeles-Rams': 'therams',
        'Miami-Dolphins': 'miamidolphins',
        'Minnesota-Vikings': 'vikings',
        'New-England-Patriots': 'patriots',
        'New-Orleans-Saints': 'neworleanssaints',
        'New-York-Giants': 'giants',
        'New-York-Jets': 'newyorkjets',
        'Philadelphia-Eagles': 'philadelphiaeagles',
        'Pittsburgh-Steelers': 'steelers',
        'San-Francisco-49ers': '49ers',
        'Seattle-Seahawks': 'seahawks',
        'Tampa-Bay-Buccaneers': 'buccaneers',
        'Tennessee-Titans': 'tennesseetitans',
        'Washington-Football-Team': 'washingtonfootball'
    }

    season_year = season.year[:4]
    return f"{values_dict[team.name]}.com/team/stats/{season_year}/REG"


@ register.simple_tag
def url_espn_nfl_values(team, season):
    values_dict = {
        'Arizona-Cardinals': 'ari',
        'Atlanta-Falcons': 'atl',
        'Baltimore-Ravens': 'bal',
        'Buffalo-Bills': 'buf',
        'Carolina-Panthers': 'car',
        'Chicago-Bears': 'chi',
        'Cincinnati-Bengals': 'cin',
        'Cleveland-Browns': 'cle',
        'Dallas-Cowboys': 'dal',
        'Denver-Broncos': 'den',
        'Detroit-Lions': 'det',
        'Green-Bay-Packers': 'gb',
        'Houston-Texans': 'hou',
        'Indianapolis-Colts': 'ind',
        'Jacksonville-Jaguars': 'jax',
        'Kansas-City-Chiefs': 'kc',
        'Las-Vegas-Raiders': 'lv',
        'Los-Angeles-Chargers': 'lac',
        'Los-Angeles-Rams': 'lar',
        'Miami-Dolphins': 'mia',
        'Minnesota-Vikings': 'min',
        'New-England-Patriots': 'ne',
        'New-Orleans-Saints': 'no',
        'New-York-Giants': 'nyg',
        'New-York-Jets': 'nyj',
        'Philadelphia-Eagles': 'phi',
        'Pittsburgh-Steelers': 'pit',
        'San-Francisco-49ers': 'sf',
        'Seattle-Seahawks': 'sea',
        'Tampa-Bay-Buccaneers': 'tb',
        'Tennessee-Titans': 'ten',
        'Washington-Football-Team': 'wsh'
    }

    season_year = season.year[:4]
    return f"{values_dict[team.name]}/season/{season_year}"


@ register.simple_tag
def url_foot_ref_values(team, season):
    values_dict = {
        'Arizona-Cardinals': 'crd',
        'Atlanta-Falcons': 'atl',
        'Baltimore-Ravens': 'rav',
        'Buffalo-Bills': 'buf',
        'Carolina-Panthers': 'car',
        'Chicago-Bears': 'chi',
        'Cincinnati-Bengals': 'cin',
        'Cleveland-Browns': 'cle',
        'Dallas-Cowboys': 'dal',
        'Denver-Broncos': 'den',
        'Detroit-Lions': 'det',
        'Green-Bay-Packers': 'gnb',
        'Houston-Texans': 'htx',
        'Indianapolis-Colts': 'clt',
        'Jacksonville-Jaguars': 'jax',
        'Kansas-City-Chiefs': 'kan',
        'Las-Vegas-Raiders': 'rai',
        'Los-Angeles-Chargers': 'sdg',
        'Los-Angeles-Rams': 'ram',
        'Miami-Dolphins': 'mia',
        'Minnesota-Vikings': 'min',
        'New-England-Patriots': 'nwe',
        'New-Orleans-Saints': 'nor',
        'New-York-Giants': 'nyg',
        'New-York-Jets': 'nyj',
        'Philadelphia-Eagles': 'phi',
        'Pittsburgh-Steelers': 'pit',
        'San-Francisco-49ers': 'sfo',
        'Seattle-Seahawks': 'sea',
        'Tampa-Bay-Buccaneers': 'tam',
        'Tennessee-Titans': 'oti',
        'Washington-Football-Team': 'was'
    }

    season_year = season.year[:4]
    return f"{values_dict[team.name]}/{season_year}"


"""
values_dict = {
        'Atlanta Hawks': ,
        'Boston Celtics': ,
        'Brooklyn Nets': ,
        'Charlotte Hornets': ,
        'Chicago Bulls': ,
        'Cleveland Cavaliers': ,
        'Dallas Mavericks': ,
        'Denver Nuggets': ,
        'Detroit Pistons': ,
        'Golden State Warriors': ,
        'Houston Rockets': ,
        'Indiana Pacers': ,
        'Los Angeles Clippers': ,
        'Los Angeles Lakers': ,
        'Memphis Grizzlies': ,
        'Miami Heat': ,
        'Milwaukee Bucks': ,
        'Minnesota Timberwolves': ,
        'New Orleans Pelicans': ,
        'New York Knicks': ,
        'Oklahoma City Thunder': ,
        'Orlando Magic': ,
        'Philadelphia 76ers': ,
        'Phoenix Suns': ,
        'Portland Trail Blazers': ,
        'Sacramento Kings': ,
        'San Antonio Spurs': ,
        'Toronto Raptors': ,
        'Utah Jazz': ,
        'Washington Wizards': ,
    }
"""

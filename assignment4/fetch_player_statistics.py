import os
import re
from operator import itemgetter
from typing import Dict, List
from urllib.parse import urljoin

import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from requesting_urls import get_html

## --- Task 8, 9 and 10 --- ##

try:
    import requests_cache
except ImportError:
    print("install requests_cache to improve performance")
    pass
else:
    requests_cache.install_cache()

base_url = "https://en.wikipedia.org"


def find_best_players(url: str) -> None:
    """Find the best players in the semifinals of the nba.

    This is the top 3 scorers from every team in semifinals.
    Displays plot over points, assists, rebounds

    arguments:
        - html (str) : html string from wiki basketball
    returns:
        - None
    """
    # Gets the teams
    teams = get_teams(url)
    assert len(teams) == 8, f"Testing length of teams: Expected 8, got {len(teams)}."

    # Gets the player for every team and stores in dict.
    all_players = {}
    for team in teams:
        all_players[team["name"]] = get_players(team["url"])

    # Gets player statistics for each player.
    for team, players in all_players.items(): # 'players' is a list of dicts
        for player in players: # 'player' is a dict of {'name': player_name, 'url': player_url}
            player_stats = get_player_stats(player["url"], team)
            
            # Simply appends the stats to the 'player' dictionary.
            for stat, number in player_stats.items():
                player[stat] = number  

    # 'all_players' is now of the form:
    # {
    #     "team name": [
    #         {
    #             "name": "player name",
    #             "url": "https://player_url",
    #             # added by get_player_stats
    #             "points": 5,
    #             "assists": 1.2,
    #             # ...,
    #         },
    #     ]
    # }

    # Selects top 3 player for each team by stat and plots the results.
    stats_to_plot = ["points", "assists", "rebounds"]
    for stat in stats_to_plot:
        
        best = {}
        for team, players in all_players.items():
            # Sorts and extracts top 3 based on stat
            top_3 = []
            top_sum = 0
            for player in players:
                if len(player) == 2: # Stats are missing
                    player[stat] = 0
                    top_3.append(player)
                else:
                    player_score = player[stat]
                    if player_score >= top_sum:
                        top_sum = player_score
                        top_3.insert(0, player)
            best[team] = top_3[:3]
            
        plot_best(best, stat=stat)


# This entire function is inspired from plot_NBA_player_statistics in example-plot.py
def plot_best(best: Dict[str, List[Dict]], stat: str = "points") -> None:
    """Plots a single stat for the top 3 players from every team.

    Arguments:
        best (dict) : dict with the top 3 players from every team
            has the form:

            {
                "team name": [
                    {
                        "name": "player name",
                        "points": 5,
                        ...
                    },
                ],
            }

            where the _keys_ are the team name,
            and the _values_ are lists of length 3,
            containing dictionaries about each player,
            with their name and stats.

        stat (str) : [points | assists | rebounds] which stat to plot.
            Should be a key in the player info dictionary.
    """
    stats_dir = "NBA_player_statistics"
    
    count_so_far = 0
    all_names = []
    
    color_count = 0

    # Iterates through each team and the players
    for team, players in best.items():
        
        # Picks a color from the team based on 'color_count'
        color = ""
        if color_count == 0:
            color = "blue"
            color_count += 1
        else:
            color = "red"
            color_count -= 1
        
        # Collects the stat and name of each player on the team
        stat_scores = []
        names = []
        for player in players:
            names.append(player["name"])
            stat_scores.append(player[stat])
            
        # Records all the names, for use later in x label
        all_names.extend(names)

        # The position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        
        # Makes bars for this team's players points with the team name as the label
        bars = plt.bar(x, stat_scores, color=color, label=team)
        
        # Adds the value as text on the bars
        plt.bar_label(bars)

    # Uses the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    
    # Adds the legend with the colors  for each team
    plt.legend(loc=0)
    
    # Turns off gridlines
    plt.grid(False)
    
    # Sets the title
    plt.title(f"{stat} per game")
    
    # Save the figure to a file
    plt.show()
    filename = f"{stats_dir}/{stat}.png"
    print(f"Creating {filename}")
    plt.savefig(filename, format="png")


def get_teams(url: str) -> list:
    """Extracts all the teams that were in the semi finals in nba

    arguments:
        - url (str) : url of the nba finals wikipedia page
    returns:
        teams (list) : list with all teams
            Each team is a dictionary of {'name': team name, 'url': team page
    """
    # Get the table
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Bracket").find_next("table")

    # find all rows in table
    rows = table.find_all("tr")
    rows = rows[2:]
    # maybe useful: identify cells that look like 'E1' or 'W5', etc.
    seed_pattern = re.compile(r"^[EW][1-8]$")

    # lots of ways to do this,
    # but one way is to build a set of team names in the semifinal
    # and a dict of {team name: team url}

    team_links = {}  # dict of team name: team url
    in_semifinal = set()  # set of teams in the semifinal

    # Loop over every row and extract teams from semi finals
    # also locate the links tot he team pages from the First Round column
    for row in rows:
        cols = row.find_all("td")
        # useful for showing structure
        # print([c.get_text(strip=True) for c in cols])

        # TODO:
        # 1. if First Round column, record team link from `a` tag
        # 2. if semifinal column, record team name

        # quarterfinal, E1/W8 is in column 1
        # team name, link is in column 2
        if len(cols) >= 3 and seed_pattern.match(cols[1].get_text(strip=True)):
            team_col = cols[2]
            a = team_col.find("a")
            team_links[team_col.get_text(strip=True)] = urljoin(base_url, a["href"])

        elif len(cols) >= 4 and seed_pattern.match(cols[2].get_text(strip=True)):
            team_col = cols[3]
            in_semifinal.add(team_col.get_text(strip=True))

        elif len(cols) >= 5 and seed_pattern.match(cols[3].get_text(strip=True)):
            team_col = cols[4]
            in_semifinal.add(team_col.get_text(strip=True))

    # return list of dicts (there will be 8):
    # [
    #     {
    #         "name": "team name",
    #         "url": "https://team url",
    #     }
    # ]

    assert len(in_semifinal) == 8
    return [
        {
            "name": team_name.rstrip("*"),
            "url": team_links[team_name],
        }
        for team_name in in_semifinal
    ]


def get_players(team_url: str) -> list:
    """Gets all the players from a team that were in the roster for semi finals
    arguments:
        team_url (str) : the url for the team
    returns:
        player_infos (list) : list of player info dictionaries
            with form: {'name': player name, 'url': player wikipedia page url}
    """
    print(f"Finding players in {team_url}")

    # Gets the table
    html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    roster = soup.find(id="Roster")
    table = roster.find_next("table")

    players = []

    # Loops over every row and get the names from roster
    rows = table.find_all("tr")
    for row in rows:
        # Get the columns
        cells = row.find_all("td")
        
        # Makes sure we are looking at the correct type of row with 7 columns.
        if len(cells) == 7:
            
            name_cell = cells[2]
            player_text = str(name_cell)
            player_name = name_cell.text.strip()
            
            # Finds name links (a tags)
            a_pat = r"(<a[^>]+>)"
            href_pat = r'href="([^"]+)"'
            a_match = re.search(a_pat, player_text)
            href_match = re.search(href_pat, a_match.group(1))
            
            player_url = f"https://en.wikipedia.org{href_match.group(1)}"
            
            # Adds players to a dict with {'name':, 'url':}
            player_dict = {'name':player_name, 'url':player_url}
            players.append(player_dict)

    # return the list of players
    return players


def get_player_stats(player_url: str, team: str) -> dict:
    """Gets the player stats for a player in a given team
    arguments:
        player_url (str) : url for the wiki page of player
        team (str) : the name of the team the player plays for
    returns:
        stats (dict) : dictionary with the keys (at least): points, assists, and rebounds keys
    """
    print(f"Fetching stats for player in {player_url}")

    # Get the table with stats
    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")
    NBA_regular_season = soup.find(id="NBA")
    if NBA_regular_season == None:
        NBA_regular_season = soup.find(id="Regular_season")
    table = NBA_regular_season.find_next("table")

    # Defines the dictionary which will contain the statistics.
    stats = {}

    rows = table.find_all("tr")
    rows = rows[1:]
    # Loop over rows and extract the stats
    for row in rows:
        cells = row.find_all("td")
        
        time_text = cells[0].text.strip()
        team_text = cells[1].text.strip()
        time_pat = r"(2021.22)"
        team_pat = rf"({team})"
        
        # Checks correct team (some players change team within season)
        if re.search(time_pat, time_text) != None and re.search(team_pat, team_text) != None :
            stat_pat = r"(\d*\.\d+)"
            
            # Loads the stats 'points', 'rebounds' and 'assists' from the columns
            rebounds = cells[8].text.strip()
            rebounds = re.search(stat_pat, rebounds)
            rebounds = float(rebounds.group(1))
            
            assists = cells[9].text.strip()
            assists = re.search(stat_pat, assists)
            assists = float(assists.group(1))
            
            points = cells[12].text.strip()
            points = re.search(stat_pat, points)
            points = float(points.group(1))
            
            stats["rebounds"] = rebounds
            stats["assists"] = assists
            stats["points"] = points

    return stats


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2022_NBA_playoffs"
    find_best_players(url)

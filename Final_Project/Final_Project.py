# final_project.py
# ESPN Hidden API - MLB Stats Analyzer
# pulls the last 3 days of MLB scores and saves them to CSVs
import requests
import json
import os
import datetime

# base url for the ESPN MLB scoreboard, we'll add the date to the end
url = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates="

# these are the keys we need to dig into the ESPN JSON response
events_key = "events"
status_key = "status"
competitions_key = "competitions"
competitors_key = "competitors"
team_key = "team"
records_key = "records"
summary_key = "summary"

# all our files go in the Final_Project folder
RESULTS_FILE = "Final_Project/results.json"
GAMES_CSV = "Final_Project/games.csv"
TEAMS_CSV = "Final_Project/teams.csv"


# a Team object holds the name, wins, and losses for one MLB team
class Team:
    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses

    # calculate win percentage, avoid dividing by zero if no games played
    def win_pct(self):
        total = self.wins + self.losses
        if total == 0:
            return 0.0
        return round(self.wins / total, 3)

    # convert to a dictionary so we can dump it to JSON later
    def to_dict(self):
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "win_pct": self.win_pct()
        }


# build a list of the last 3 days so we always have recent data
dates = []
for i in range(1):
    day = datetime.datetime.now() - datetime.timedelta(days=i)
    dates.append({
        "url_date": day.strftime("%Y%m%d"),       
        "display_date": day.strftime("%Y-%m-%d")  # CSVs look nicer with hyphens
    })

# open both CSVs in append mode so we never lose old data
games_file = open(GAMES_CSV, "a")
teams_file = open(TEAMS_CSV, "a")

# only write the headers if the file is brand new and empty
if os.path.getsize(GAMES_CSV) == 0:
    games_file.write("date, game, status, home_team, home_score, away_team, away_score\n")
if os.path.getsize(TEAMS_CSV) == 0:
    teams_file.write("date, name, wins, losses, win_pct\n")

all_games = []
all_teams = {}

# loop through each date and hit the ESPN API
for date in dates:
    complete_url = url + date["url_date"]
    display_date = date["display_date"]
    print(complete_url)

    request = requests.get(complete_url)
    scoreboard = json.loads(request.text)

    # loop through each game on that day
    for event in scoreboard.get(events_key, []):
        game_name = event.get("name", "Unknown")
        status = event.get(status_key, {}).get("type", {}).get("description", "")
        competitors = event.get(competitions_key, [{}])[0].get(competitors_key, [])

        home_team, away_team = "", ""
        home_score, away_score = "0", "0"

        # each game has two competitors, figure out which is home and which is away
        for c in competitors:
            name = c.get(team_key, {}).get("displayName", "Unknown")
            score = c.get("score", "0")
            record = c.get(records_key, [{}])[0]
            wins = int(record.get(summary_key, "0-0").split("-")[0])
            losses = int(record.get(summary_key, "0-0").split("-")[1])

            # only add each team once to avoid duplicates
            if name not in all_teams:
                all_teams[name] = Team(name, wins, losses)

            if c.get("homeAway") == "home":
                home_team = name
                home_score = score
            else:
                away_team = name
                away_score = score

        all_games.append({
            "game": game_name,
            "status": status,
            "home": {"team": home_team, "score": home_score},
            "away": {"team": away_team, "score": away_score}
        })

        # append this game as a new row in the CSV
        games_file.write(display_date + ", " + game_name + ", " + status + ", " + home_team + ", " + home_score + ", " + away_team + ", " + away_score + "\n")

    # save each team's current record for this date
    for name, team in all_teams.items():
        teams_file.write(display_date + ", " + team.name + ", " + str(team.wins) + ", " + str(team.losses) + ", " + str(team.win_pct()) + "\n")

# done writing, close both files
games_file.close()
teams_file.close()

# --- analysis ---

# sort teams by win percentage to find the top 5
teams_list = list(all_teams.values())
sorted_teams = sorted(teams_list, key=lambda t: t.win_pct(), reverse=True)
top5 = [t.to_dict() for t in sorted_teams[:5]]

# count how many teams have more wins than losses
winning_teams = [t for t in teams_list if t.wins > t.losses]

# add up all the scores to get the average runs per game
total, count = 0, 0
for g in all_games:
    home_score = g.get("home", {}).get("score", "0")
    away_score = g.get("away", {}).get("score", "0")
    if home_score.isdigit() and away_score.isdigit():
        total += int(home_score) + int(away_score)
        count += 1

avg_score = round(total / count, 1) if count > 0 else 0

# put all the analysis into one dictionary and save it to results.json
results = {
    "top_5_by_win_pct": top5,
    "teams_above_500": len(winning_teams),
    "avg_combined_score": avg_score,
    "recent_games": all_games
}

with open(RESULTS_FILE, "w") as f:
    json.dump(results, f, indent=4)

# read it back and print a quick summary to the console
with open(RESULTS_FILE, "r") as f:
    loaded = json.load(f)

print("\n-- Top 5 Teams --")
for t in loaded["top_5_by_win_pct"]:
    print(t["name"] + " | " + str(t["wins"]) + "W - " + str(t["losses"]) + "L | " + str(t["win_pct"]))

print("\n-- Avg Combined Score: " + str(loaded["avg_combined_score"]) + " runs --")
# When are the next habs games this week?

import requests
import arrow

def parse_games(schedule):
    parse = lambda game : {
        'date': game['date'],
        'home': game['games'][0]['teams']['home']['team']['name'],
        'away': game['games'][0]['teams']['away']['team']['name'],
        'venue': game['games'][0]['venue']['name']
    }
    games = list(map(lambda x: parse(x), schedule))
    return games

def gen_url():
    today = arrow.now().format('YYYY-MM-DD')
    next_week = arrow.now().replace(days=7).format('YYYY-MM-DD')
    url = f'https://statsapi.web.nhl.com/api/v1/schedule?teamId=8&startDate={today}&endDate={next_week}'
    return url

def print_games(games):
    for game in games:
        date = arrow.get(game['date']).format('dddd')
        home = game['home']
        away = game['away']
        venue = game['venue']
        fmt = f"{date}: {home} vs. {away} at the {venue}."
        print(fmt)

url = gen_url()
response = requests.get(url=url)
json = response.json()
games = parse_games(json['dates'])
print_games(games)


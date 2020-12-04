"""Advent of Code Score Timeline

Produces a terminal stdout for a private leaderboard, showing what order the users solved
the daily problems in as well as showing score given for that solution.

Requires env:
ADVENT_SESSION_COOKIE: session cookie with adventofcode
ADVENT_LEADERBOARD_NUMBER: uuid of leaderboard
"""
import os
import sys
import requests


def get_session_cookie_from_env():
    return {'session': os.getenv('ADVENT_SESSION_COOKIE')}


def get_stats_data_from_site():
    cookies = get_session_cookie_from_env()
    uuid = os.getenv('ADVENT_LEADERBOARD_NUMBER')
    r = requests.post(f'https://adventofcode.com/2020/leaderboard/private/view/{uuid}.json', cookies=cookies)
    if r.status_code != 200:
        print(f'Status Code: {r.status_code}')
        print(r)
    data = r.json()
    return data


def parse_timelime_from_data(data):
    timeline = []

    for member, value in data['members'].items():
        name = value['name']
        for day in value['completion_day_level'].keys():
            for level in value['completion_day_level'][day].keys():
                time = value['completion_day_level'][day][level]['get_star_ts']
                timeline.append([name, day, level, time])
    return timeline


def display_timeline_with_scores(timeline, user=None):
    s = sorted(timeline, key = lambda x: (x[1], x[2], x[3]))

    n = 5
    store = (0, 0)
    print('user', 'day', 'level', 'timestamp', 'points')
    for item in s:
        if store != (item[1], item[2]):
            store = (item[1], item[2])
            n = 5
        if not user:
            print(*item, n)
        elif item[0] == user:
            print(*item, n)
        
        n -= 1
    return


def main():
    data = get_stats_data_from_site()
    timeline = parse_timelime_from_data(data)
    display_timeline_with_scores(timeline)
    return


if __name__ == '__main__':
    main()

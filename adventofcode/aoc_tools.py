import requests
import json
import os

dir_name = os.path.dirname(os.path.abspath(__file__))

session_id = "53616c7465645f5fae56e3b8c4be3716cbb904d43fc868b6b47cc9eaef0ca4f266e8674017fdb17992036263cbcd2843"


def memoize(function):
    filename = dir_name + "/cache.dat"
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            cache = json.loads(file.read())
    except:             # If file doesn't exist or is corrupted, create a new cache
        cache = {}

    def decorator(day):
        day = str(day)
        if day not in cache:
            data = function(day)    # Peform the download
            cache[day] = data       # Put the data in the cache
            with open(filename, "w", encoding="utf-8") as file:
                file.write(json.dumps(cache))
            
        return cache[day]
    
    return decorator


@memoize
def get_input(day):
    cookies = { "session": session_id }
    url = "https://adventofcode.com/2021/day/{}/input".format(day)
    r = requests.get(url, cookies=cookies)

    print("Downloaded day", day)
    if r.status_code == 200:
        return r.text
    elif r.status_code == 400:
        raise PermissionError("Authentication failed.")
    else:
        raise ConnectionError("Unknown connection error", r.status_code)

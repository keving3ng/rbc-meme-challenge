#!/venv/bin/python
import requests

API = "https://memeservice.cfapps.io/api/memes"
PTS_THRESHOLD = 60000


try:
    response = requests.get(API)
    data = response.json()
except:
    print("Error")

def filter_memes(data, threshold=60000):
    return 0

def sum_total_points(data):
    total_pts = sum([meme['points'] for meme in data)
    return total_pts

def calc_rank(rank):
    return 0
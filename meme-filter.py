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

def calc_rank(data, rank):
    # The data is 0 indexed, rank will be 1
    points = data[rank - 1]['points']
    print("To earn rank {} on the meme leaderboard, you will need more than {} points".format(rank, points))
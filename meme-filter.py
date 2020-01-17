#!/venv/bin/python
import requests

API = "https://memeservice.cfapps.io/api/memes"

def print_clean_number(num):
    return '{:.1f}k'.format(num / 1000) 

def filter_memes(data, threshold=60000):
    for meme in data:
        if (meme['points'] < threshold):
            break
        print("{} pts - {} by {} on {}".format(print_clean_number(meme['points']), meme['title'], meme['author'], meme['link']))

def sum_total_points(data):
    total_pts = sum([meme['points'] for meme in data])
    return print_clean_number(total_pts)

def calc_rank(data, rank):
    # The data is 0 indexed, rank will be 1
    points = data[rank - 1]['points']
    print("To earn rank {} on the meme leaderboard, you will need more than {} points".format(rank, points))

if __name__ == "__main__":
    try:
        response = requests.get(API)
        data = response.json()
    except:
        print("Error")
    
    filter_memes(data)
    input('\nPress Enter to Continue...')
    print('\nPoints total={}'.format(sum_total_points(data)))
    input('\nPress Enter to Continue...')
    calc_rank(data, 1)
    calc_rank(data, 10)
    calc_rank(data, 100)
    calc_rank(data, 500)
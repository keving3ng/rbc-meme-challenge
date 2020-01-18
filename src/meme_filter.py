#! venv/bin/python
import requests

API = "https://memeservice.cfapps.io/api/memes"

def print_clean_number(num):
    '''
    Utility function to cleanup long numbers for better displaying.
    Supports numbers: 1 000 >= num < 1 000 000
    
    Args:
        num (int): the long number to convert

    Returns:
        formatted string of float

    Exceptions:
        None

    Ex:
        >>> print_clean_number(131500)
        131.5k
    '''
    return '{:.1f}k'.format(num / 1000) 

def filter_memes(data, threshold=60000, printout=True):
    '''
    Filters out memes using list comprehension for all memes above a points threshold

    Args:
        data     (dict): dict representation of the api data
        threshold (int): cutoff for memes to be added to the list. defaults to 60000
        printout (bool): toggle print out of popular memes. defaults to True

    Returns:
        int of number of popular memes over the threshold/cutoff

    Exceptions:
        None

    Ex:
        >>> filter_memes(data, threshold=1000000000, printout=False)
        0
    '''
    popular_memes = [meme for meme in data if meme['points'] > threshold]
    
    if printout:
        for meme in popular_memes:
            print("{} pts - {} by {} on {}".format(print_clean_number(meme['points']), meme['title'], meme['author'], meme['link']))
    
    return len(popular_memes)

def sum_total_points(data):
    '''
    Sums the points of all memes in the meme dataset. 

    Args:
        data (dict): dict representation of the api data
 
    Returns:
        int of the total number of points of all memes in the data

    Exceptions:
        None

    Ex:
        >>> sum_total_points(data)
        18726243
    '''
    total_pts = sum([meme['points'] for meme in data])
    return total_pts

def calc_rank(data, rank, printout=True):
    '''
    Determines the amount of points required to reach a given rank on the meme leaderboards.

    Args:
        data     (dict): dict representation of the api data
        rank      (int): desired rank 
        printout (bool): toggle to enable/disable printing out message. defaults to True

    Returns:
        int of the number of points required to reach the given rank

    Exceptions:
        IndexError if rank is not within the range of the dataset

    Ex:
        >>> calc_rank(data, 2000, printout=False)
        Index out of range
        >>> calc_rank(data, 1, printout=False)
        70000
    '''
    try:
        points = data[rank - 1]['points']
    except IndexError:
        print("Index out of range")

    if printout:
        print("To earn rank {} on the meme leaderboard, you will need more than {} points".format(rank, points))
        
    return points

if __name__ == "__main__":
    try:
        response = requests.get(API)
        data = response.json()
    except:
        print("Error")
    
    print(filter_memes(data, threshold=60000))
    input('\nPress Enter to Continue...')
    print('\nPoints total={}'.format(sum_total_points(data)))
    input('\nPress Enter to Continue...')
    calc_rank(data, 1)
    calc_rank(data, 10)
    calc_rank(data, 100)
    calc_rank(data, 500)
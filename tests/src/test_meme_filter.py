#! venv/bin/python
import sys
import pytest
import json
from unittest import mock

sys.path.append("src")
import meme_filter

with open("tests/data/test_data.json") as f:
    data = json.load(f)

@pytest.mark.parametrize("threshold, exp_num", [(60000, 13), (30000, 277), (70000, 9), (20000, 803)])
def test_filter_memes(threshold, exp_num):
    assert meme_filter.filter_memes(data, threshold) == exp_num

def test_sum_total_points():
    assert meme_filter.sum_total_points(data) == 25783017

@pytest.mark.parametrize("rank, points", [(1, 194635), (10, 69180), (100, 38596), (500, 25204)])
def test_calc_rank(rank, points):
    assert meme_filter.calc_rank(data, rank) == points
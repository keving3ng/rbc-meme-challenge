#! venv/bin/python
import sys
import pytest
import json
from unittest import mock

sys.path.append("src")
import meme_filter

with open("tests/data/test_data.json") as f:
    data = json.load(f)

# def test_filtermemes():
#     pass
print(data)
@pytest.mark.parametrize("rank, points", [(1, 194635), (10, 69180), (100, 38596), (500, 25204)])
def test_calc_rank(rank, points):
    assert meme_filter.calc_rank(data, rank) == points
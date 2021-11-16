import pytest
import requests


class TestBudget:
    URL = "http://10.0.0.58:5000/"
    all_items = "{}/item".format(URL)

    def test_get_books(self):
        r = requests.get(TestBudget.all_items)
        assert r.status_code == 200
    

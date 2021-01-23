from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_player(self):
        league = ["English", "Spanish", "German"]
        pack = ["Gold", "Silver", "Bronze"]
        player_name = [b"Pogba" ]

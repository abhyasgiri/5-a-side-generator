from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_player(self):
        information 
        with patch("random.choice") as m:
            m.return_value.text = "Pogba"
            response = self.client.get(url_for("get_player"), json={"league" : "English", "pack" : "Gold"})
            self.assertIn(b"Pogba", response.data)
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app, db
from application.models import Players

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Players(player_name = "test_player"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_one(self):
        with requests_mock.mock() as a:
            a.get("http://football-cards_service-2:5002/league", text="English")
            a.get("http://football-cards_service-3:5000/pack", text="Gold")
            a.post("http://football-cards_service-4:5000/player", text="Pogba")
            response = self.client.get(url_for('index'))
            self.assertIn(b"You have won Pogba from a Gold pack in the English league!", response.data) #need to correct frontend display
            self.assertIn(b"You have won test_player", response.data) #maybe remove this? it tries to check for test_player from above but i dont think that goes through the system as it doesnt have a pack or league




from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app
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
        with requests_mock.mock() as m:
            m.get("http://football-cards_nation-backend:5002/league", json= {"league" : "English"})
            m.get("http://football-cards_pack_backend:5003/pack", json= {"pack" : "Gold"})
            m.post("http://football-cards_player_backend:5004/player", text="Pogba")
            response = self.client.get(url_for('index'))
            self.assertIn(b"English", response.data)
            self.assertIn(b"Gold", response.data)
            self.assertIn(b"Pogba", response.data)
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "English", "pack" : "Gold"})
        self.assertEqual(b"Pogba", response.data)

    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "English", "pack" : "Silver"})
        self.assertEqual(b"Grealish", response.data)
        
    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "English", "pack" : "Bronze"})
        self.assertEqual(b"Knight", response.data)

    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "Spanish", "pack" : "Gold"})
        self.assertEqual(b"Messi", response.data)

    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "Spanish", "pack" : "Silver"})
        self.assertEqual(b"Alvaro Vallejo", response.data)

    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "Spanish", "pack" : "Bronze"})
        self.assertEqual(b"Ximo Navarro", response.data)

    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "German", "pack" : "Gold"})
        self.assertEqual(b"Jaden Sancho", response.data)

    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "German", "pack" : "Silver"})
        self.assertEqual(b"Thomas Friedrich", response.data)

    def test_player(self):
        response = self.client.post(url_for('get_player'), json={"league" : "German", "pack" : "Bronze"})
        self.assertEqual(b"Drexler", response.data)
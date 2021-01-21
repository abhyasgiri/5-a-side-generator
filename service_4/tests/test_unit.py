from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_player(self):
        with patch("random.choice") as m:
            m.return_value = "Gold"
            response = self.client.get(url_for('get_pack'))
            self.assertIn(b"Gold", response.data)

#        for _ in range(10):
#            response = self.client.get(url_for('get_pack'))
#            self.assertIn(response.data, [b"Gold", b"Silver", b"Bronze"])

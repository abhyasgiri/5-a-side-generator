from application import app
from flask import request, jsonify
import random

@app.route("/league", methods=["GET"])
def get_league():
    leagues = ["English", "Spanish", "German"]
    return jsonify({"league" : random.choice(leagues)})


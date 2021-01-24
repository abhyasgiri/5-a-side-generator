from application import app
from flask import request, jsonify
import random

@app.route("/league", methods=["GET"])
def get_league():
    leagues = ["ENGLISH", "SPANISH", "GERMAN"]
    return jsonify({"league" : random.choice(leagues)})


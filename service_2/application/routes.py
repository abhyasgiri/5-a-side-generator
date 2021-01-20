from application import app
from flask import request, jsonify
import random

@app.route("/league", methods=["GET"])
def get_league():
    leagues = ["English", "Spanish", "German"]
    return jsonify({"league" : random.choice(leagues)})


#maybe make this more complex by allowing each team to have at least one GK, max 2 attackers and max 2 defenders
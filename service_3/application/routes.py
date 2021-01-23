from application import app
from flask import request, jsonify
import random

@app.route("/pack", methods=["GET"])
def get_pack():
    packs = ["Gold", "Silver", "Bronze"]
    return jsonify({"pack" : random.choices(packs, weights = [80, 10 ,10], k=1)[0]})
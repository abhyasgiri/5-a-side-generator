from application import app
from flask import request, Response

@app.route("/team", methods=["POST"])
def get_team():
    team = ["Team A", "Team B", "Team C"]
    position[player] = request.data.decode('utf-8')
    return Response(position[player] + " will play for " + str(random.choice(team)), mimetype='text/plain')
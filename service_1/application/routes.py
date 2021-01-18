from application import app
import requests

@app.route("/")
def index():
    player_response = requests.get("http://football-frontend:5000/player")
    position_response = requests.post("http://football-frontend:5000/position", data=player_response.text)
    team_response = requests.post("http://football-frontend:5000/team", data=player_response.text, position_response.text)
    return render_template("index.html", player=player_response.text, position=position_reponse.text, team=team_response.text)

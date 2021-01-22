from application import app, db
import requests
from application.models import Players
from flask import render_template, flash

@app.route("/")
def index():
    league_response = requests.get("http://football-cards_nation-backend:5002/league")
    pack_response = requests.get("http://football-cards_pack-backend:5003/pack", data=league_response.text)

    information = {'league': league_response.json()["league"] , 'pack': pack_response.json()["pack"]}

    player_response = requests.post("http://football-cards_player-backend:5004/player", json=information)

    new_player = Players(player_name=player_response.text)
    db.session.add(new_player)
    db.session.commit()

    all_players = Players.query.all()

    return render_template("index.html", new_player=player_response.text, pack=pack_response.json()["pack"], league=league_response.json()["league"], all_players=all_players)


#do logic in service 4
#player picks a random league, gets a random pack (gold, silver, bronze), 
#happy hour and normal times - happy hour the chance of getting gold pack is 50%
#and if you get a silver pack, you get two players

#make the query a bit more selective - 
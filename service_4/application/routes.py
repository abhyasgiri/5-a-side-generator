from application import app
from flask import request, Response
import random 

@app.route("/player", methods=["POST"])
def get_player():
    pack = request.json["pack"]
    league = request.json["league"]
    if league == "English" and pack == "Gold":
        players_pack = ["Pogba", "Firmino", "Son", "Kane"]
        player_name = random.choice(players_pack)
        return Response(player_name, mimetype ='text/plain')
    elif league == "English" and pack == "Silver":
        players_pack = ["Grealish", "Baily", "Neto", "Matip"]
        player_name = random.choice(players_pack)
        return Response(player_name, mimetype ='text/plain')
    elif league == "English" and pack == "Bronze":
        players_pack = ["Knight", "Obafemi", "Shabani"]
        player_name = random.choice(players_pack) 
        return Response(player_name, mimetype ='text/plain')
    elif league == "Spanish" and pack == "Gold":
        players_pack = ["Hazard", "Messi", "Suarez", "Joao Felix"]
        player_name = random.choice(players_pack) 
        return Response(player_name, mimetype ='text/plain')
    elif league == "Spanish" and pack == "Silver":
        players_pack = ["Jose Espino", "Alvaro Vallejo", "Sergio Leon"]
        player_name = random.choice(players_pack) 
        return Response(player_name, mimetype ='text/plain')
    elif league == "Spanish" and pack == "Bronze":
        players_pack = ["Fede Vadillo", "Ximo Navarro", "Mosquera"]
        player_name = random.choice(players_pack) 
        return Response(player_name, mimetype ='text/plain')
    elif league == "German" and pack == "Gold":
        players_pack = ["Jaden Sancho", "Erling Halland", "Robert Lewandowski", "Serge Gnabry"]
        player_name = random.choice(players_pack) 
        return Response(player_name, mimetype ='text/plain')
    elif league == "German" and pack == "Silver":
        players_pack = ["Richter", "Ziegler", "Thomas Friedrich"]
        player_name = random.choice(players_pack) 
        return Response(player_name, mimetype ='text/plain')
    elif league == "German" and pack == "Bronze":
        players_pack = ["Schmelzer", "Drexler", "Geiger"]
        player_name = random.choice(players_pack) 
        return Response(player_name, mimetype ='text/plain')

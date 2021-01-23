from application import app
from flask import request, Response
import random 

@app.route("/player", methods=["POST"])
def get_player():
    pack = request.json["pack"]
    league = request.json["league"]
    if league == "English" and pack == "Gold":
        player_name = "Pogba"
        return Response(player_name, mimetype ='text/plain')
    elif league == "English" and pack == "Silver":
        player_name = "Grealish"
        return Response(player_name, mimetype ='text/plain')
    elif league == "English" and pack == "Bronze":
        player_name = "Knight"
        return Response(player_name, mimetype ='text/plain')
    elif league == "Spanish" and pack == "Gold":
        player_name = "Messi"
        return Response(player_name, mimetype ='text/plain')
    elif league == "Spanish" and pack == "Silver":
        player_name = "Alvaro Vallejo"
        return Response(player_name, mimetype ='text/plain')
    elif league == "Spanish" and pack == "Bronze":
        player_name = "Ximo Navarro"
        return Response(player_name, mimetype ='text/plain')
    elif league == "German" and pack == "Gold":
        player_name = "Jaden Sancho"
        return Response(player_name, mimetype ='text/plain')
    elif league == "German" and pack == "Silver":
        player_name = "Thomas Friedrich"
        return Response(player_name, mimetype ='text/plain')
    elif league == "German" and pack == "Bronze":
        player_name = "Drexler"
        return Response(player_name, mimetype ='text/plain')

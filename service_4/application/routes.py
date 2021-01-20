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


#to imporve it i can choose a player to come from a separate database
#if testing for each if statement is getting tedious maybe only have gold and silver packs 
'''
players = [
    {
        "league": "English",
        "pack": "Gold",
        "player_name": ["Pogba", "Firmino", "Son", "Kane"]
    },
    {
        "league": "English",
        "pack": "Silver",
        "player_name": ["Grealish", "Baily", "Neto", "Matip"]
    },

    {
        "league": "English",
        "pack": "Bronze",
        "player_name": ["Knight", "Obafemi", "Shabani"]
    } 

    {
        league: "Spanish",
        pack: "Gold",
        player_name: ["Hazard", "Messi", "Suarez", "Joao Felix"]
    },

    {
        league: "Spanish",
        pack: "Silver",
        player_name: ["Doumbia", "Jose Espino", "Alvaro Vallejo", "Sergio Leon"]
    },

    {
        league: "Spanish",
        pack: "Bronze",
        player_name: ["Fede Vadillo", "Ximo Navarro", "Mosquera"]
    },

    {
        league: "German",
        pack: "Gold",
        player_name: ["Jaden Sancho", "Erling Halland", "Robert Lewandowski", "Serge Gnabry"]
    },

    {
        league: "German",
        pack: "Silver",
        player_name: ["Richter", "Ziegler", "Thomas Friedrich"]
    },

    {
        league: "German",
        pack: "Bronze",
        player_name: ["Schmelzer", "Drexler", "Geiger"]
    }
]
''' 

#using the nation and the pack, this service gives us a player card(s) 

#(which is a choice between 2 players)
#two different modes: normal run, and there will be happy hour mode where the chance of getting Gold pack 50% instead of 33%
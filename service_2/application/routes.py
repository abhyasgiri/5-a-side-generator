from application import app
from flask import request, Response
import random 

@app.route("/player", methods=["GET"])
def get_player():
    players = ["Best", "Pele", "Maradona", "Zidane", "Ronaldo", "Ronaldinho", "Cryuff", "Gullit", "Maldini", "Beckenbauer", "Roberto Carlos", "Henry", "C.Ronaldo", "Messi", "Cannavaro"]
    return Response(str(random.choice(players)), mimetype='text/plain')


#maybe make this more complex by allowing each team to have at least one GK, max 2 attackers and max 2 defenders
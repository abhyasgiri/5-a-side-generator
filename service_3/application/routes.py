from application import app
from flask import request, Response

@app.route("/position", methods=["POST"])
def get_position():
    position = {"Best" : "Attacker" , "Pele" : "Attacker", "Maradona" : "Midfielder", "Zidane" : "Midfielder", "Ronaldo" : "Attacker", "Ronaldinho" : "Midfielder", "Cryuff" : "Midfielder", "Gullit" : "Midfielder", "Maldini" : "Defender", "Beckenbauer" : "Defender", "Roberto Carlos" : "Defender", "Henry" : "Attacker", "C.Ronaldo" : "Attacker", "Messi" : "Attacker", "Cannavaro": "Defender"}
    player = request.data.decode('utf-8')
    return Response(position[player], mimetype='text/plain')
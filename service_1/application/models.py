from application import db

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(40), nullable=False)

#class Packs(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    pack = db.Column(db.String(10), nullable=False)

#class Leagues(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    league = db.Column(db.String(10), nullable=False)
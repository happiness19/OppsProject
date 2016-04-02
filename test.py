from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "UserInformation"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(18), unique=True)
    password = db.Column(db.String(25))
    team = db.Column(db.String(10))

    def __init__(self, username, password,team):
        self.username = username
        self.password = password
        (self.latitude, self.longitude) = (40.443034,-79.942180)
        self.team = team

    def __repr__(self):
        return '<User %r>' % self.username

class Portal(db.Model):
    __tablename__="PortalStatus"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10),unique=True)
    status = db.Column(db.String(20))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    
    def __init__(self,name,coordinates):
        self.name = name
        self.status = "unoccupied"
        self.latitude, self.longitude = coordinates
        if self.name == "UC": superPortal = True
        else: superPortal = False
        self.superPortal = superPortal

    def __repr__(self):
        return '<Portal %r at (%f, %f)>' % (self.name, self.latitude,self.longitude)

db.create_all()
portals = ({"CFA":(40.441619, -79.942977), "Porter":(40.441700, -79.946314),
            "Gates":(40.443437, -79.944672),"UC":(40.443388, -79.942001),
            "MM":(40.442016, -79.941507),"Wean":(40.442661, -79.945831),
            "DH":(40.442498, -79.944479),"Hunt":(40.441069, -79.943728),
            "SYG":(40.441069, -79.943728),"Donner":(40.441894, -79.940263),
            "Rez":(40.447046, -79.946720)})


for portal,coordinates in portals.items():
    newPortal = Portal(portal,coordinates)
    db.session.add(newPortal)
    db.session.commit()
from flask_sqlalchemy import SQLAlchemy

from .views import app

#Create database connection object
db = SQLAlchemy(app)

class Host(db.Model):
    __tablename__ = "hosts"
    ip = db.Column(db.Text,primary_key=True)
    timestamp = db.Column(db.Integer)
    hostname = db.Column(db.Text)
    open = db.Column(db.Text)
    filtered = db.Column(db.Text)

    def __init__(self, ip, timestamp, hostname,  open, filtered):
        self.timestamp = timestamp
        self.hostname = hostname
        self.open = open
        self.filtered = filtered

db.create_all  

  #  (top_port_scan, os_detection, ver_detection, tcp_scan, syn_scan)
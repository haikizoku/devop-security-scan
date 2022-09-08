from flask_sqlalchemy import SQLAlchemy
import logging as lg   #pour la journalisation

from .views import app

#Create database connection object
db = SQLAlchemy(app)

class Host(db.Model):
    __tablename__ = "hosts"
    ip = db.Column(db.Text,primary_key=True)
    timeout = float
    hostname = db.Column(db.Text)
    state = db.Column(db.Text)
    filtered = db.Column(db.Text)

    def __init__(self, ip, timeout: float, hostname,  state, filtered):
        self.timeout = timeout
        self.hostname = hostname
        self.state = open
        self.filtered = filtered

db.create_all  

def init_db():
  db.drop_all()
  db.create_all()
  db.session.add(Host("open", 1))
  db.session.add(Host("hostname", 2))
  db.session.commit()
  lg.warning('Database initialized!')

  #  (top_port_scan, os_detection, ver_detection, tcp_scan, syn_scan)
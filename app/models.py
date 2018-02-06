from app import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    artist = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date, nullable=False)

    def __init__(self, artist, name, release_date):
        self.artist = artist
        self.name = name
        self.release_date = release_date

    def __repr__(self):
        return '<Album %r>' % self.name

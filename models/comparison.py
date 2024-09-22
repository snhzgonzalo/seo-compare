from datetime import datetime
from extensions import db

class Comparison(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url1_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
    url2_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    url1 = db.relationship('Url', foreign_keys=[url1_id])
    url2 = db.relationship('Url', foreign_keys=[url2_id])

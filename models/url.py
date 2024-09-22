from extensions import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    speed_index = db.Column(db.Float, nullable=False)
    time_to_interactive = db.Column(db.Float, nullable=False)

    def display_speed_index(self):
        return f"{self.speed_index} seg."

    def display_time_to_interactive(self):
        return f"{self.time_to_interactive} seg."


from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


# Models go below
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    image_url = db.Column(
        db.String, default="https://wallpapercave.com/wp/wp12696574.jpg"
    )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name = property(get_full_name)

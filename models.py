from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String

db = SQLAlchemy()


def connect_db(app):
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String, nullable=False)
    last_name = mapped_column(String, nullable=False)
    image_url = mapped_column(
        String, default="https://wallpapercave.com/wp/wp12696574.jpg"
    )

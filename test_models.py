from unittest import TestCase
from app import app
from models import db, User


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly_test"
app.config["SQlALCHEMY_ECHO"] = False

db.drop_all()
db.create_all()


class Blogly_test(TestCase):
    def setUp(self):
        with app.app_context():
            User.query.delete()

    def tearDown(self):
        with app.app_context():
            db.session.rollback()

    def test_full_name(self):
        with app.app_context():
            user = User(first_name="John", last_name="Wick")
            self.assertEqual(user.full_name, "John Wick")

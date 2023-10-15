from unittest import TestCase

from app import app
from models import User, db

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly_test"
app.config["SQLALCHEMY_ECHO"] = False
app.config["TESTING"] = True

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    def setUp(self):
        User.query.delete()
        user = User(first_name="John", last_name="Doe")
        db.session.add(user)
        db.session.commit()
        self.user_id = user.id
        self.user = user

    def tearDown(self):
        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            res = client.get("/users")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("John", html)

    def test_profile_user(self):
        with app.test_client() as client:
            res = client.get(f"/users/{self.user_id}")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("John Doe", html)

    def test_new_user(self):
        with app.test_client() as client:
            data = {"first_name": "Bob", "last_name": "Doe", "image_url": ""}
            res = client.post(
                "/users/new",
                data=data,
                follow_redirects=True,
            )
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("Bob", html)

    def test_edit_user(self):
        with app.test_client() as client:
            self.assertEqual(self.user.first_name, "John")
            data = {
                "first_name": "Zork",
                "last_name": "Doe",
                "image_url": self.user.image_url,
            }
            res = client.post(
                f"/users/{self.user_id}/edit", data=data, follow_redirects=True
            )
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("Zork Doe", html)

    def test_delete_user(self):
        with app.test_client() as client:
            res = client.get(f"/users/{self.user_id}/delete", follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertNotIn("John", html)

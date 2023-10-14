from flask import Flask, redirect, render_template, request
from models import db, connect_db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


@app.route("/")
def home():
    users = db.session.execute(db.select(User)).scalars()
    return render_template("home.html", users=users)


@app.route("/add-user")
def add_user():
    return render_template("add_user.html")


@app.route("/create-user", methods=["POST"])
def create_user():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    image_url = request.form.get("image_url")
    image_url = image_url if image_url else None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")


@app.route("/profile/<user_id>")
def profile_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar_one()
    return render_template("profile.html", user=user)


@app.route("/delete/<user_id>")
def delete_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar_one()
    db.session.delete(user)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

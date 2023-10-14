from flask import Flask, redirect, render_template, request
from models import db, connect_db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


@app.route("/")
def home():
    return redirect("/users")


@app.route("/users")
def users():
    users = db.session.execute(
        db.select(User).order_by(User.last_name, User.first_name)
    ).scalars()
    return render_template("home.html", users=users)


@app.route("/users/new", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        user = User(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            image_url=request.form["image_url"],
        )
        user.image_url = user.image_url if user.image_url else None

        db.session.add(user)
        db.session.commit()
        return redirect("/users")

    return render_template("add_user.html")


@app.route("/users/<id>")
def profile_user(id):
    user = db.session.execute(db.select(User).where(User.id == id)).scalar()
    return render_template("profile.html", user=user)


@app.route("/users/<id>/delete")
def delete_user(id):
    user = db.session.execute(db.select(User).where(User.id == id)).scalar()
    db.session.delete(user)
    db.session.commit()
    return redirect("/")


@app.route("/users/<id>/edit", methods=["GET", "POST"])
def edit_profile(id):
    user = db.session.execute(db.select(User).where(User.id == id)).scalar()
    if request.method == "POST":
        user.first_name = request.form.get("first_name")
        user.last_name = request.form.get("last_name")
        user.image_url = request.form.get("image_url")
        user.image_url = user.image_url if user.image_url else None

        db.session.add(user)
        db.session.commit()
        return redirect(f"/users/{user.id}")
    return render_template("edit.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)

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
    user = User(
        first_name=request.form["first_name"],
        last_name=request.form["last_name"],
        image_url=request.form["image_url"],
    )
    user.image_url = user.image_url if user.image_url else None

    db.session.add(user)
    db.session.commit()
    return redirect("/")


@app.route("/profile/<id>")
def profile_user(id):
    user = db.session.execute(db.select(User).where(User.id == id)).scalar()
    return render_template("profile.html", user=user)


@app.route("/delete/<id>")
def delete_user(id):
    user = db.session.execute(db.select(User).where(User.id == id)).scalar()
    db.session.delete(user)
    db.session.commit()
    return redirect("/")


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_profile(id):
    user = db.session.execute(db.select(User).where(User.id == id)).scalar()
    if request.method == "POST":
        user.first_name = request.form.get("first_name")
        user.last_name = request.form.get("last_name")
        user.image_url = request.form.get("image_url")
        user.image_url = user.image_url if user.image_url else None

        db.session.add(user)
        db.session.commit()
        return redirect(f"/profile/{user.id}")
    return render_template("edit.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)

from models import User, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [
        User(
            first_name="John",
            last_name="Wick",
            image_url="https://avatarfiles.alphacoders.com/336/336452.jpg",
        ),
        User(
            first_name="Mace",
            last_name="Windu",
            image_url="https://comicvine.gamespot.com/a/uploads/scale_medium/11122/111226069/4817468-6565664823-tumbl.jpg",
        ),
        User(
            first_name="Anakin",
            last_name="Skywalker",
            image_url="https://i.redd.it/vwm1lqdtymj91.jpg",
        ),
        User(
            first_name="John",
            last_name="Nolan",
            image_url="https://tv-fanatic-res.cloudinary.com/iu/s--faBe1hrA--/t_full/cs_srgb,f_auto,fl_strip_profile.lossy,q_auto:420/v1679686940/john-nolan-the-rookie-s5e19.png",
        ),
        User(
            first_name="Naruto",
            last_name="Uzumaki",
            image_url="https://comicvine.gamespot.com/a/uploads/scale_medium/11117/111178336/5603895-dcc2d502-6c35-49c9-c93c-6eae7f44d551.jpg",
        ),
        User(
            first_name="Hera",
            last_name="Syndulla",
            image_url="https://upload.wikimedia.org/wikipedia/en/e/e3/Hera_Syndulla_Ahsoka.jpg",
        ),
        User(
            first_name="Bo-Katan",
            last_name="Kryze",
            image_url="https://i.redd.it/0d2d1q6qm0k61.jpg",
        ),
        User(
            first_name="Ahsoka",
            last_name="Tano",
            image_url="https://i.redd.it/4spfxs2x0ie61.jpg",
        ),
        User(first_name="Ghost", last_name="Unknown"),
    ]

    db.session.add_all(users)
    db.session.commit()

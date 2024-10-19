from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@localhost/test"

db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(50))

with app.app_context():
    db.create_all()

@app.route('/', methods=["GET"])
def test_back():
    user = db.session.execute(db.select(User).order_by(User.username)).scalar_one()
    user_dump = {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }
    return {"msg": user_dump}

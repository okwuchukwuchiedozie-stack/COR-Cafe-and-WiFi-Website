from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Boolean
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///cafes.db")
db = SQLAlchemy(model_class=Base)
db.init_app(app)


@app.context_processor
def inject_current_year():
    from datetime import datetime

    return {
        "current_year": datetime.now().year
    }


class Cafe(db.Model):

    __tablename__ = "cafe"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str | None] = mapped_column(String(250))
    coffee_price: Mapped[str | None] = mapped_column(String(250))


class CafeForm(FlaskForm):

    cafe = StringField("Cafe Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[DataRequired()])
    cafe_map_url = StringField("Cafe Map URL", validators=[DataRequired(), URL()])
    cafe_img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    has_sockets = BooleanField("Sockets")
    has_toilet = BooleanField("Toilet")
    has_wifi = BooleanField("WiFi")
    can_take_calls = BooleanField("Can take calls")
    seats = StringField("Number of Seats", validators=[DataRequired()])
    submit = SubmitField("Add Cafe")


@app.route("/")
def home():

    cafes = db.session.execute(db.select(Cafe)).scalars().all()

    return render_template("index.html", cafes=cafes)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():

    form = CafeForm()

    if form.validate_on_submit():

        new_cafe = Cafe(
            name=form.cafe.data,
            map_url=form.cafe_map_url.data,
            img_url=form.cafe_img_url.data,
            location=form.location.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            can_take_calls=form.can_take_calls.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )

        db.session.add(new_cafe)
        db.session.commit()

        flash(
            f"{form.cafe.data} was added successfully!",
            "success"
        )

        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):

    cafe = db.get_or_404(Cafe, cafe_id)
    cafe_name = cafe.name

    db.session.delete(cafe)
    db.session.commit()

    flash(
        f"{cafe_name} was deleted successfully!",
        "success"
    )

    return redirect(url_for("home"))




if __name__ == "__main__":
    app.run(debug=False)
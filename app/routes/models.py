from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin

class Recipe(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), unique=True)
    image = db.Column(db.String(250))
    title = db.Column(db.String(50), nullable=False)
    category = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text())
    instructions = db.Column(db.Text(), nullable=False)

    # foreign key
    chef_id = db.Column(db.Integer, db.ForeignKey('chef.id'), nullable=False)


class Chef(db.Model, CRUDMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String(250))
    description = db.Column(db.Text())


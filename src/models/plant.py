from src.ext import db
from src.models.base import BaseModel

class Plant(BaseModel, db.Model):
    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    eng_name = db.Column(db.String(255), unique=True, nullable=False)
    family_name = db.Column(db.String(255), unique=True, nullable=False)
    family_name_geo = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(255), unique=True, nullable=False)
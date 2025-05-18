from src.ext import db
from src.models.base import BaseModel

class Question(BaseModel, db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    pair_number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    next_pair_number = db.Column(db.Integer)

    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=True)
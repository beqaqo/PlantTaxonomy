from src.ext import db

class BaseModel:
    def create(self, commit=True):
        db.session.add(self)
        if commit:
            self.save()

    def delete(self):
        db.session.delete(self)
        self.save()

    @staticmethod
    def save():
        db.session.commit
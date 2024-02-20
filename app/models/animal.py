from ..utils.database import db

class Animal(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=True)
   gender = db.Column(db.String(100), nullable=False)
   age = db.Column(db.Integer, nullable=False)
   diet = db.Column(db.String(100), nullable=False)

   def as_dict(self):
         return {
                  "id": self.id,
                  "name": self.name,
                  "gender": self.gender,
                  "age": self.age,
                  "diet": self.diet
               }

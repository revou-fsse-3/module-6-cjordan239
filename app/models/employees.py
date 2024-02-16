from ..utils.database import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    shift = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "gender": self.gender,
            "birthday": str(self.birthday),
            "shift": self.shift
        }

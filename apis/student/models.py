from exts import db


class Teacher(db.Model):
    __tablename__ = "teacher"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)

    def __repr__(self):
        return '<Teacher %r>' % self.name


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    sex = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    teacher_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Student %r>' % self.name

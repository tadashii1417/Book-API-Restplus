from base_task.models import db

class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    authorId = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    view = db.Column(db.Integer, nullable=False)
    vote = db.Column(db.Integer, nullable=False)
    download = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return "Book: " + self.title


class Authors(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return "Author: " + self.firstName

db.create_all()
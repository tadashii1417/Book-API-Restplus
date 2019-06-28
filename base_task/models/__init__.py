# coding=utf-8
import logging
from datetime import datetime
import flask_bcrypt as _fb
import flask_migrate as _fm
import flask_sqlalchemy as _fs

__author__ = 'Truong'
_logger = logging.getLogger('api')

db = _fs.SQLAlchemy()
migrate = _fm.Migrate(db=db)
bcrypt = _fb.Bcrypt()


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(50), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)

    authorId = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    author = db.relationship('Authors', backref=db.backref('books'))

    status = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    view = db.Column(db.Integer, default=0)
    vote = db.Column(db.Integer, default=0)
    download = db.Column(db.Integer, default=0)

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
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    bookcount = db.Column(db.Integer, default=0)

    def __repr__(self) -> str:
        return "Author: " + self.firstName


def init_app(app, **kwargs):
    """
    Extension initialization point
    :param flask.Flask app:
    :param kwargs:
    :return:
    """
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate.init_app(app)
    _logger.info('Start app in {env} environment with database: {db}'.format(
        env=app.config['ENV_MODE'],
        db=app.config['SQLALCHEMY_DATABASE_URI']
    ))


from .base import TimestampMixin

# Import all necessary models here

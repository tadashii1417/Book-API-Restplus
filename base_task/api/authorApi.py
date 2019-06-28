from flask_restplus import Namespace, Resource, fields
from ..models import *
from .util import valiateAuthorPayload

author = Namespace('authors', description="Authors related operations.")

authorModel = author.model('Author', {
    'id': fields.Integer(description="Author identifier", example=1),
    'firstName': fields.String(description="Author first name", example="truong", min_length=3),
    'lastName': fields.String(description="Author last name", example="duong", min_length=3),
    'email': fields.String(description="Author email", example="truong@gmail.com", required=True),
    'phone': fields.String(description="Author phone number", example="95454", required=True),
    'address': fields.String(description="Author address", example="Ha tinh", min_length=10),
    'status': fields.String(description="Author status ", example="active"),
    'created': fields.DateTime(description="Author created date", example="2015-5-10T10:55:43"),
    'updated': fields.DateTime(description="Author updated date", example="2015-5-10T10:55:43"),
})


@author.route('/')
class AuthorApi(Resource):

    # @author.marshal_list_with(authorModel)
    def get(self):
        '''Author api to get all authors.'''
        # return Authors.query.all()
        res = []
        for author in Authors.query.all():
            bestBook = db.session.query(Books).filter(Books.authorId == author.id).order_by(Books.vote.desc()).first()
            temp = {
                "id": author.id,
                "firstName": author.firstName,
                "lastName": author.lastName,
                "email": author.email,
                "phone": author.phone,
                "address": author.address,
                "book-count": len(author.books),
                "bestBook-isbn": bestBook.isbn if bestBook else "",
                "bestBook-title": bestBook.title if bestBook else ""
            }
            res.append(temp)

        return res

    @author.expect(authorModel)
    @author.response(400, "Input not valid")
    def post(self):
        '''Author api to create new authors.'''
        valiateAuthorPayload(author.payload, author)

        newAuthor = Authors(
            firstName=author.payload['firstName'],
            lastName=author.payload['lastName'],
            email=author.payload['email'],
            phone=author.payload['phone'],
            address=author.payload['address'],
            status=author.payload['status'],
            created=author.payload['created'],
        )
        db.session.add(newAuthor)
        db.session.commit()
        return author.payload

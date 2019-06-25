from flask_restplus import Namespace, Resource, fields

book = Namespace('books', description="Books related operations.")

bookModel = book.model('Book', {
    'id': fields.Integer(description="Book identifier"),
    'title': fields.String(description="Book title"),
    'isbn': fields.String(description="Book ISBN"),
    'year': fields.Integer(description="Year of the book"),
    'authorId': fields.Integer(description="Identifier of the book author"),
    'status': fields.String(),
    'created': fields.DateTime(),
    'updated': fields.DateTime(),
    'view': fields.Integer(),
    'vote': fields.Integer(),
    'download': fields.Integer()
})


@book.route('/get')
class BookApi(Resource):
    '''Book api to get all books.'''

    def get(self):
        return {"hi": "truong"}
from flask_restplus import Namespace, Resource, fields
from ..models import *
book = Namespace('books', description="Books related operations.")

bookModel = book.model('Book', {
    'id': fields.Integer(description="Book identifier", example="22"),
    'title': fields.String(description="Book title", example="Book title sample"),
    'isbn': fields.String(description="Book ISBN", example="ABS23"),
    'year': fields.Integer(description="Year of the book", example="1996"),
    'authorId': fields.Integer(description="Identifier of the book author", example="10"),
    'status': fields.String(description="Book status", example="còn"),
    'created': fields.DateTime(description="Book created date", example="2015-5-10T10:55:43"),
    'updated': fields.DateTime(description="Book lasted update", example="2015-5-10T10:56:43"),
    'view': fields.Integer(description="Number of view", example="22"),
    'vote': fields.Integer(description="Number of vote", example="2"),
    'download': fields.Integer(description="Number of download times.", example="10")
})


# create read update delete searchbook(isbn) or likely by title

@book.route('/get')
class BookApiList(Resource):
    @book.marshal_list_with(bookModel)
    def get(self):
        '''Book api to get all books.'''
        return Books.query.all()


    def post(self):
        '''Book api create new book.'''
        return {"hi": "truong"}


@book.route('/<int:id>')
@book.response(404, "ID not found")
@book.param('id', 'The book identifier')
class BookApi(Resource):

    def get(self, id):
        '''Book api to get a specific book by its id.'''
        return {"hi": "truong"}


    def delete(self, id):
        '''Book api to delete a books.'''
        return {"hi": "truong"}


    def put(self, id):
        '''Book api to update given book identifier'''
        return {"hi": "truong"}

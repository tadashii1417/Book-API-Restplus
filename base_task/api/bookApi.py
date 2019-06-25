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


# create read update delete searchbook(isbn) or likely by title

@book.route('/get')
class BookApiList(Resource):
    '''Book api to get all books.'''

    def get(self):
        return {"hi": "truong"}

    '''Book api create new book.'''

    def post(self):
        return {"hi": "truong"}


@book.route('/<int:id>')
@book.response(404, "ID not found")
@book.param('id', 'The book identifier')
class BookApi(Resource):
    '''Book api to get a specific book by its id.'''

    def get(self, id):
        return {"hi": "truong"}

    '''Book api to delete a books.'''

    def delete(self, id):
        return {"hi": "truong"}

    '''Book api to update given book identifier'''

    def put(self, id):
        return {"hi": "truong"}

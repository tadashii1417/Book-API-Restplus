from flask_restplus import Namespace, Resource, fields, inputs
from ..models import *
from .util import valiateBookPayload

book = Namespace('books', description="Books related operations.")

bookModel = book.model('Book', {
    'id': fields.Integer(description="Book identifier", example=22),
    'title': fields.String(description="Book title", example="Book title sample", require=True, min_length=5),
    'isbn': fields.String(description="Book ISBN", example="ABS23", require=True, min_length=10),
    'year': fields.Integer(description="Year of the book", example=1996, require=True),
    'authorId': fields.Integer(description="Identifier of the book author", example=10, require=True),
    'status': fields.String(description="Book status", example="new"),
    'created': fields.DateTime(description="Book created date", example="2015-5-10T10:55:43"),
    'updated': fields.DateTime(description="Book lasted update", example="2015-5-10T10:56:43"),
    'view': fields.Integer(description="Number of view", example=22, default=0),
    'vote': fields.Integer(description="Number of vote", example=2, default=0),
    'download': fields.Integer(description="Number of download times.", example=10, default=0)
})


@book.route('/')
@book.response(201, "Book created.")
class BookApiList(Resource):
    @book.doc('Book_lists')
    @book.marshal_list_with(bookModel)
    def get(self):
        '''Book api to get all books.'''
        return Books.query.all()

    @book.doc('Insert_book')
    @book.expect(bookModel, validate=True)
    @book.response(400, "Invalid input")
    def post(self):
        '''Book api create new book.'''
        valiateBookPayload(book.payload, book)
        newBook = Books(
            title=book.payload['title'],
            isbn=book.payload['isbn'],
            year=book.payload['year'],
            authorId=book.payload['authorId'],
            status=book.payload['status'],
            created=book.payload['created'],
            updated=book.payload['updated'],
        )
        db.session.add(newBook)
        updateAuthor = Authors.query.filter_by(id=1).first()
        updateAuthor.bookcount += 1
        db.session.commit()
        return book.payload, 201


@book.route('/<int:id>')
@book.response(404, "ID not found")
@book.param('id', 'The book identifier')
class BookApi(Resource):

    @book.marshal_with(bookModel)
    def get(self, id):
        '''Book api to get a specific book by its id.'''
        getBook = db.session.query(Books).filter(Books.id == id).first()
        if not getBook:
            book.abort(404, "ID not found")
        return getBook

    @book.response(204, "Book deleted")
    def delete(self, id):
        '''Book api to delete a specific book.'''
        delBook = db.session.query(Books).filter(Books.id == id).first()
        if not delBook:
            book.abort(404, "ID not found")

        updateAuthor = Authors.query.filter_by(id=delBook.authorId).first()
        updateAuthor.bookcount -= 1
        db.session.delete(delBook)
        db.session.commit()
        return "Book deleted", 204

    @book.expect(bookModel)
    @book.marshal_with(bookModel)
    def put(self, id):
        '''Book api to update given book identifier'''
        updateBook = db.session.query(Books).filter(Books.id == id).first()
        if not updateBook:
            book.abort(404, "ID not found")

        valiateBookPayload(book.payload, book)

        updateBook.title = book.payload['title']
        updateBook.isbn = book.payload['isbn']
        updateBook.year = book.payload['year']
        updateBook.authorId = book.payload['authorId']
        updateBook.status = book.payload['status']
        updateBook.created = book.payload['created']
        updateBook.updated = book.payload['updated']
        db.session.commit()
        return updateBook


@book.route('/isbn/<isbn>')
@book.response(404, "ISBN not found")
@book.param('isbn', "International Standard Book Number.")
class BookISBN(Resource):

    @book.marshal_with(bookModel)
    def get(self, isbn):
        '''Book api to get a specific book by its isbn.'''
        if not db.session.query(Books).filter(Books.isbn == isbn).first():
            book.abort(404, "ISBN not found")
        return db.session.query(Books).filter(Books.isbn == isbn).first()


@book.route('/title/<search>')
@book.param('search', "Title string to search")
class BookISBN(Resource):

    @book.marshal_list_with(bookModel)
    def get(self, search):
        '''Book api to seach list of books by its title.'''
        res = []
        for x in search.split():
            res += db.session.query(Books).filter(Books.title.like("%" + x + "%")).all()
        return res

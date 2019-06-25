from flask_restplus import Namespace, Resource, fields

author = Namespace('authors', description="Authors related operations.")

authorModel = author.model('Author', {
    'ID': fields.Integer(description="Book identifier"),
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


@author.route('/get')
class AuthorApi(Resource):
    '''Author api to get all authors.'''

    def get(self):
        return {"hi": "truong author"}
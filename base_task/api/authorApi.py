from flask_restplus import Namespace, Resource, fields

author = Namespace('authors', description="Authors related operations.")

authorModel = author.model('Author', {
    'id': fields.Integer(description="Author identifier"),
    'firstName': fields.String(description="Author first name"),
    'lastName': fields.String(description="Author last name"),
    'email': fields.String(description="Author email"),
    'phone': fields.String(description="Author phone number"),
    'address': fields.String(),
    'status': fields.String(),
    'created': fields.DateTime(),
    'updated': fields.DateTime(),
})


@author.route('/get')
class AuthorApi(Resource):
    '''Author api to get all authors.'''

    def get(self):
        return {"hi": "truong author"}
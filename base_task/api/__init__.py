# coding=utf-8
import logging

from flask import Blueprint
from flask_restplus import Api

# Import all necesary API NameSpace here
from .bookApi import book
from .authorApi import author

__author__ = 'Truong'
_logger = logging.getLogger('api')

api_wms = Blueprint('api', __name__, url_prefix='/api')

custom_definition = {
    'info': {
        'x-logo': {
            'url': 'https://teko-vn.github.io/api-docs/Teko-Logo-01.svg'
        }
    },
}

api = Api(
    app=api_wms,
    version='1.0',
    title='Teko WMS API Specification',
    validate=False,
    description='This documentation describes APIs used in/exposed from Teko micro-services ecosystem \
    # Introduction\
    These specifications are following\
    [OpenAPI 3.0.0 format](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md).',
    license='Apache 2.0',
    license_url='http://www.apache.org/licenses/LICENSE-2.0.html',
    contact_email='son.lp@teko.vn'
    # doc='' # disable Swagger UI
)

# add custom definition
api.add_namespace(book)
api.add_namespace(author)


def init_app(app, **kwargs):
    """
    :param flask.Flask app: the app
    :param kwargs:
    :return:
    """
    # Add all necesary namespace here
    # api.add_namespace(user_ns)

    app.register_blueprint(api_wms)

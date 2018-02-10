import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug import Request, url_decode

############################
# class MethodRewriteMiddleware(object):
#
#     def __init__(self, app):
#         self.app = app
#
#     def __call__(self, environ, start_response):
#         if 'METHOD_OVERRIDE' in environ.get('QUERY_STRING', ''):
#             args = url_decode(environ['QUERY_STRING'])
#             method = args.get('__METHOD_OVERRIDE__')
#             if method:
#                 method = method.encode('ascii', 'replace')
#                 environ['REQUEST_METHOD'] = method
#         return self.app(environ, start_response)
##########################

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mydatabase.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views

import json
from flask import Flask, request, jsonify, session, Blueprint
from config.database import db
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jti
)
import bcrypt
import time
from logzero import logger
import traceback

# app = Flask(__name__)
get_started = Blueprint('get_started', __name__)


def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


@get_started.route("/register", methods=["GET", 'POST'])
def signup():
    defaultValue = ''
    firstName = request.form.get('first_name',    defaultValue)
    lastName = request.form.get('last_name', defaultValue)
    phoneNumber = request.form.get('phone_number', defaultValue)
    username = request.form.get('username', defaultValue)
    email = request.form.get('email', defaultValue)
    password = request.form.get('password', defaultValue)
    location = request.form.get('location', defaultValue)

    # validation
    # make a loop that che

    # These are timestamps thus they sould not be included as form fields...
    # created_at = request.form.get('created_at', defaultValue)
    # updated_at = request.form.get('updataed_at', defaultValue)


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=5000)
# @get_started.route('/')
# @get_started.route('/register', methods =['GET', 'POST'])
# def register():
#     data = request.get_json()
#     if request.get_json() == 'POST':
#         first_name = [StringField('first_name')]
#         last_name = [StringField('last_name')]
#         phone_number = [StringField('phone_number')]
#         username = [StringField('username')]
#         email = [StringField('email')]
#         password = ['password']
#         location = [StringField('location')]
#         img = ['img']
#         created_at = [StringField('created_at')]
#         updated_at = [StringField('updated_at')]
#         cur = db.cursor(db.cursors.DictCursor)
#         db.execute('SELECT * FROM main.users WHERE users.username =%s AND password = %s', (username, password))
#         user = cur.fetchone()
#
#         error = {}
#
#         if user:
#             error['user'] = 'already exists'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             error['email'] = 'invalid email address'
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             error['username'] = 'invalid username'
#         elif not username or not password or not email:
#             error['user'] = 'fill the form'
#         else:
#             cur = conn.cursor()
#             cur.execute("INSERT INTO main.users VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",)
#
#             db.commit()
#             token = jwt.encode({'user': data})
#             error = jwt.encode({'user': error})
#         return jsonify({'token': token})
#         # return jsonify({"username": username, "message": f"user {username} created."}), 201
#     return jsonify({'error': error})

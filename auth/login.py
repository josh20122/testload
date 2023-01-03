from flask import Flask, request, jsonify, session, Blueprint, make_response
from config.database import *
import jwt
import datetime
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jti
)
import bcrypt
import time
from logzero import logger
import traceback

sign_in = Blueprint('sign_in', __name__)


@sign_in.route('/')
@sign_in.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400
    username = request.json_get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"message": "Wrong username or password"}), 400

    con = db.cursor(db)
    cur = con.cursor()
    cur.execute('SELECT * FROM main.users WHERE users.username =%s AND password = %s', (user_name, password))
    users = cur.fetchone()
    try:
        user = db[username]
        logger.debug(f'username={username}')
        if not user:
            return jsonify({"message": "Bad username or password"}), 401

        logger.debug(f'{user}')
        if bcrypt.checkpw(password.encode(), user["password"].encode()):
            logger.debug(f'{user["username"]}')
            db.execute('UPDATE main.users SET password = %s WHERE username = %s', (password, user["username"]))
            db.commit()
            logger.debug(f'{user["username"]}')
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return jsonify({"message": "Bad username or password"}), 401
    except Exception as e:
        logger.error(traceback.format_exc())
        return jsonify({"message": "An error occurred"}), 500

    access_token = create_access_token(identity=user["user_id"])
    db.execute('UPDATE main.users SET password = %s WHERE username = %s', (password, user["username"]))
    db.commit()
    get_jti(access_token), username
    return jsonify(access_token=access_token), 200

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token')
#         if not token:
#             return jsonify({'message': 'Token is missing'}), 403
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'])
#         except:
#             return jsonify({'message': 'Token is invalid'}), 403
#         return f(*args, **kwargs)
#
#     return decorated


# @sign_in.route('/')
# @sign_in.route('/login', methods=['POST', 'GET'])
# def login():
#     auth = request.form.get('username')
#     login_error = {}
#     if auth == 'POST' and 'user_name' in request.form and 'password' in request.form:
#         username = request.form[StringField('username')]
#         password = request.form[StringField('password')]
#         cur = db.connection.cursor(db.cursors.DictCursor)
#         db.execute('SELECT * FROM main.users WHERE users.username =%s AND password = %s', (user_name, password))
#         users = cur.fetchone()
#         if users:
#             session['loggedin'] = True
#             session['id'] = users['id']
#             session['user_name'] = users['user_name']
#         else:
#             login_error['user'] = 'incorrect username/password'
#             return jsonify({'login_error': login_error}), 401
#         auth = jwt.encode({'user': auth, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')
#     return jsonify({'token': auth})


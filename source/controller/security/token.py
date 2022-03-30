from flask import request, jsonify
from functools import wraps
from source.model.dbModel import User

import os
import jwt
import datetime as dt

# By Thatchawin Leelawat
# verifying the JWT
def jwt_Token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is not found'}), 401
        try:
            res = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), "HS256")
        except:
            return jsonify({
                'message' : 'Token is invalid/ expired'
            }), 401

        return  f(res, *args, **kwargs)
  
    return decorated

# generated token containing user data like 
def genJWT(public_id, secret_key = os.getenv('JWT_SECRET_KEY')):    
    token = jwt.encode({'public_id' : public_id, 'exp' : dt.datetime.utcnow() + dt.timedelta(minutes=180)}, secret_key, "HS256")
    return token

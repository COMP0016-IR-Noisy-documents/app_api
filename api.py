from flask import request

from source.controller.authentication.token import jwt_Token
from source.controller.controller import Controller, app

from flask_cors import CORS

app.config.from_object('config.DevelopmentConfig')
CORS(app)

controller = Controller()

#for debugging only
@app.route("/callback", methods=["GET"], strict_slashes=False)
def callback():

    return request.args, 200 

#search API 
@app.route("/search", methods=["POST"], strict_slashes=False)
def search():
    
    return controller.search()

#register new user
@app.route("/register", methods=["POST"], strict_slashes=False)
def register():
    return controller.register()
    

#login route
@app.route("/login", methods=["POST"], strict_slashes=False)
def login():
    return controller.login()
    

#get current user details
@app.route("/current-user-detail", methods=['GET'])
@jwt_Token
def userDetail(token):
    return controller.userDetail()

#get current user details
@app.route("/search-history", methods=['POST'])
def searchHistory():
    return controller.collectHistory()

#get current user details
@app.route("/click-history", methods=['POST'])
def clickHistory():
    return controller.clickHistory()

if __name__ == '__main__':
    app.run()
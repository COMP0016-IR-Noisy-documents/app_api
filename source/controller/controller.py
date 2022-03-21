from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


from source.model.dbModel import db, User, SearchHistory, ClickHistory
from source.model.searchModel import searchModel

from source.controller.security.password import EncPassword
from source.controller.security.token import genJWT
from source.controller.modifyFormat import modifyFilter

import datetime
import json
import jwt
import os

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Controller:
    def __init__(self) -> None:
        
        self.__searchmodel = searchModel()
    
    #search for a related document
    def search(self):
        body = request.json    
        title = body.get('query')
        filter = body.get('filter')

        searchFilter = modifyFilter(filter)
        
        if title is None:
            title = ''
        
        try:      
            result = self.__searchmodel.search(title, searchFilter)
            ''' 
            reformat from "{"id1": {obj1}, "id2": {obj2}}" to {"result": [{obj1}, {obj2}]}
            '''

            resDict = result.to_dict(orient='index')

            resList = []
            for key in resDict.keys():
                resList.append(resDict[key])
            resJSON = {"result": resList}
            return resJSON, 200
        except:
            return "some error occur in the server", 500

    #register user to db
    def register(self):
        body = request.json
    
        Username = body.get('username')
        Password = body.get('password')
        Email = body.get('email')
        DisplayName = body.get('displayname')

        if User.query.filter_by(Username=Username).first() != None:
            return ('this username has already been used', 401)

        if User.query.filter_by(Email=Email).first() != None:
            return ('this email has already been used', 401)

        db.session.add(User(Username, Password, Email, DisplayName))
        db.session.commit()

        return ('user has been registered', 200)

    #login user
    def login(self):

        body = request.json
    
        Username = body.get('username')
        Password = body.get('password')

        try:
            user = User.query.filter_by(Username=Username).first()
            if user.Username == Username:
                salt = user.Salt
                hashed_password = EncPassword(Password, salt)
                if user.Password == hashed_password.getPassword():
                    token =  genJWT(user.PublicID)
                    user = User.query.filter_by(Username=Username).first()

                    return jsonify({'token' : token}), 200
                return 'wrong password', 401
        except:
            return 'wrong username', 401

    #get user detail
    def userDetail(self):
        token = request.headers['x-access-token']
        data = jwt.decode(token, app.config['SECRET_KEY'], "HS256")
        print(data)
        user = User.query.filter_by(PublicID = data['public_id']).first()


        user_json = jsonify({
            'public_id': data['public_id'],
            'username': user.Username,
            'email': user.Email,
            'displayname': user.DisplayName
        })
        return user_json, 200

    #DEMO
    #get user detail
    def collectHistory(self):
        body = request.json

        Query = body.get('query')
        Filter = body.get('filter')
        #top_20 url
        TopDocumentID = body.get('top_document_id')
        PublicID = body.get('public_id')

        print(PublicID)

        try:
            user = User.query.filter_by(PublicID = PublicID).first()
            FK_UserID = user.UserID
        except:
            print('user is not login/ cannot get user id')
            FK_UserID = None
 
        db.session.add(SearchHistory(Query, json.dumps(Filter), TopDocumentID, FK_UserID))
        db.session.commit()
        searchhistory = SearchHistory.query.order_by(SearchHistory.SearchID.desc()).filter_by(Query = Query).first()
        SearchID = searchhistory.SearchID
        return {"search_id": SearchID}, 200

    #DEMO
    #get click history
    def clickHistory(self):
        body = request.json

        DocumentID = body.get('document_id')
        DocumentPos = body.get('document_pos')
        FK_SearchID = body.get('search_id')
        PublicID = body.get('public_id')

        try:
            user = User.query.filter_by(PublicID = PublicID).first()
            FK_UserID = user.UserID
        except:
            print('user is not login/ cannot get user id')
            FK_UserID = None

 
        db.session.add(ClickHistory(DocumentID, DocumentPos, FK_SearchID, FK_UserID))
        db.session.commit()

        return 'data has been collected to the db'

# test code
if __name__ == "__main__":
    C = Controller()
    sr = C.search("Italy")
    for result in sr.iterrows():
        print(result)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

from source.controller.authentication.password import EncPassword

import uuid
from datetime import datetime, timezone

db = SQLAlchemy()

# Initialise the database collecting user detail
class User(db.Model):
    __tablename__ = 'user'
    UserID = db.Column(db.Integer, primary_key=True)
    PublicID = db.Column(db.String(50), unique = True)
    Username = db.Column(db.String(200), unique = True)
    Password = db.Column(db.String(200))
    Salt = db.Column(db.String(200))
    Email = db.Column(db.String(200), unique = True)
    DisplayName = db.Column(db.String(200))

    def __init__(self, Username: str, Password: str, Email: str, DisplayName: str, Salt: str=None):
        self.Username = Username
        self.PublicID = str(uuid.uuid4())
        self.Email = Email
        self.DisplayName = DisplayName
        if (Salt == None):
            pwd = EncPassword(Password)
            self.Salt = pwd.getSalt()
        else:
            pwd = EncPassword(Password, Salt)
            self.Salt = Salt
        self.Password = pwd.getPassword()

# Initialise the database collecting user detail
class SearchHistory(db.Model):
    __tablename__ = 'search_history'
    SearchID = db.Column(db.Integer, primary_key=True)
    Query = db.Column(db.String(50), unique = True)
    Filter = db.Column(db.String(200), unique = True)
    Timestamp = db.Column(db.TIMESTAMP)
    TopDocumentID = db.Column(db.String(200))
    FK_UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))

    def __init__(self, Query: str, Filter: str, TopDocumentID: str=None, FK_UserID: str=None):
        self.Query = Query
        self.Filter = Filter
        self.Timestamp = datetime.now().astimezone()
        self.TopDocumentID = TopDocumentID
        self.FK_UserID = FK_UserID              

# Initialise the database collecting user detail
class ClickHistory(db.Model):
    __tablename__ = 'click_history'
    ClickID = db.Column(db.Integer, primary_key=True)
    DocumentID = db.Column(db.Integer)
    Timestamp = db.Column(db.TIMESTAMP)
    DocumentPos = db.Column(db.Integer)
    FK_SearchID = db.Column(db.Integer, db.ForeignKey('search_history.SearchID'))
    FK_UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))

    def __init__(self, DocumentID: int, DocumentPos: int, FK_SearchID: str=None, FK_UserID: str=None):
        self.DocumentID = DocumentID
        self.Timestamp = datetime.now().astimezone()
        self.DocumentPos = DocumentPos  
        self.FK_SearchID = FK_SearchID
        self.FK_UserID = FK_UserID   
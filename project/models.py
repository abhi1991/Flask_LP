# project/models.py


import datetime

from project import db, bcrypt

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return 'user email is {0}'.format(self.email)


class UserData(db.Model):

    __tablename__ = 'userdata'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String,unique = False,nullable = False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String,unique = False, nullable = False)
    email_added_on = db.Column(db.DateTime, nullable=False)

    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.email_added_on = datetime.datetime.now()
        
     
        
        
        
        

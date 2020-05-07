from flask import Flask
import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()

db = SQLAlchemy()

class DBClass(db.Model):
    __tablename__ = 'sys_users'
    UserID = db.Column(db.Integer, primary_key = True)
    FirstName = db.Column(db.String(200), unique=True)
    LastName = db.Column(db.String(200), unique=True)
    UserName = db.Column(db.String(200), unique=True, nullable=False)
    UserPassword = db.Column(db.String(100), unique=True, nullable=False)
    UserEmail = db.Column(db.String(100), unique=True)
    Role_ID = db.Column(db.Integer, db.ForeignKey('role_table.Role_ID'), nullable=False)
    #Active = db.Column(db.Boolean, unique=False)
    #DateCreated = db.Column(db.DateTime, db.DateTime, default=datetime.datetime.utcnow(), unique=True)
    
        
class DBClass2(db.Model):
    __tablename__ = 'role_table'
    Role_ID = db.Column(db.Integer, primary_key = True)
    RoleName = db.Column(db.String(200), unique=True)
    RoleActive = db.Column(db.Boolean, unique=False)
    users_vw = db.relationship('DBClass', backref='role_table', uselist=False)
    #Active = db.Column(db.Boolean, unique=False)
    #DateCreated = db.Column(db.DateTime, db.DateTime, default=datetime.datetime.utcnow(), unique=True)
    
        
class DBClass3(db.Model):
    __tablename__ = 'staff_table'
    staff_ID = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(200), unique=True)
    lastname = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    datejoined = db.Column(db.Date)
    desgnation = db.Column(db.String(200), unique=True)
    gender = db.Column(db.String(200), unique=True)
    phone = db.Column(db.String(200), unique=True)
    DOB = db.Column(db.Date)
    address = db.Column(db.String(200), unique=True)
    pics_url = db.Column(db.String(200), unique=True)
    education = db.Column(db.String(200), unique=True)
    #Active = db.Column(db.Boolean, unique=False)
    #DateCreated = db.Column(db.DateTime, db.DateTime, default=datetime.datetime.utcnow(), unique=True)
    
  
    def __init__(self, FirstName, LastName, UserName, UserPassword, UserEmail, RoleName, RoleActive):
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.UserPassword = generate_password_hash(UserPassword)
        self.UserEmail = UserEmail
        self.RoleName = RoleName
        self.RoleActive = RoleActive
        
  
    def __init__(self, firstname, lastname, email, datejoined, desgnation, gender, phone, DOB, address, pics_url, education):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.datejoined = datejoined
        self.desgnation = desgnation
        self.gender = gender
        self.phone = phone
        self.DOB = DOB
        self.address = address
        self.pics_url = pics_url
        self.education = education
        

'''
    def check_password(self, UserPassword1):
        return check_password_hash(self.password_hash, UserPassword)
        
        
    __tablename__ = 'staff_table'
    Staff_ID = db.Column(db.Integer, primary_key = True)
    FirstName = db.Column(db.String(200), unique=True)
    LastName = db.Column(db.String(200), unique=True)
    UserName = db.Column(db.String(200), unique=True, nullable=False)
    UserEmail = db.Column(db.String(100), unique=True)
    #Active = db.Column(db.Boolean, unique=False)
    #DateCreated = db.Column(db.DateTime, db.DateTime, default=datetime.datetime.utcnow(), unique=True)
   
        
    def __init__(self, FirstName, LastName, UserName, UserPassword, UserEmail):
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.UserPassword = generate_password_hash(UserPassword)
        #self.UserPassword = UserPassword
        self.UserEmail = UserEmail

'''

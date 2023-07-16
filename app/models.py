from .extentions import *


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable= False)
    password = db.Column(db.String,nullable=False)
    
    cources= db.relationship('Cource',back_populates='instructor',lazy=True)
    
    
class Cource(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String,nullable = False)
    instructor_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    students = db.relationship('Student',backref='cource_taken',lazy=True)
    instructor = db.relationship('User',back_populates='cources')
    
class Student(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String,nullable = False)
    cource_id = db.Column(db.Integer,db.ForeignKey("cource.id"))
    
    cource = db.relationship('Cource',backref='by_student',lazy=True)
from flask_restx import Resource,Namespace
from werkzeug.security import generate_password_hash,check_password_hash
from .models import *
from .api_models import *
from flask import request
from flask_jwt_extended import jwt_required,get_jwt_identity,create_access_token,create_refresh_token



authorizations = {
    "jsonWebToken":{
        "type":"apiKey",
        "in":"Header",
        "name":"Authorization"
    }
}


ns = Namespace('api',authorizations=authorizations)

@ns.route('/apidocs')
class Customer(Resource):
    def get(self):
        return {"hello":"customers"}

@ns.route('/register')
class Register(Resource):
    @ns.expect(register_input_model)
    def post(self):
        try: 
            password =generate_password_hash(ns.payload["password"])
            user =User(username= ns.payload["username"],password= password)
            db.session.add(user)
            db.session.commit()
            return {"message":"registerd sucessfully"}
        except Exception as e:
            return {"error":f"error occured is {e}"}
            
@ns.route('/login')
class Login(Resource):
    @ns.expect(login_input_model)
    def post(self):
        try:
            username= ns.payload["username"]
            password = ns.payload["password"]
            user = User.query.filter(User.username==username).first()
            if not user:
                return {"message":"User Not Found"},401
            if not check_password_hash(user.password,password):
                return {"message":"password does not match"}
            token = create_access_token(username)
            return {"message":"Login successful",
                    "token":token},201
        except Exception as e :
            return {"error":e}
                
        
        
            
        
    
        
        

@ns.route('/cources')
class CourcesListApi(Resource):
    @jwt_required()
    @ns.doc(security = "jsonWebToken")
    @ns.marshal_list_with(cource_model)
    def get(self):
        return Cource.query.all()
    
    @ns.marshal_list_with(cource_model)
    @ns.expect(cource_input_model)
    def post(self):
        print(ns.payload["name"])
        name = ns.payload["name"]
        cource = Cource(name =name)
        db.session.add(cource)
        db.session.commit()
        return cource

@ns.route('/cources/<int:id>')
class CourceApi(Resource):
    @ns.marshal_with(cource_model)
    def get(self,id):
        cource = Cource.query.filter_by(id = id).first()
        return cource,201
    
    @ns.expect(cource_input_model)
    @ns.marshal_with(cource_model)
    def put(self, id):
        name = ns.payload["name"]
        cource = Cource.query.filter_by(id = id).first()
        cource.name =name
        db.session.commit()
        return cource,201
        
    def delete(self,id):
        cource = Cource.query.filter_by(id=id).first()
        if cource is None:
            return {"message": "Cource not found"}, 404
        try:
            db.session.delete(cource)
            db.session.commit()
            return {}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": "Error deleting cource"}, 500
        
        
        
@ns.route('/students')
class Students(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()  
    
    @ns.marshal_list_with(student_model)
    @ns.expect(student_input_model)
    def post(self):
        name=ns.payload['name']
        cource_id =ns.payload['cource_id']
        student = Student(name=name,cource_id =cource_id)
        db.session.add(student)
        db.session.commit()
        return student
    
    
    
@ns.route('/students/<int:id>')
class Students_Ind(Resource):    
    @ns.marshal_with(student_model)
    def get(self,id):
        std = Student.query.filter_by(id=id).first()
        return std
        
        
    @ns.marshal_with(student_model)
    @ns.expect(student_input_model)
    def put(self,id):
        std = Student.query.filter_by(id=id).first()
        std.name = ns.payload['name']
        std.cource_id = ns.payload['cource_id']
        db.session.commit()
        return std,200
    
    @ns.marshal_with(student_model)
    def delete(self,id):
        std = Student.query.filter_by(id=id).first()
        db.session.delete(std)
        db.session.commit()
        return {},204
        
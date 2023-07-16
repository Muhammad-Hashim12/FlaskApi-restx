from flask_restx import fields
from .extentions import api

#model validation
student_model =api.model("Student",{
    "id": fields.Integer,
    "name":fields.String,
})

cource_model = api.model("Cource",{
    "id" : fields.Integer,
    "name" : fields.String,
    "students":fields.Nested(student_model)
})


#for input <instaed of reqparse>
cource_input_model = api.model("Cource",{
    "name":fields.String
})

student_input_model = api.model('Student',{
     "name":fields.String,
     "cource_id":fields.Integer
})

register_input_model = api.model('User',{
    "username":fields.String,
    "password":fields.String
})

login_input_model = api.model('User',{
    "username":fields.String,
    "password":fields.String
})
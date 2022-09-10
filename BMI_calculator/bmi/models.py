from BMI_calculator import db

class Bmi_tab(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(50),unique=True,primary_key=True)
    weight= db.Column(db.Float)
    height= db.Column(db.Float)
    bmi_res= db.Column(db.Float)
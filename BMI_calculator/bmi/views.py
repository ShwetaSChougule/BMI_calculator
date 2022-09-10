from flask import Blueprint,render_template,request,redirect,url_for
from bmi.models import Bmi_tab
from BMI_calculator import db
# create blueprint
mod = Blueprint('bmi',__name__,url_prefix ="/bmi")

@mod.route("/bmi_calc",methods=['GET','POST'])
def fetch_name():
    bmi_res =' '
    if request.method == 'POST' and 'weight' in request.form:
        name = request.form.get('name')
        weight = int(request.form.get('weight'))
        height = int(request.form.get('height'))
        bmi_res = calc(weight,height)
    # #     to put data  to table
        u = Bmi_tab(
            name = name,
            weight =weight,
            height = height,
            bmi_res = bmi_res
            )
        db.session.add(u)
        db.session.commit()
    return render_template("index.html",content=bmi_res)

def calc(weight,height):
    return round(weight/((height*0.01)**2),2)


@mod.route("/bmi_calc",methods=['GET','POST'])
def update_data():
    if request.method == 'GET':

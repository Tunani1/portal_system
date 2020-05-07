from flask import Flask, flash, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash

from models import *
from flask.helpers import flash

app = Flask(__name__)

ENV = 'env'

if ENV == 'env':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Tunani14real@localhost:8888/sch_db'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

@app.route('/home')
def index():
    return render_template('home.html')

# Students URL
@app.route('/students')
def students():
    return render_template('students.html')

@app.route('/add_student')
def add_student():
    return render_template('add_student.html')

@app.route('/add_user')
def add_user():
    return render_template('add_user.html')

@app.route('/about_student')
def about_student():
    return render_template('about_student.html')

@app.route('/edit_student')
def edit_student():
    return render_template('edit_student.html')


# Course URL
@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/add_course')
def add_course():
    return render_template('add_course.html')

@app.route('/about_course')
def about_course():
    return render_template('about_course.html')

@app.route('/edit_course')
def edit_course():
    return render_template('edit_course.html')


# Faculty URL
@app.route('/faculties')
def faculties():
    return render_template('faculties.html')

@app.route('/add_faculty')
def add_faculty():
    return render_template('add_faculty.html')

@app.route('/edit_faculty')
def edit_faculty():
    return render_template('edit_faculty.html')


# Department URL
@app.route('/departments')
def departments():
    return render_template('departments.html')

@app.route('/add_department')
def add_department():
    return render_template('add_department.html')

@app.route('/edit_department')
def edit_department():
    return render_template('edit_department.html')


# Fees Colllection URL
@app.route('/fees')
def fees():
    return render_template('fees.html')

@app.route('/add_fee')
def add_fee():
    return render_template('add_fee.html')

@app.route('/fee_receipt')
def fee_receipt():
    return render_template('fee_receipt.html')


# Professors URL
@app.route('/professors')
def professors():
    return render_template('professors.html')

@app.route('/add_professor')
def add_professor():
    return render_template('add_professor.html')

@app.route('/about_professor')
def about_professor():
    return render_template('about_professor.html')

@app.route('/edit_professor')
def edit_professor():
    return render_template('edit_professor.html')

# Staffs URL
@app.route('/staffs')
def staffs():
    return render_template('staffs.html')

@app.route('/add_staff')
def add_staff():
    return render_template('add_staff.html')

@app.route('/about_staff')
def about_staff():
    return render_template('about_staff.html')

@app.route('/edit_staff')
def edit_staff():
    return render_template('edit_staff.html')

# Login URL

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def logins():
    return render_template('logins.html', msg='')

# Signup URL
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Login Function
@app.route('/home', methods=['POST', 'GET'])
def DBLogin():
    
    if request.method == 'POST':
        user = db.session.query(DBClass).filter_by(UserName = request.form['UserName']).first()
        UserPassword = request.form['UserPassword']
        
        if user and check_password_hash(user.UserPassword, UserPassword):
            #flash('Ade')
            return redirect(url_for('index'))
            #return render_template('home.html')
        else:
            msg = 'Incorrect username or password!'
            return render_template('logins.html', msg=msg)
        
        msg = ''
        return render_template('logins.html', msg=msg)
    
 #image = request.files['fileimg'].read()

# User Creation Function
@app.route('/add_user', methods=['POST', 'GET'])
def submitUser():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        UserName = request.form['UserName']
        UserPassword = request.form['UserPassword']
        UserEmail = request.form['UserEmail']
        #print(UserPassword, UserEmail)
        if db.session.query(DBClass).filter(DBClass.FirstName == FirstName).count() == 0:
            data = DBClass(FirstName, LastName, UserName, UserPassword, UserEmail)
            db.session.add(data)
            db.session.commit()
            
            #return redirect(url_for('home'))
            return render_template('home.html')
        
        return render_template('add_user.html')
  

# Staff Function
@app.route('/add_staff', methods=['POST', 'GET'])
def submitStaff():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        datejoined = request.form['datejoined']
        desgnation = request.form['desgnation']
        gender = request.form['gender']
        phone = request.form['phone']
        DOB = request.form['DOB']
        address = request.form['address']
        pics_url = request.form['pics_url']
        education = request.form['education']
        #print(UserPassword, UserEmail)
        if db.session.query(DBClass3).filter(DBClass3.firstname == firstname).count() == 0:
            data = DBClass3(firstname, lastname, email, datejoined, desgnation, gender, phone, DOB, address, pics_url, education)
            db.session.add(data)
            db.session.commit()
            
            #return redirect(url_for('home'))
            return render_template('home.html')
        
        return render_template('add_staff.html')
if __name__ == "__main__":
    app.run()

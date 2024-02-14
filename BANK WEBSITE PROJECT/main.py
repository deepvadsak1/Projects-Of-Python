from flask import Flask, render_template, request, jsonify,url_for,redirect
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies
from datetime import datetime, timedelta
import mysql.connector
import json

app = Flask(__name__)
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
app.config["JWT_COOKIE_SECURE"] = True
app.config["SECRET_KEY"] = 'fwni464dg3riFCB34694'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:@localhost/yourbank'
jwt = JWTManager(app)
db = mysql.connector.connect(
  host="localhost",
  user="deep",
  password="deep",
  database="yourbank"
)

users = {
    'user1': {
        'username': 'user1',
        'password': 'password1',
        'email': 'email'
    },
    'user2': {
        'username': 'user2',
        'password': 'password2',
        'email' : 'email'
    }
}
JWT_SECRET_KEY = 'hsa784hf4abvhj94ty7jcavhk'


@jwt.unauthorized_loader
@jwt.invalid_token_loader
def custom_unauthorized_response(_err):
    return redirect(url_for('login'))

@app.route("/")
def main_page():
    return render_template('main_page.html')

# @jwt.unauthorized_loader
# @jwt.invalid_token_loader           
@app.route("/logout", methods=["POST",'GET'])
def logout_with_cookies():
    response = redirect(url_for('ac_page'))
    unset_jwt_cookies(response)
    return response



@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username_input = request.form.get("email")
        password = request.form.get("password")
        mycursor = db.cursor(dictionary=True)

        mycursor.execute('SELECT * FROM `signin` WHERE `email` = "' + username_input + '" AND `password` = "' + password + '";')

        myresult = mycursor.fetchone()
        if myresult is not None:
            access_token = create_access_token(identity=username_input)
            response = redirect("/index")
            set_access_cookies(response, access_token)
            return response
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


    


@app.route("/signin", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        phone_no = request.form.get("phone_no")
                                                                                                             
        

        mycursor = db.cursor(dictionary=True)

        mycursor.execute('INSERT INTO `signin`(`email`,`name`, `password`,`phone_no`, `srno`) VALUES ("'+email+'","'+name+'","'+password+'","'+phone_no+'","null")')

        db.commit()

        if name in users:
            return "User already exists! Please choose a different username."
        
        users[name] = {'name': name, 'password': password, 'email': email, 'phone_no': phone_no}
        return render_template('index.html')

    return render_template('signin.html')



@app.route("/about", methods=['GET', 'POST'])
@jwt_required()
def about():
    if request.method == 'POST':
        email = request.form.get('email')
        mycursor = db.cursor(dictionary=True)
        mycursor.execute('INSERT INTO `subscribe`(`email`,`srno`) VALUES ("'+email+'","null")')
        db.commit()
        users[email] = {'email':email}
        return render_template('about.html')
    return render_template('about.html')



@app.route("/service", methods=['GET','POST'])
@jwt_required()
def services():
    
    if request.method == 'POST':
        email = request.form.get('email')
        mycursor = db.cursor(dictionary=True)
        mycursor.execute('INSERT INTO `subscribe`(`email`,`srno`) VALUES ("'+email+'","null")')
        db.commit()
        users[email] = {'email':email}
        return render_template('service.html')
    return render_template('service.html')



@app.route("/contact", methods = ['GET','POST'])
@jwt_required()
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone_no = request.form.get('phone_no')
        email = request.form.get('email')
        message = request.form.get('message')
        
        mycursor = db.cursor(dictionary=True)
        mycursor.execute('INSERT INTO `contacts` (`name`,`phone_no`, `email`,`message`, `srno`) VALUES ("'+name+'","'+phone_no+'","'+email+'","'+message+'","null")')
        db.commit()

        if name in users:
            return "User already exists! Please choose a different username."
        else:
            users[name] = {'name':name, 'phone_no':phone_no, 'email':email, 'message':message}
            return render_template('contact.html')
    if request.method == 'POST':
        email = request.form.get('email')
        mycursor = db.cursor(dictionary=True)
        mycursor.execute('INSERT INTO `subscribe`(`email`,`srno`) VALUES ("'+email+'","null")')
        db.commit()
        users[email] = {'email':email}
        return render_template('contact.html')
    return render_template('contact.html')



@app.route("/index", methods = ['GET','POST'])
@jwt_required()
def index():
    if request.method == 'POST':
            name = request.form.get('name')
            phone_no = request.form.get('phone_no')
            email = request.form.get('email')
            message = request.form.get('message')
            
            mycursor = db.cursor(dictionary=True)
            mycursor.execute('INSERT INTO `contacts` (`name`,`phone_no`, `email`,`message`, `srno`) VALUES ("'+name+'","'+phone_no+'","'+email+'","'+message+'","null")')
            db.commit()

            if name in users:
                return "User already exists! Please choose a different username."
            else:
                users[name] = {'name':name, 'phone_no':phone_no, 'email':email, 'message':message}
                return render_template('contact.html')

    if request.method == 'POST':
        email = request.form.get('email')
        mycursor = db.cursor(dictionary=True)
        mycursor.execute('INSERT INTO `subscribe`(`email`,`srno`) VALUES ("'+email+'","null")')
        db.commit()
        users[email] = {'email':email}
        return render_template('index.html')
    return render_template('index.html')


@app.route("/acno", methods = ['GET','POST'])
def create_ac_no():
    ac_no = request.form.get('ac_no')
    pin = request.form.get('pin')

    mycursor = db.cursor(dictionary=True)
    mycursor.execute('INSERT INTO `accounts` (`ac_no`,`pin`,`srno`) VALUES ("'+ac_no+'","'+pin+'","null")')
    db.commit()

    if ac_no in users:
            return "User already exists! Please choose a different account number."
    else:
            users[ac_no] = {'ac_no':ac_no, 'pin':pin}
            return render_template('contact.html')
    

if __name__ == "__main__":
    app.run(debug=True)


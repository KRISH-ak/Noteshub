from flask import Flask, render_template, request, redirect, url_for
import pymysql
from werkzeug.utils import secure_filename
import os

from flask_session import Session

regi = {}

conn = pymysql.connect(host = 'localhost', user='root',password="",db='noteshub')
app = Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)
UPLOAD_FOLDER = 'static'

@app.route('/')
def login():
    return render_template('/login.html')


@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/about')
def about():
    return render_template('/about.html')

@app.route('/courses')
def courses():
    return render_template('/courses.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/user_reg', methods=['POST'])
def user_reg():
    if request.method == 'POST':
        name = request.form['name1']
        email = request.form['email']
        password = request.form['password']
        
        
        
        cursor = conn.cursor()
        query = "SELECT * FROM user_reg WHERE name = %s"
        val = (name,)
        cursor.execute(query,val)
        existing_user = cursor.fetchone()
        cursor.close()
        
        if existing_user:
            return render_template('login.html', error ="username already exists.")
        
        cursor = conn.cursor()
        query = "INSERT INTO user_reg (name, email, password) VALUES(%s,%s,%s)"
        val = (name,password,email)
        cursor.execute(query,val)
        conn.commit()
        cursor.close()
        
        return render_template('index.html', success="Registration successfully") 
        
@app.route('/user_login', methods=['POST'])
def user_login():
    cursor = conn.cursor()
    email = request.form['email']
    password = request.form['password']
    print(email)
    print(password)

    query = "SELECT * FROM user_reg WHERE email=%s AND password=%s"

    val = (password,email )
    cursor.execute(query, val)
    user = cursor.fetchone()
    cursor.close()
    print(user)

    if user:
      
        return render_template('/index.html')
    else:
        # Failed login
        return render_template('login.html', login_error=True)

app.run(debug = True)
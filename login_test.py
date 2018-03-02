import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.config['USERNAME']="admin"
app.config['PASSWORD']="admin"
app.config['ADMINPASSWORD']="ofcl2504"
app.config['SECRET_KEY']="xeew\xe4\xc0\xee\xb1]\x9b\xa0\x9e)\x15Qhem\xe5\xf17\xd6\xceB\xb7\xb4"
app.config['DATABASE']="user.db"

@app.route('/')
def show_mainpage():
	if not session.get('logged_in'):
		return redirect(url_for('login'))
	else:
		return "<h1>main page</h1><a href='%s'>logout</a>"%(url_for('logout'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
        if request.method == 'POST':
                if request.form['username'] != app.config['USERNAME']:
                        error = 'Invalid Username'
			return render_template('error.html', error=error, nextpage="login")
                elif request.form['password'] != app.config['PASSWORD']:
                        error = 'Invalid Password'
			return render_template('error.html',error=error, nextpage="login")
                else:
                        session['logged_in'] = True
                        flash('You were logged in')
                        return "<h1>main page</h1><a href='%s'>logout</a>"%(url_for('logout'))
        return render_template('login_new.html')

@app.route('/logout')
def logout():
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('login'))


#user register and database settings\
def connect_db():
        return sqlite3.connect(app.config['DATABASE'])

def init_db():
        coon = connect_db()
        c = coon.cursor()
        c.execute('''CREATE TABLE USERS
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME TEXT NOT NULL,
                PASSWORD TEXT NOT NULL);''')
        coon.commit()
        coon.close()

def insert_db(username, password):
        coon = connect_db()
        c = coon.cursor()
	sql = "INSERT INTO USERS (USERNAME, PASSWORD) VALUES ('%s', '%s');"%(username, password)
        c.execute(sql)
        coon.commit()
        coon.close()


@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		adminpassword = request.form['adminpassword']
		print adminpassword
		if adminpassword == app.config['ADMINPASSWORD']:
			insert_db(username, password)
			
			return "<head><meta http-equiv=\"refresh\" content=\"1;url='%s'\"></head><h1>register success!</h1>"%(url_for('login'))
		else:
			error = "Invalid adminpassword"
			return render_template('error.html', error=error)
	else:
		return render_template('register_new.html', error=error)
	

if __name__ == '__main__':
        app.run()


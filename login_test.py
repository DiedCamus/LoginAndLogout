import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.config['USERNAME']="admin"
app.config['PASSWORD']="admin"
app.config['SECRET_KEY']="xeew\xe4\xc0\xee\xb1]\x9b\xa0\x9e)\x15Qhem\xe5\xf17\xd6\xceB\xb7\xb4"

@app.route('/')
def show_mainpage():
	if not session.get('logged_in'):
		return "please log in"
	else:
		return "main page"

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
        if request.method == 'POST':
                if request.form['username'] != app.config['USERNAME']:
                        error = 'Invalid username'
                elif request.form['password'] != app.config['PASSWORD']:
                        error = 'Invalid password'
                else:
                        session['logged_in'] = True
                        flash('You were logged in')
                        return "main page"
        return render_template('login.html', error=error)

@app.route('/logout')
def logout():
        session.pop('logged_in', None)
        flash('You were logged out')
        return "please log in"

if __name__ == '__main__':
        app.run()


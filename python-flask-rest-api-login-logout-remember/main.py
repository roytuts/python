import pymysql
from app import app, COOKIE_TIME_OUT
from db import mysql
from flask import flash, session, render_template, request, redirect, make_response
from werkzeug import generate_password_hash, check_password_hash

@app.route('/')
def index():
	if 'email' in session:
		username = session['email']
		return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>Click here to logout</a></b>"
	return "You are not logged in <br><a href = '/login'></b>" + "click here to login</b></a>"
	
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/submit', methods=['POST'])
def login_submit():
	conn = None
	cursor = None
	
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	_remember = request.form.getlist('inputRemember')
	
	if 'email' in request.cookies:
		username = request.cookies.get('email')
		password = request.cookies.get('pwd')
		conn = mysql.connect()
		cursor = conn.cursor()
		sql = "SELECT * FROM user WHERE user_email=%s"
		sql_where = (username,)
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		if row and check_password_hash(row[3], password):
			print(username + ' ' + password)
			session['email'] = row[2]
			cursor.close()
			conn.close()
			return redirect('/')
		else:
			return redirect('/login')
	# validate the received values
	elif _email and _password:
		#check user exists			
		conn = mysql.connect()
		cursor = conn.cursor()
		sql = "SELECT * FROM user WHERE user_email=%s"
		sql_where = (_email,)
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		if row:
			if check_password_hash(row[3], _password):
				session['email'] = row[2]
				cursor.close() 
				conn.close()
				if _remember:
					resp = make_response(redirect('/'))
					resp.set_cookie('email', row[2], max_age=COOKIE_TIME_OUT)
					resp.set_cookie('pwd', _password, max_age=COOKIE_TIME_OUT)
					resp.set_cookie('rem', 'checked', max_age=COOKIE_TIME_OUT)
					return resp
				return redirect('/')
			else:
				flash('Invalid password!')
				return redirect('/login')
		else:
			flash('Invalid email/password!')
			return redirect('/login')
	else:
		flash('Invalid email/password!')
		return redirect('/login')
		
@app.route('/logout')
def logout():
	if 'email' in session:
		session.pop('email', None)
	return redirect('/')

if __name__ == "__main__":
    app.run()
import pymysql
from app import app
from db_config import mysql
from flask import flash, session, render_template, request, redirect
from werkzeug import generate_password_hash, check_password_hash

@app.route('/')
def index():
	if 'email' in session:
		username = session['email']
		return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to logout</a></b>"
	return "You are not logged in <br><a href = '/login'></b>" + "click here to login</b></a>"
	
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/submit', methods=['POST'])
def login_submit():
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	# validate the received values
	if _email and _password and request.method == 'POST':
		#check user exists			
		conn = mysql.connect()
		cursor = conn.cursor()
		sql = "SELECT * FROM tbl_user WHERE user_email=%s"
		sql_where = (_email,)
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		if row:
			if check_password_hash(row[3], _password):
				session['email'] = row[1]
				cursor.close() 
				conn.close()
				return redirect('/')
			else:
				flash('Invalid password!')
				return redirect('/login')
		else:
			flash('Invalid email/password!')
			return redirect('/login')
		
@app.route('/logout')
def logout():
	session.pop('email', None)
	return redirect('/')

if __name__ == "__main__":
    app.run()
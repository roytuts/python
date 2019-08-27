import pymysql
from app import app
from db_config import mysql
from flask import flash, render_template, request, redirect, url_for
from werkzeug import generate_password_hash, check_password_hash
		
@app.route('/register', methods=['POST'])
def save_user_info():
	cursor = None
	try:
		name = request.form['name']
		dob = request.form['dob']
		gender = request.form['gender']
		password = request.form['password']
		phone = request.form['phone']
		email = request.form['email']
		address = request.form['address']
		
		# validate the received values
		if name and dob and gender and password and phone and email and address and request.method == 'POST':
		
			#do not save password as a plain text
			_hashed_password = generate_password_hash(password)
			
			# save user information
			sql = "INSERT INTO user(name, password, email, phone, gender, dob, address) VALUES(%s, %s, %s, %s, %s, %s, %s)"
			data = (name, _hashed_password, email, phone, gender, dob, address)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			
			flash('You registered successfully!')
			
			return redirect(url_for('.home'))
		else:			
			return 'Error while saving user information'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def home():
	return render_template('multi-step-registration.html')
		
if __name__ == "__main__":
    app.run()
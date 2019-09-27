import pymysql
from app import app
from db import mysql
from flask import jsonify, request, session
from werkzeug import check_password_hash
		
@app.route('/')
def home():
	if 'username' in session:
		username = session['username']
		return jsonify({'message' : 'You are already logged in', 'username' : username})
	else:
		resp = jsonify({'message' : 'Unauthorized'})
		resp.status_code = 401
		return resp

@app.route('/login', methods=['POST'])
def login():
	conn = None;
	cursor = None;
	
	try:
		_json = request.json
		_username = _json['username']
		_password = _json['password']
		
		# validate the received values
		if _username and _password:
			#check user exists			
			conn = mysql.connect()
			cursor = conn.cursor()
			
			sql = "SELECT * FROM user WHERE username=%s"
			sql_where = (_username,)
			
			cursor.execute(sql, sql_where)
			row = cursor.fetchone()
			
			if row:
				if check_password_hash(row[2], _password):
					session['username'] = row[1]
					#cursor.close()
					#conn.close()
					return jsonify({'message' : 'You are logged in successfully'})
				else:
					resp = jsonify({'message' : 'Bad Request - invalid password'})
					resp.status_code = 400
					return resp
		else:
			resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
			resp.status_code = 400
			return resp

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()
		
@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return jsonify({'message' : 'You successfully logged out'})
		
if __name__ == "__main__":
    app.run()
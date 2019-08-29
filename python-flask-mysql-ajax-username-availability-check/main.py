import pymysql
from app import app
from db_config import mysql
from flask import jsonify, request, render_template
		
@app.route('/user_check', methods=['POST'])
def username_check():
	conn = None
	cursor = None
	try:
		username = request.form['username']
		
		# validate the received values
		if username and request.method == 'POST':		
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute("SELECT * FROM user WHERE login_username=%s", username)
			row = cursor.fetchone()
			
			if row:
				resp = jsonify('<span style=\'color:red;\'>Username unavailable</span>')
				resp.status_code = 200
				return resp
			else:
				resp = jsonify('<span style=\'color:green;\'>Username available</span>')
				resp.status_code = 200
				return resp
		else:
			resp = jsonify('<span style=\'color:red;\'>Username is required field.</span>')
			resp.status_code = 200
			return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def home():
	return render_template('username.html')
		
if __name__ == "__main__":
    app.run()
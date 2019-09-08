import pymysql
from app import app
from db import mysql
from flask import jsonify, request

@app.route('/user')
def get_user():
	conn = None;
	cursor = None;
	try:
		id = request.args.get('id')
		if id:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute("SELECT user_id id, user_name name, user_email email, user_password pwd FROM user WHERE user_id=%s", id)
			row = cursor.fetchone()
			resp = jsonify(row)
			resp.status_code = 200
			return resp
		else:
			resp = jsonify('User "id" not found in query string')
			resp.status_code = 500
			return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
if __name__ == "__main__":
    app.run()
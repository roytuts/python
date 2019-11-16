import pymysql
from db_config import mysql
from werkzeug import generate_password_hash, check_password_hash

def user_exist(email):
	conn = None;
	cursor = None;
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		
		sql = "SELECT email FROM user WHERE email=%s"
		sql_where = (email,)
		
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		
		if row:
			return True
		return False

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()

def register(email, name, pwd):
	conn = None;
	cursor = None;
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		
		sql = "INSERT INTO user(name, email, pwd) VALUES(%s, %s, %s)"
		data = (name, email, generate_password_hash(pwd),)
		
		cursor.execute(sql, data)
		
		conn.commit()

	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()
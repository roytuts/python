import pymysql
from app import app
from db_config import mysql
from flask import flash, render_template, jsonify

@app.route('/')
def home():
	return render_template('calendar_events.html')

@app.route('/calendar-events')
def calendar_events():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, title, url, class, UNIX_TIMESTAMP(start_date)*1000 as start, UNIX_TIMESTAMP(end_date)*1000 as end FROM event")
		rows = cursor.fetchall()
		resp = jsonify({'success' : 1, 'result' : rows})
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
if __name__ == "__main__":
    app.run()
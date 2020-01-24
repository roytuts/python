import pymysql
from app import app
from db import mysql
from flask import jsonify, request, render_template

@app.route('/')
def home():
	return render_template('xchart.html')

@app.route('/xchart', methods=['POST'])
def x_chart():
	conn = None
	cursor = None

	_json = request.json	
	start_date = _json['start']
	end_date = _json['end']	
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		sql = "SELECT SUM(no_of_visits) total_visits, DATE(access_date) day_date FROM site_log WHERE DATE(access_date) >= %s AND DATE(access_date) <= %s GROUP BY DATE(access_date) ORDER BY DATE(access_date) DESC";

		param = (start_date, end_date)
		
		cursor.execute(sql, param)
		
		rows = cursor.fetchall()
		
		data = []
		
		for row in rows:
			data.append({'label':row['day_date'], 'value':int(row['total_visits'])})

		resp = jsonify(data)
		
		resp.status_code = 200
		
		return resp
	
	except Exception as e:
		print(e)

	finally:
		if cursor and conn:
			cursor.close()
			conn.close()
		
if __name__ == "__main__":
    app.run()
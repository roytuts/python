import io
import csv
import pymysql
from app import app
from db import mysql
from flask import Flask, Response, render_template

@app.route('/')
def download():
	return render_template('download.html')

@app.route('/download/report/csv')
def download_report():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		cursor.execute("SELECT emp_id, emp_first_name, emp_last_name, emp_designation FROM employee")
		result = cursor.fetchall()

		output = io.StringIO()
		writer = csv.writer(output)
		
		line = ['Emp Id, Emp First Name, Emp Last Name, Emp Designation']
		writer.writerow(line)

		for row in result:
			line = [str(row['emp_id']) + ',' + row['emp_first_name'] + ',' + row['emp_last_name'] + ',' + row['emp_designation']]
			writer.writerow(line)

		output.seek(0)
		
		return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=employee_report.csv"})
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

if __name__ == "__main__":
    app.run()
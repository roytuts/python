import io
import xlwt
import pymysql
from app import app
from db import mysql
from flask import Flask, Response, render_template

@app.route('/')
def upload_form():
	return render_template('download.html')

@app.route('/download/report/excel')
def download_report():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		cursor.execute("SELECT emp_id, emp_first_name, emp_last_name, emp_designation FROM employee")
		result = cursor.fetchall()
		
		#output in bytes
		output = io.BytesIO()
		#create WorkBook object
		workbook = xlwt.Workbook()
		#add a sheet
		sh = workbook.add_sheet('Employee Report')
		
		#add headers
		sh.write(0, 0, 'Emp Id')
		sh.write(0, 1, 'Emp First Name')
		sh.write(0, 2, 'Emp Last Name')
		sh.write(0, 3, 'Designation')
		
		idx = 0
		for row in result:
			sh.write(idx+1, 0, str(row['emp_id']))
			sh.write(idx+1, 1, row['emp_first_name'])
			sh.write(idx+1, 2, row['emp_last_name'])
			sh.write(idx+1, 3, row['emp_designation'])
			idx += 1
		
		workbook.save(output)
		output.seek(0)
		
		return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=employee_report.xls"})
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

if __name__ == "__main__":
    app.run()
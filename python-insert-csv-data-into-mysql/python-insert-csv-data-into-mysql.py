import csv
import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='roytuts')

cur = conn.cursor()

#file = open('students.csv')
file = open('students-header.csv')
csv_data = csv.reader(file)

skipHeader = True

for row in csv_data:
	if skipHeader:
		skipHeader = False
		continue
	cur.execute('INSERT INTO student(student_id, student_name, student_dob, student_email, student_address)' 'VALUES(%s, %s, %s, %s, %s)', row)

#query = "LOAD DATA INFILE 'C:/python/python-insert-csv-data-into-mysql/students-header.csv' INTO TABLE student FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (student_id, student_name, student_dob, student_email, student_address)"

#query = "LOAD DATA INFILE 'C:/python/python-insert-csv-data-into-mysql/students.csv' INTO TABLE student FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (student_id, student_name, student_dob, student_email, student_address)"

#cur.execute(query)

conn.commit()

conn.close()
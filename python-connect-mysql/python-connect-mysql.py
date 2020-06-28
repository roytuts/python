#import mysql.connector

#conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='roytuts')

#print (conn)

#conn.close()

#from mysql.connector import (connection)

#conn = connection.MySQLConnection(user='root', password='root', host='127.0.0.1', database='roytuts')

#print (conn)

#conn.close()

#import mysql.connector
#from mysql.connector import errorcode

#try:
#	conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='roytuts')

#	print (conn)
#except mysql.connector.Error as err:
#	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#		print("Something is wrong with user name or password")
#	elif err.errno == errorcode.ER_BAD_DB_ERROR:
#		print("Database does not exist")
#	else:
#		print(err)
#else:
#	conn.close()

#import mysql.connector

#config = {
#	'user': 'root',
#	'password': 'root',
#	'host': '127.0.0.1',
#	'database': 'roytuts',
#	'raise_on_warnings': True
#}

#conn = mysql.connector.connect(**config)

#print (conn)

#conn.close()

import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='roytuts', use_pure=True)

print (conn)

conn.close()

